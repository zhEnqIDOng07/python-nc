# # 发起连接
# import socket
# import struct
# # 1.实例化客户端socket 对象
# # 建立同种协议通信
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 2.连接服务端，参数元组
# client.connect(("127.0.0.1",8888))
# # 3.发送数据,参数必须为字节类型
# while 1:
#     msg = input().strip()
#     if not msg:
#         continue
#     if msg.lower() == "q":
#         break
#     msg = msg.encode("u8")
#     client.send(msg)
#
#     # 解决粘包
#     # 1.计算消息长度
#     msg_len = len(msg)
#     # msg_len_byte 固定字节的值
#     msg_len_byte = struct.pack("i",msg_len)
#     # 4.接收消息
#     data = client.recv(1024)
#     data = data.decode('u8')
#     print('服务端回复的消息', data)
# # 5.释放资源
# client.close()

# # 单词通信
# import socket
# MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# MySocket.connect(("192.168.6.250", 227))
#
# MySocket.send(b'hello')
# MySocket.close()

# # 循环通信
# import socket
# MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# MySocket.connect(("192.168.6.250", 227))
#
# while 1:
#     message = input("请输入您要发送的数据>>>").strip()
#     if not message:
#         continue
#     MySocket.send(message.encode())
#     msg = MySocket.recv(1024).decode() # 数据接受
#     print(msg) # 打印输出

# 循环问题 解决粘包问题
# import socket
# import struct
#
#
# def rec_data(Mysock, buf_size=1024):
#     """粘包问题解决"""
#     #先接收命令执行结果的长度
#     struct_bytes = Mysock.recv(4)
#     msg_size = struct.unpack('i', struct_bytes)[0]
#
#     #接收真实数据
#     rec_size = 0
#     data = b''
#     while rec_size < msg_size:
#         data += Mysock.recv(buf_size)
#         rec_size += buf_size
#     return data
#
# def send_data(Mysock, data):
#     """发送数据也解决粘包问题"""
#     if type(data) == str:
#         data = data.encode('u8')
#
#     # 新增发送命令的粘包解决方案
#     # 计算命令长度 , 打包发送
#     command_len = struct.pack('i', len(data))
#     Mysock.send(command_len)
#     # 发送命令
#     Mysock.send(data)
#
# def MySock():
#     client = socket.socket()
#     client.connect(('127.0.0.1', 227))
#     while 1:
#         try:
#             # 新增解包接收命令
#             message = rec_data(client)
#             if message == b'q':
#                 break
#             print(message.decode("utf-8"))
#             message = input(">>>").strip()
#             send_data(client, message)
#         except Exception:
#             break
#     client.close()
#
# if __name__ == "__main__":
#     MySock()

# import socket
# import struct
# import subprocess
#
#
# def exec_cmd(command):
#     """执行命令函数"""
#     obj = subprocess.Popen(command.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                            stdin=subprocess.PIPE)
#     stdout_res = obj.stdout.read() + obj.stderr.read()
#     return stdout_res
#
# def rec_data(Mysock, buf_size=1024):
#     """粘包问题解决"""
#     #先接收命令执行结果的长度
#     struct_bytes = Mysock.recv(4)
#     msg_size = struct.unpack('i', struct_bytes)[0]
#
#     #接收真实数据
#     rec_size = 0
#     data = b''
#     while rec_size < msg_size:
#         data += Mysock.recv(buf_size)
#         rec_size += buf_size
#     return data
#
# def send_data(Mysock, data):
#     """发送数据也解决粘包问题"""
#     if not data:
#         return
#     if type(data) == str:
#         data = data.encode('u8')
#
#     # 新增发送命令的粘包解决方案
#     # 计算命令长度 , 打包发送
#     command_len = struct.pack('i', len(data))
#     Mysock.send(command_len)
#     # 发送命令
#     Mysock.send(data)
#
# def MySock():
#     client = socket.socket()
#     client.connect(('127.0.0.1', 227))
#     while 1:
#         try:
#             # 新增解包接收命令
#             cmd = rec_data(client)
#             if cmd == b'exit()':
#                 break
#             res = exec_cmd(cmd)
#             send_data(client, res)
#         except Exception:
#             break
#     client.close()
#
# if __name__ == "__main__":
#     MySock()

