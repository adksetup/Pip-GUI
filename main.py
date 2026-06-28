from customtkinter import CTk, CTkEntry, CTkButton
from subprocess import run
from termcolor import cprint
from tkinter import messagebox

class PipGui:
    def __init__(self, window: CTk) -> None:
        self.window = window
        self.window.geometry('350x220')
        self.window.resizable(True, True)
        self.window.wm_title('Pip GUI')
        self.home()
    def home(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.install_btn = CTkButton(self.window, text='安装',
                                     command=self.install_func, corner_radius=20)
        self.install_btn.place(relx=0.5, rely=0.2, anchor='center')
        self.uninstall_btn = CTkButton(self.window, text='移除',
                                       command=self.uninstall_func, corner_radius=20)
        self.uninstall_btn.place(relx=0.5, rely=0.4, anchor='center')
        self.list_btn = CTkButton(self.window, text='显示已安装的包',
                                  command=self.list_func, corner_radius=20)
        self.list_btn.place(relx=0.5, rely=0.6, anchor='center')
        self.show_btn = CTkButton(self.window, text='显示指定包的详细信息',
                                  command=self.show_func, corner_radius=20)
        self.show_btn.place(relx=0.5, rely=0.8, anchor='center')
    def install_func(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            self.pkg_name_entry = CTkEntry(self.window, width=200, corner_radius=5,
                                           placeholder_text='请输入要安装的包名')
            self.pkg_name_entry.place(relx=0.5, rely=0.4, anchor='center')
            install_pkg_btn = CTkButton(self.window, text='安装',
                                        command=self.installer, corner_radius=5)
            install_pkg_btn.place(relx=0.5, rely=0.6, anchor='center')
            back_to_home_btn = CTkButton(self.window, text='返回主界面',
                                         command=self.home, corner_radius=5)
            back_to_home_btn.place(relx=0.1, rely=0.1, anchor='center')
        except Exception as e:
            cprint(f'错误: {e}', 'red')

    def uninstall_func(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            self.pkg_name_entry2 = CTkEntry(self.window, width=200, corner_radius=5,
                                            placeholder_text='请输入要移除的包名')
            self.pkg_name_entry2.place(relx=0.5, rely=0.4, anchor='center')
            uninstall_pkg_btn = CTkButton(self.window, text='移除',
                                        command=self.uninstaller, corner_radius=5)
            uninstall_pkg_btn.place(relx=0.5, rely=0.6, anchor='center')
            back_to_home_btn = CTkButton(self.window, text='返回主界面',
                                         command=self.home, corner_radius=5)
            back_to_home_btn.place(relx=0.1, rely=0.1, anchor='center')
        except Exception as e:
            cprint(f'错误: {e}', 'red')

    def list_func(self):
        try:
            run(f'pip list', shell=True)
        except Exception as e:
            cprint(f'错误: {e}', 'red')

    def show_func(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            self.pkg_name_entry3 = CTkEntry(self.window, width=200, corner_radius=5,
                                            placeholder_text='请输入要获取信息的包名')
            self.pkg_name_entry3.place(relx=0.5, rely=0.4, anchor='center')
            show_pkg_btn = CTkButton(self.window, text='获取对应信息',
                                        command=self.show_n, corner_radius=5)
            show_pkg_btn.place(relx=0.5, rely=0.6, anchor='center')
            back_to_home_btn = CTkButton(self.window, text='返回主界面',
                                         command=self.home, corner_radius=5)
            back_to_home_btn.place(relx=0.1, rely=0.1, anchor='center')
        except Exception as e:
            cprint(f'错误: {e}', 'red')

    def installer(self):
        try:
            run(f'pip install {self.pkg_name_entry.get()}', shell=True)
            messagebox.showinfo("已完成", '已安装1个包')
        except Exception as e:
            cprint(f'错误: {e}', 'red')

    def uninstaller(self):
        try:
            run(f'pip uninstall {self.pkg_name_entry2.get()}', shell=True)
            messagebox.showinfo("已完成", '已移除1个包')
        except Exception as e:
            cprint(f'错误: {e}', 'red')

    def show_n(self):
        try:
            run(f'pip show {self.pkg_name_entry3.get()}', shell=True)
        except Exception as e:
            cprint(f'错误: {e}', 'red')

if __name__ == '__main__':
    app = CTk()
    gui = PipGui(app)
    app.mainloop()
