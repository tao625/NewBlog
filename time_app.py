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
        self.root.geometry("500x420")
        self.root.resizable(False, False)

        self.auto_refresh = False
        self.refresh_interval = 1000

        self.setup_ui()
        self.update_time()

    def setup_ui(self):
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Microsoft YaHei", 22, "bold"), foreground="#1E88E5")
        style.configure("Time.TLabel", font=("Consolas", 36, "bold"), foreground="#2196F3")
        style.configure("Date.TLabel", font=("Microsoft YaHei", 14), foreground="#757575")
        
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="⏰ 当前时间", style="Title.TLabel")
        title_label.pack(pady=(0, 15))

        time_container = ttk.Frame(main_frame, borderwidth=2, relief="groove", padding=15)
        time_container.pack(fill=tk.X, pady=(0, 15))

        self.time_label = ttk.Label(time_container, text="", style="Time.TLabel", anchor="center")
        self.time_label.pack()

        self.date_label = ttk.Label(time_container, text="", style="Date.TLabel", anchor="center")
        self.date_label.pack(pady=(8, 0))

        format_container = ttk.LabelFrame(main_frame, text="时间格式", padding=12)
        format_container.pack(fill=tk.X, pady=(0, 10))

        self.format_var = tk.StringVar(value="default")

        formats = [
            ("默认格式", "default"),
            ("日期时间", "full"),
            ("仅时间", "time"),
            ("ISO格式", "iso")
        ]

        format_frame = ttk.Frame(format_container)
        format_frame.pack()
        for text, value in formats:
            rb = ttk.Radiobutton(
                format_frame,
                text=text,
                value=value,
                variable=self.format_var,
                command=self.update_time,
                padding=5
            )
            rb.pack(side=tk.LEFT, padx=8)

        control_container = ttk.LabelFrame(main_frame, text="控制", padding=12)
        control_container.pack(fill=tk.X)

        left_frame = ttk.Frame(control_container)
        left_frame.pack(side=tk.LEFT)

        self.auto_var = tk.BooleanVar(value=False)
        auto_check = ttk.Checkbutton(
            left_frame,
            text="自动刷新",
            variable=self.auto_var,
            command=self.toggle_auto_refresh,
            padding=5
        )
        auto_check.pack(side=tk.TOP, anchor="w", pady=2)

        interval_frame = ttk.Frame(left_frame)
        interval_frame.pack(side=tk.TOP, anchor="w", pady=2)

        ttk.Label(interval_frame, text="刷新间隔:").pack(side=tk.LEFT, padx=(0, 5))
        self.interval_var = tk.StringVar(value="1秒")
        interval_combo = ttk.Combobox(
            interval_frame,
            textvariable=self.interval_var,
            values=["0.5秒", "1秒", "2秒", "5秒"],
            width=6,
            state="readonly"
        )
        interval_combo.pack(side=tk.LEFT)
        interval_combo.bind("<<ComboboxSelected>>", self.change_interval)

        right_frame = ttk.Frame(control_container)
        right_frame.pack(side=tk.RIGHT)

        refresh_btn = ttk.Button(
            right_frame,
            text="🔄 刷新",
            command=self.update_time,
            width=10
        )
        refresh_btn.pack()

    def get_current_time(self):
        return datetime.datetime.now()

    def format_time(self, dt, format_type="default"):
        formats = {
            "default": "%H:%M:%S",
            "full": "%Y-%m-%d %H:%M:%S",
            "time": "%H:%M:%S",
            "iso": "%H:%M:%S"
        }
        return dt.strftime(formats.get(format_type, formats["default"]))

    def format_date(self, dt):
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        weekday = weekdays[dt.weekday()]
        return f"{dt.year}年{dt.month}月{dt.day}日 {weekday}"

    def update_time(self):
        now = self.get_current_time()
        format_type = self.format_var.get()

        self.time_label.config(text=self.format_time(now, format_type))
        self.date_label.config(text=self.format_date(now))

        if self.auto_refresh:
            self.root.after(self.refresh_interval, self.update_time)

    def toggle_auto_refresh(self):
        self.auto_refresh = self.auto_var.get()
        if self.auto_refresh:
            self.update_time()

    def change_interval(self, event=None):
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
