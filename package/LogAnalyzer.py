import os
import pandas as pd


class LogAnalyzer():

    def __init__(self,log_path):
        self.log_path = log_path



    def detect(self):
        #errors参数当解码出错时如何处理。
        file = open(self.log_path,mode="r",encoding="utf-8",errors="ignore")

        names = []
        values = []

        for line in file.readlines():
            
            keywords = ["warning","error"]

            if any(k in line.lower() for k in keywords):
                continue

            line = line.strip()#去掉空行尾的换行符

            if not line:
                continue

            str = line.split(":",1)

            if len(str)!=2:
                continue   
            
            name = str[0].strip()
            value = str[1].strip()

            names.append(name)
            values.append(value)

        
        self.df = pd.DataFrame(
            {
                "name":names,
                "value":values
            }
        )
