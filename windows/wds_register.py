import queue
import tkinter
import threading
from tkinter import ttk
from tkinter import messagebox


def double_handler(event):
    """处理双击事件"""
    widget = str(event.widget).split(".!")[2]
    if widget == "listbox":
        RegisterGui.queue.put("显示寄存器列表")
        pass
    elif widget == "treeview":
        RegisterGui.queue.put("显示bit控制框")
        pass
    pass


def button_handler(button):
    """处理按钮对应的功能"""
    RegisterGui.queue.put(button["text"])
    pass


class RegisterGui:
    """寄存器类"""
    queue = queue.Queue()

    def __init__(self, root):
        """初始化寄存器界面"""
        self.title_lb = tkinter.Label(root, text="标准寄存器读写", font=("楷体", 20))
        self.title_lb.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.05)

        # 文件加载框
        self.file_sel_fm = tkinter.LabelFrame(root, text="文件加载区", font=("楷体", 14))
        self.file_sel_fm.place(relx=0.005, rely=0.05, relwidth=0.245, relheight=0.945)
        # 文件列表滚动条
        self.file_lbx_sb = tkinter.Scrollbar(self.file_sel_fm)
        self.file_lbx_sb.place(relx=0.94, rely=0.005, relwidth=0.05, relheight=0.92)
        # 文件列表
        self.file_lbx = tkinter.Listbox(self.file_sel_fm, font=("Times New Roman", 14))
        self.file_lbx.config(yscrollcommand=self.file_lbx_sb.set)
        self.file_lbx.place(relx=0.01, rely=0.005, relwidth=0.93, relheight=0.92)
        self.file_lbx.bind("<Double-1>", double_handler)
        self.file_lbx_sb.config(command=self.file_lbx.yview)
        # 文件加载按钮
        self.file_load_bt = tkinter.Button(self.file_sel_fm, text="文件加载", font=("楷体", 14))
        self.file_load_bt.place(relx=0.3, rely=0.94, relwidth=0.4, relheight=0.05)
        self.file_load_bt.config(command=lambda var=self.file_load_bt: button_handler(var))

        # 寄存器显示框
        self.file_show_fm = tkinter.LabelFrame(root, text="寄存器显示区", font=("楷体", 14))
        self.file_show_fm.place(relx=0.255, rely=0.05, relwidth=0.74, relheight=0.945)
        # 树状表格参数配置
        ttk.Style().configure("Treeview", rowheight=35)
        ttk.Style().configure("Treeview.Heading", foreground="red", font=("楷体", 18))
        # 树状表格滚动条
        self.tree_sb = tkinter.Scrollbar(self.file_show_fm)
        self.tree_sb.place(relx=0.83, rely=0.005, relwidth=0.02, relheight=0.99)
        # 树状表格
        self.tree = ttk.Treeview(self.file_show_fm, columns=("address", "value"))
        self.tree.config(yscrollcommand=self.tree_sb.set)
        self.tree.place(relx=0.005, rely=0.005, relwidth=0.825, relheight=0.99)
        self.tree_sb.config(command=self.tree.yview)
        self.tree.heading("#0", text="名称")
        self.tree.heading("address", text="地址")
        self.tree.heading("value", text="值")
        self.tree.column("address", anchor="center")
        self.tree.column("value", anchor="center")
        self.tree.tag_configure("odd", font=("Times New Roman", 16), background="green")
        self.tree.tag_configure("even", font=("Times New Roman", 16), background="blue")
        self.tree.bind("<Double-1>", double_handler)
        # 添加寄存器按钮
        self.add_reg_bt = tkinter.Button(self.file_show_fm, text="添   加", font=("楷体", 14))
        self.add_reg_bt.place(relx=0.86, rely=0.04, relwidth=0.13, relheight=0.05)
        self.add_reg_bt.config(command=lambda var=self.add_reg_bt: button_handler(var))
        # 删除选中寄存器按钮
        self.del_reg_bt = tkinter.Button(self.file_show_fm, text="删除选中", font=("楷体", 14))
        self.del_reg_bt.place(relx=0.86, rely=0.14, relwidth=0.13, relheight=0.05)
        self.del_reg_bt.config(command=lambda var=self.del_reg_bt: button_handler(var))
        # 删除全部寄存器按钮
        self.del_all_bt = tkinter.Button(self.file_show_fm, text="删除全部", font=("楷体", 14))
        self.del_all_bt.place(relx=0.86, rely=0.24, relwidth=0.13, relheight=0.05)
        self.del_all_bt.config(command=lambda var=self.del_all_bt: button_handler(var))
        # 保存寄存器按钮
        self.sv_reg_bt = tkinter.Button(self.file_show_fm, text="保存全部", font=("楷体", 14))
        self.sv_reg_bt.place(relx=0.86, rely=0.34, relwidth=0.13, relheight=0.05)
        self.sv_reg_bt.config(command=lambda var=self.sv_reg_bt: button_handler(var))
        # 读取选中按钮
        self.rd_sel_bt = tkinter.Button(self.file_show_fm, text="读取选中", font=("楷体", 14))
        self.rd_sel_bt.place(relx=0.86, rely=0.54, relwidth=0.13, relheight=0.05)
        self.rd_sel_bt.config(command=lambda var=self.rd_sel_bt: button_handler(var))
        # 读取全部按钮
        self.rd_all_bt = tkinter.Button(self.file_show_fm, text="读取全部", font=("楷体", 14))
        self.rd_all_bt.place(relx=0.86, rely=0.64, relwidth=0.13, relheight=0.05)
        self.rd_all_bt.config(command=lambda var=self.rd_all_bt: button_handler(var))
        # 生成头文件
        self.crt_h_bt = tkinter.Button(self.file_show_fm, text="生成头文件", font=("楷体", 14))
        self.crt_h_bt.place(relx=0.86, rely=0.84, relwidth=0.13, relheight=0.05)
        self.crt_h_bt.config(command=lambda var=self.crt_h_bt: button_handler(var))

        # 创建任务处理线程
        threading.Thread(target=self.task_handler, daemon=True).start()

        # adds = [x for x in range(0xC0012000, 0xC0013000, 4)]
        # adds_id = []
        # sons_id = []
        # gsons_id = []
        #
        # self.tree.tag_configure("style", font=("Times New Roman", 16))
        # for address in adds:
        #     idx = self.tree.insert("", index="end", text="Ana", values=("0x%X" % address, "0x%X"%0x3), tags="style")
        #     adds_id.append(idx)
        #
        # for adds in adds_id:
        #     son = self.tree.insert(adds, index="end", text="[31:0]gain[31:0]", values=("", "0x%X"%0x3), tags="style")
        #     sons_id.append(son)
        #
        #     gson = self.tree.insert(son, index="end", text="[0]", values=("", 1), tags="style")
        #     gsons_id.append(gson)

        pass

    def task_handler(self):
        """处理消息内容"""
        while True:
            msg = RegisterGui.queue.get()
            if msg == "文件加载":
                pass
            if msg == "添   加":
                AddRegister(self.tree, self.file_show_fm)
                pass
            if msg == "删除选中":
                sel_tup = self.tree.selection()
                for each in sel_tup:
                    self.tree.delete(each)
                pass
            if msg == "删除全部":
                pass
            if msg == "保存全部":
                pass
            if msg == "读取选中":
                pass
            if msg == "读取全部":
                pass
            if msg == "生成头文件":
                pass
            if msg == "显示寄存器列表":
                pass
            if msg == "显示bit控制框":
                pass
            pass
        pass
    pass


class AddRegister:
    """添加寄存器"""
    def __init__(self, tree, father):
        """初始化添加界面"""
        self.tree = tree

        self.tl = tkinter.Toplevel(father)
        self.tl.title("添加寄存器")
        self.tl.geometry("400x150")
        self.tl.resizable(0, 0)
        self.tl.attributes("-topmost", 1)
        # 名称标签
        self.reg_name_lb = tkinter.Label(self.tl, text="名  称", font=("楷体", 14))
        self.reg_name_lb.place(relx=0.0, rely=0.05, relwidth=0.3, relheight=0.2)
        # 名称输入框
        self.reg_name_nt = tkinter.Entry(self.tl, font=("Times New Roman", 18))
        self.reg_name_nt.place(relx=0.35, rely=0.06, relwidth=0.6, relheight=0.18)
        # 地址标签
        self.reg_addr_lb = tkinter.Label(self.tl, text="地  址", font=("楷体", 14))
        self.reg_addr_lb.place(relx=0.0, rely=0.3, relwidth=0.3, relheight=0.2)
        # 地址输入框
        self.reg_addr_nt = tkinter.Entry(self.tl, font=("Times New Roman", 18))
        self.reg_addr_nt.place(relx=0.35, rely=0.31, relwidth=0.6, relheight=0.18)
        # 确定按钮
        self.reg_ok_bt = tkinter.Button(self.tl, text="确定", font=("楷体", 14))
        self.reg_ok_bt.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.25)
        self.reg_ok_bt.config(command=lambda var=self.reg_ok_bt: self.button_handler(var))
        # 取消按钮
        self.reg_no_bt = tkinter.Button(self.tl, text="取消", font=("楷体", 14))
        self.reg_no_bt.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.25)
        self.reg_no_bt.config(command=lambda var=self.reg_no_bt: self.button_handler(var))

    def button_handler(self, button):
        """实现按钮对应的功能"""
        if button["text"] == "确定":
            if not self.reg_name_nt.get():
                messagebox.showwarning("添加窗口", "未输入寄存器名称")
                return
            if not self.reg_addr_nt.get():
                messagebox.showwarning("添加窗口", "未输入寄存器地址")
                return
            # 检查地址有效性
            try:
                int(self.reg_addr_nt.get(), 16)
            except ValueError:
                messagebox.showwarning("添加窗口", "输入的寄存器地址不合法, 请重新输入")
                return
            if int(self.reg_addr_nt.get(), 16) % 4 != 0:
                messagebox.showwarning("添加窗口", "输入的寄存器地址未对齐, 请重新输入")
                return

            # 获取值
            name = self.reg_name_nt.get()
            addr = int(self.reg_addr_nt.get(), 16)
            # 插入树状列表
            self.tree.insert("", index="end", text=name, values=("0x%08X" % addr,), tags="odd")
            self.reg_name_nt.delete(0, "end")
            self.reg_addr_nt.delete(0, "end")
            pass
        elif button["text"] == "取消":
            self.tl.destroy()
            pass
        pass
    pass
