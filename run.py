import subprocess
import zipfile

zip_path ='/home/aistudio/data/data247831/torch.zip'
save_path = '/home/aistudio/data/data247831/'

file=zipfile.ZipFile(zip_path)
file.extractall(save_path)

libraries = [
    '{}torch-2.1.0+cu118-cp310-cp310-linux_x86_64.whl'.format(save_path),
    '{}torchaudio-2.1.0+cu118-cp310-cp310-linux_x86_64.whl'.format(save_path),
    '{}torchvision-0.16.0+cu118-cp310-cp310-linux_x86_64.whl'.format(save_path),
    'segmentation-models-pytorch',
    'pytorch_lightning' ,
    'polars',
    'transformers',
    "-U 'wandb>=0.12.10'"
]

# 循环安装库
for library in libraries:
    print(f"安装 {library}...")
    subprocess.call(['pip', 'install', library])

print(f"升级 {'hydra-core'}...")
subprocess.call(['pip', 'install', 'hydra-core', '--upgrade'])
