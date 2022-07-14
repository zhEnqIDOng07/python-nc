import subprocess

obj = subprocess.Popen("whoami", shell=True,
                       stdout=subprocess.PIPE, # 标准正确输出
                       stderr=subprocess.PIPE) # 标准错误输出
# 正确输出
res = obj.stdout.read()
print(res)
# 解码
print(res.decode('gbk'))  #subprocess使用当前系统默认编码，得到结果为bytes类型，在windows下需要用gbk解码
# 错误输出
res_err = obj.stderr.read()
# 打印
print(res_err)