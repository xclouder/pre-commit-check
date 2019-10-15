# pre-commit-check

此工具目标是在客户端提交代码时，做一些必要的检查，防止错误代码不小心提交。

目前会检查代码中的Debug.Log类接口。这种API在真机上性能比较差，只能本地调试的时候使用，提交代码时需要去掉。计划未来持续扩展，检测更多的错误情况。

此工具使用TortoiseSVN的客户端svnhook实现。使用方式如下：
1、拉取检查python脚本：
https://github.com/xclouder/pre-commit-check.git

2、配置TortoiseSVN的client hook

3、Command Line To Execute栏输入
python 你的计算机上检查脚本位置
