# Pip GUI
跨平台图形化 Pip 管理工具，可视化操作 Python 包管理器，无需手动输入命令行。

## 功能特点
- 可视化图形界面，一键完成 pip 安装、卸载、查询、升级
- 实时输出 pip 运行日志，操作过程一目了然
- 全平台适配：Windows / macOS / Linux
- 配套一键依赖安装脚本，源码运行无需手动配库

## 发布包 Assets 说明
| 文件名称 | 适用平台 | 介绍 |
|--------|--------|------|
| InstallDependencies.bat | Windows | Windows 一键依赖安装脚本 |
| install_dependencies.sh | macOS / Linux | Mac & Linux 依赖安装脚本 |
| Pip-GUI-v0.1-macos.dmg | macOS | Mac 标准安装包，拖拽安装到应用程序 |
| Pip-GUI-v0.1-linuxormacos.zip | macOS / Linux | 绿色压缩包，解压即可直接运行 |
| Pip-GUI-windows-portable.exe | Windows | Windows 便携单文件版，无需安装 |
| Pip-GUI-windows-setup.exe | Windows | 7-Zip 自解压安装包，完整安装程序 |

## 使用教程
### 方式一：直接运行编译好的程序包
1. 进入仓库 Releases 页面，下载对应系统的文件
2. 运行对应程序：
- Windows 便携版：双击 `Pip-GUI-windows-portable.exe` 直接启动
- Windows 安装版：双击 `Pip-GUI-windows-setup.exe`，选择安装路径后点击安装
- Mac DMG：打开镜像，将软件拖入「应用程序」文件夹
- Mac / Linux 压缩包：解压后运行内部可执行文件

### 方式二：源码运行
1. 下载源码到本地文件夹
2. 先安装运行依赖：
Windows：双击 `InstallDependencies.bat`
Mac / Linux 终端执行：
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
3. 启动程序
```bash
python main.py
```

## 注意事项
1. 电脑需提前安装 Python 并配置系统环境变量
2. Mac / Linux 运行脚本前必须赋予执行权限
3. Windows 使用安装包安装后不会创建桌面快捷方式。

## 项目信息
项目名称：Pip GUI，
工具系列：QPALZM Toolkit，
开发作者：AdkSetup，
支持平台：全跨平台（Windows / macOS / Linux）。
