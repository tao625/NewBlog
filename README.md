# 时间显示程序

一个简洁实用的 Python 时间显示工具，支持命令行和 GUI 两种模式。

## 功能特点

- 实时显示当前时间和日期
- 多种时间格式支持
- 自动刷新功能
- 可打包为独立 exe 运行

## 文件说明

| 文件 | 说明 |
|------|------|
| `time_app.py` | GUI 版本，使用 tkinter 构建界面 |
| `time_automation.py` | 命令行版本，支持定时刷新 |

## 使用方法

### GUI 版本

```bash
python time_app.py
```

功能：
- 实时显示时间和日期
- 切换多种时间格式（默认/完整/仅时间/ISO）
- 自动刷新开关，可调节间隔

### 命令行版本

```bash
python time_automation.py
```

## 打包为 exe

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "时间显示程序" time_app.py
```

生成的 exe 文件位于 `dist/` 目录下。

## 环境要求

- Python 3.6+
- tkinter（Python 内置）

## 许可证

MIT License
