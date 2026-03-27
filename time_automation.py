"""
自动化获取时间程序
功能：获取并显示当前时间，支持定时刷新和多种格式输出
"""

import datetime
import time
import sys
import io

# 修复 Windows 控制台中文编码问题
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    import schedule
    SCHEDULE_AVAILABLE = True
except ImportError:
    SCHEDULE_AVAILABLE = False


def get_current_time():
    """获取当前时间"""
    return datetime.datetime.now()


def format_time(dt, format_type="default"):
    """根据指定格式格式化时间"""
    formats = {
        "default": "%Y-%m-%d %H:%M:%S",
        "date": "%Y年%m月%d日",
        "time": "%H:%M:%S",
        "full": "%Y年%m月%d日 %H时%M分%S秒",
        "iso": "%Y-%m-%dT%H:%M:%S"
    }
    return dt.strftime(formats.get(format_type, formats["default"]))


def display_time(format_type="default"):
    """显示当前时间"""
    now = get_current_time()
    formatted = format_time(now, format_type)
    print(f"[{format_type}] 当前时间: {formatted}")
    return formatted


def run_scheduled(interval_seconds=1, duration_seconds=10, format_type="default"):
    """
    定时运行时间获取
    :param interval_seconds: 刷新间隔（秒）
    :param duration_seconds: 运行时长（秒）
    :param format_type: 时间格式
    """
    print(f"开始定时获取时间，每 {interval_seconds} 秒刷新一次，运行 {duration_seconds} 秒...")
    print("-" * 50)

    start_time = time.time()
    count = 0

    while time.time() - start_time < duration_seconds:
        count += 1
        display_time(format_type)
        time.sleep(interval_seconds)

    print("-" * 50)
    print(f"定时任务完成，共获取 {count} 次时间")


def run_with_schedule(interval_minutes=1, format_type="default"):
    """
    使用schedule库定时运行（需要安装: pip install schedule）
    :param interval_minutes: 刷新间隔（分钟）
    :param format_type: 时间格式
    """
    if not SCHEDULE_AVAILABLE:
        print("错误: 未安装 schedule 库")
        print("请运行: pip install schedule")
        return

    print(f"使用schedule库定时获取时间，每 {interval_minutes} 分钟刷新一次...")
    print("按 Ctrl+C 停止")
    print("-" * 50)

    schedule.every(interval_minutes).minutes.do(display_time, format_type=format_type)

    # 首次立即执行
    display_time(format_type)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # 示例1: 显示不同格式的时间
    print("=" * 50)
    print("不同格式的时间显示:")
    print("=" * 50)
    for fmt in ["default", "date", "time", "full", "iso"]:
        display_time(fmt)

    print("\n")

    # 示例2: 定时获取时间（每隔1秒，运行5秒）
    print("=" * 50)
    print("定时获取时间示例:")
    print("=" * 50)
    run_scheduled(interval_seconds=1, duration_seconds=5, format_type="default")

    # 示例3: 使用schedule库（取消注释以启用）
    # print("\n")
    # print("=" * 50)
    # print("使用schedule库定时获取:")
    # print("=" * 50)
    # run_with_schedule(interval_minutes=1, format_type="full")
