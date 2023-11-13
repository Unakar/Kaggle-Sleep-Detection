import subprocess

# 定义要安装的库列表
libraries = [
    'torch-2.1.0+cu118-cp310-cp310-linux_x86_64.whl',
    'torchaudio-2.1.0+cu118-cp310-cp310-linux_x86_64.whl',
    'torchvision-0.16.0+cu118-cp310-cp310-linux_x86_64.whl',
    'segmentation-models-pytorch' ,
    'pytorch_lightning' ,
    'hydra-core --upgrade',
    'polars',
    'transformers',
    "-U 'w'andb>=0.12.10"
]

# 循环安装库
for library in libraries:
    print(f"安装 {library}...")
    subprocess.call(['pip', 'install', library])