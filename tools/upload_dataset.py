import json
import shutil
from pathlib import Path
from typing import Any

import click
from kaggle.api.kaggle_api_extended import KaggleApi


def copy_files_with_exts(source_dir: Path, dest_dir: Path, exts: list):
    """
    source_dir: 探索开始的目录，即要进行文件搜索或处理的根目录。
    dest_dir: 复制到的目标目录，即处理后文件的目标存储位置。
    exts: 目标文件的扩展名列表，即要处理的特定类型文件的扩展名列表，例如 ['.txt', '.jpg']
    """

    #遍历指定目录中的文件，并根据其扩展名进行复制操作
    for ext in exts:
        for source_path in source_dir.rglob(f"*{ext}"):

            relative_path = source_path.relative_to(source_dir)
            dest_path = dest_dir / relative_path


            dest_path.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(source_path, dest_path)
            print(f"Copied {source_path} to {dest_path}")


@click.command()
@click.option("--title", "-t", default="CMI-model")
@click.option("--dir", "-d", type=Path, default="./output/train")
@click.option("--extentions", "-e", type=list[str], default=["best_model.pth", ".hydra/*.yaml"])
@click.option("--user_name", "-u", default="tubotubo")
@click.option("--new", "-n", is_flag=True)
def main(
    title: str,
    dir: Path,
    extentions: list[str] = [".pth", ".yaml"],
    user_name: str = "tubotubo",
    new: bool = False,
):

    # 使用指定的扩展名，将目录下的文件压缩为zip文件，并上传到Kaggle。

    # 参数:
    # title (str): 在上传到Kaggle时使用的标题
    # dir (Path): 包含要上传文件的目录
    # extensions (list[str], optional): 要上传的文件扩展名.
    # user_name (str, optional): Kaggle用户名.
    # new (bool, optional): 是否作为新数据集上传.

    tmp_dir = Path("./tmp")
    tmp_dir.mkdir(parents=True, exist_ok=True)

    # 拷贝扩展名为.pth的文件
    copy_files_with_exts(dir, tmp_dir, extentions)

    # 创建 dataset-metadata.json
    dataset_metadata: dict[str, Any] = {}
    dataset_metadata["id"] = f"{user_name}/{title}"
    dataset_metadata["licenses"] = [{"name": "CC0-1.0"}]
    dataset_metadata["title"] = title
    with open(tmp_dir / "dataset-metadata.json", "w") as f:
        json.dump(dataset_metadata, f, indent=4)

    # api
    api = KaggleApi()
    api.authenticate()

    if new:
        api.dataset_create_new(
            folder=tmp_dir,
            dir_mode="tar",
            convert_to_csv=False,
            public=False,
        )
    else:
        api.dataset_create_version(
            folder=tmp_dir,
            version_notes="",
            dir_mode="tar",
            convert_to_csv=False,
        )

    # delete tmp dir
    shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    main()
