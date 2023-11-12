# Kaggle-Sleep-Detection

此项目为kaggle2023睡眠质量检测比赛的代码

小组成员：谢天，郭俊荣，杨锦东，张又升

目前采用Transformer架构，实现了经典的encoder-decoder结构，后续会加入attention机制.

在/run文件夹下运行此项目,/run/conf通过yaml完成模型配置，具体模型实现在/src目录下

暂时没有使用时序模型的SOTA，后续学习后尝试接入


本地训练请修改/run/conf/dir/local.yaml中的数据集路径!!