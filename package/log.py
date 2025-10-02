import os
import datetime
import sys
import inspect
class Logger():

    def __init__(self):

        log_dir = "./log"
        os.makedirs(log_dir, exist_ok=True)

        name = "./log/"+str(datetime.datetime.today())+".log"

        name = name.replace(":","-")

        self.file = open(name,mode="w")


    def Get_content(self,content):
        time = str(datetime.datetime.today())
        exc_type, exc_value, exc_tb = sys.exc_info()

        # 判断是否处于异常上下文中（即是否有有效的 traceback）
        if exc_tb is not None:
            filename = os.path.basename(exc_tb.tb_frame.f_code.co_filename)  # 仅保留文件名（不含路径）
            lineno = exc_tb.tb_lineno  # 异常发生的行号
            full_message = f"[{time}][{filename}:{lineno}] {content}"

        else:
            frame = inspect.currentframe().f_back.f_back
            filename = os.path.basename(frame.f_code.co_filename)  # 调用者文件名
            lineno = frame.f_lineno  # 调用者行号

            # 注意：这里为了格式统一，也应加上 [ERROR][时间] 前缀（原代码缺失，建议补充）
            full_message = f"[{time}][{filename}:{lineno}] {content}"

        return full_message


    def INFO(self,content):
        full_message = "[INFO]"+self.Get_content(content)
        print(full_message)
        self.file.write(full_message+"\n")
        self.file.flush() # 及时写入文件，避免缓存


    def WARRNING(self,content):
        full_message = "[WARRNING]"+self.Get_content(content)
        print("\033[33m"+full_message+"\033[0m")
        self.file.write(full_message+"\n")

        self.file.flush()# 及时写入文件，避免缓存

    def ERROR(self, content):

        full_message = "[ERROR]"+self.Get_content(content)

        # 将完整日志消息写入日志文件，并换行
        self.file.write(full_message + "\n")
        # 立即刷新缓冲区，确保日志及时写入磁盘（防止程序崩溃时丢失日志）
        self.file.flush()

        # 在控制台输出带红色高亮的日志消息（\033[31m 表示红色，\033[0m 表示重置颜色）
        print("\033[31m" + full_message + "\033[0m")

    def __def__(self):
        self.file.close()
        print("日志系统关闭")