"""
时间显示程序 - GUI版本
功能：显示当前时间，支持多种格式和自动刷新
"""

import datetime
import tkinter as tk
from tkinter import ttk


class TimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("时间显示程序")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # 自动刷新状态
        self.auto_refresh = False
        self.refresh_interval = 1000  # 毫秒

        self.setup_ui()
        self.update_time()

    def setup_ui(self):
        """设置界面"""
        # 标题
        title_label = ttk.Label(
            self.root,
            text="⏰ 当前时间",
            font=("Microsoft YaHei", 18, "bold")
        )
        title_label.pack(pady=20)

        # 主时间显示框
        self.time_frame = ttk.Frame(self.root)
        self.time_frame.pack(fill=tk.X, padx=20)

        # 时间显示标签
        self.time_label = ttk.Label(
            self.time_frame,
            text="",
            font=("Consolas", 24, "bold"),
            foreground="#2196F3"
        )
        self.time_label.pack(pady=10)

        # 日期显示标签
        self.date_label = ttk.Label(
            self.time_frame,
            text="",
            font=("Microsoft YaHei", 14),
            foreground="#666666"
        )
        self.date_label.pack(pady=5)

        # 分隔线
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=20, pady=15)

        # 格式选择区域
        format_frame = ttk.LabelFrame(self.root, text="时间格式", padding=10)
        format_frame.pack(fill=tk.X, padx=20, pady=5)

        self.format_var = tk.StringVar(value="default")

        formats = [
            ("默认格式", "default"),
            ("日期时间", "full"),
            ("仅时间", "time"),
            ("ISO格式", "iso")
        ]

        for text, value in formats:
            rb = ttk.Radiobutton(
                format_frame,
                text=text,
                value=value,
                variable=self.format_var,
                command=self.update_time
            )
            rb.pack(side=tk.LEFT, padx=10)

        # 控制区域
        control_frame = ttk.LabelFrame(self.root, text="控制", padding=10)
        control_frame.pack(fill=tk.X, padx=20, pady=10)

        # 自动刷新开关
        self.auto_var = tk.BooleanVar(value=False)
        auto_check = ttk.Checkbutton(
            control_frame,
            text="自动刷新",
            variable=self.auto_var,
            command=self.toggle_auto_refresh
        )
        auto_check.pack(side=tk.LEFT, padx=10)

        # 刷新间隔选择
        ttk.Label(control_frame, text="刷新间隔:").pack(side=tk.LEFT, padx=5)
        self.interval_var = tk.StringVar(value="1秒")
        interval_combo = ttk.Combobox(
            control_frame,
            textvariable=self.interval_var,
            values=["0.5秒", "1秒", "2秒", "5秒"],
            width=8,
            state="readonly"
        )
        interval_combo.pack(side=tk.LEFT, padx=5)
        interval_combo.bind("<<ComboboxSelected>>", self.change_interval)

        # 手动刷新按钮
        refresh_btn = ttk.Button(
            control_frame,
            text="刷新",
            command=self.update_time
        )
        refresh_btn.pack(side=tk.RIGHT, padx=10)

    def get_current_time(self):
        """获取当前时间"""
        return datetime.datetime.now()

    def format_time(self, dt, format_type="default"):
        """格式化时间"""
        formats = {
            "default": "%H:%M:%S",
            "full": "%Y-%m-%d %H:%M:%S",
            "time": "%H:%M:%S",
            "iso": "%H:%M:%S"
        }
        return dt.strftime(formats.get(format_type, formats["default"]))

    def format_date(self, dt):
        """格式化日期"""
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        weekday = weekdays[dt.weekday()]
        return f"{dt.year}年{dt.month}月{dt.day}日 {weekday}"

    def update_time(self):
        """更新时间显示"""
        now = self.get_current_time()
        format_type = self.format_var.get()

        self.time_label.config(text=self.format_time(now, format_type))
        self.date_label.config(text=self.format_date(now))

        # 如果开启自动刷新，安排下一次更新
        if self.auto_refresh:
            self.root.after(self.refresh_interval, self.update_time)

    def toggle_auto_refresh(self):
        """切换自动刷新状态"""
        self.auto_refresh = self.auto_var.get()
        if self.auto_refresh:
            self.update_time()

    def change_interval(self, event=None):
        """改变刷新间隔"""
        intervals = {
            "0.5秒": 500,
            "1秒": 1000,
            "2秒": 2000,
            "5秒": 5000
        }
        self.refresh_interval = intervals.get(self.interval_var.get(), 1000)


def main():
    root = tk.Tk()
    app = TimeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
