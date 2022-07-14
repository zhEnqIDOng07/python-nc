# # 监听 等待他人连接
# import socket
# import struct
#
# # 基于网络 ， tcp协议 默认不写也为此
# # 1.实例化socket对象
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 2.绑定ip+port bind() 参数是一个元组
# server.bind(("127.0.0.1", 8888))
# # 3.建立监听
# server.listen(5)
# print("等待连接...")
# # 4.等待连接 conn是一个通信管道, addr 是连接过来的客户端的地址
# conn, addr = server.accept()
# print(f"建立管道{conn}")
# print(f"客户端地址{addr}")
#
# while 1:
#     # 5.接受数据，字节类型，
#     # 解决粘包
#     # 接收4个字节
#     lens = conn.recv(4)
#     # 返回i一个元组
#     all_size = struct.unpack("i",lens)[0]
#     #缓冲区有 固定大小 循环接收
#     recv_size = 0
#     data = b''
#     while recv_size < all_size:
#         data += conn.recv(1024)
#         recv_size += 1024
#
#     data = data.decode("u8")
#     print("客户端发来的消息", data)
#     # 6.服务端回复消息
#     msg = input().strip()
#     if not msg:
#         continue
#     if msg.lower() == 'q':
#         break
#     msg = msg.encode('u8')
#     # 解决粘包
#     msg_len = len(msg)
#     # msg_len_byte 固定字节的值
#     msg_len_byte = struct.pack("i",msg_len)
#     server.send(msg)
# # 7.释放资源
# conn.close()
# server.close()

# # 单次通信
# import socket
#
# MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 初始化socket对象
#
# MySocket.bind(("0.0.0.0", 227)) # 绑定ip + port
# MySocket.listen(10) # 开启监听
#
# print('等待客户端连接...') # 等待客户端建立连接请求
#conn, cli_addr = MySocket.accept()
# print("建立了一个通道:{}".format(conn))
# print("客户端地址：{}".format(cli_addr))
#
# message = conn.recv(1024) # 最大接收的数据量为1024个字节,收到的是bytes类型
#
# print(f"接收到的数据是：{message.decode()}")
#
# conn.close() # 关闭管道连接
# MySocket.close() # 释放socket

# # 循环通信
# import socket
#
# Mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# Mysocket.bind(('0.0.0.0',227))
# Mysocket.listen(10)
#
# print('等待客户端连接...')
# conn, cli_addr = Mysocket.accept()
# while 1:
#     try:
#         message = conn.recv(1024).decode()
#
#         if not message:
#             break
#         print(f"接收到的数据：{message}")
#         conn.send(message.upper().encode())
#     except Exception:
#         break
#
# conn.close()
# Mysocket.close()

# # 循环问题 解决粘包问题
# import socket
# import struct
#
# def rec_data(Mysock, buf_size=1024):
#     """解决粘包"""
#     # 先接受命令执行结果的长度
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
#     # 新增发送命令的粘包解决方案
#     # 计算命令长度 , 打包发送
#     command_len = struct.pack('i', len(data))
#     Mysock.send(command_len)
#     # 发送命令
#     Mysock.send(data)
#
# def MySock():
#     server = socket.socket()
#     server.bind(('0.0.0.0', 227))
#     server.listen(2)
#     print("等待连接...")
#     conn, cli_addr = server.accept()
#     print(f"新建一个链接,链接管道为{conn}")
#     print(f"当前客户端的地址为{cli_addr}")
#     while 1:
#         try:
#             data = input(">>>").strip()
#             if not data:
#                 continue
#             send_data(conn, data)
#             if data =="exit()":
#                 break
#             # 接收客户端发来的内容
#             data = rec_data(conn)
#             print(data.decode('u8'))
#         except Exception:
#             break
#     conn.close()
#     server.close()
#
# if __name__ == "__main__":
#     MySock()

# import socket
# import struct
#
# def rec_data(Mysock, buf_size=1024):
#     """解决粘包"""
#     # 先接受命令执行结果的长度
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
#     # 新增发送命令的粘包解决方案
#     # 计算命令长度 , 打包发送
#     command_len = struct.pack('i', len(data))
#     Mysock.send(command_len)
#     # 发送命令
#     Mysock.send(data)
#
# def MySock():
#     server = socket.socket()
#     server.bind(('0.0.0.0', 227))
#     server.listen(2)
#     print("等待连接...")
#     conn, cli_addr = server.accept()
#     print(f"新建一个链接,链接管道为{conn}")
#     print(f"当前客户端的地址为{cli_addr}")
#     while 1:
#
#         try:
#             cmd = input(f">>>").strip()
#             if not cmd:
#                 continue
#             if cmd =="exit()":
#                 send_data(conn, cmd)
#                 break
#             # 接收客户端发来的内容
#             send_data(conn, cmd)
#             data = rec_data(conn)
#             print(data.decode('gbk').strip())
#         except Exception:
#             break
#     conn.close()
#     server.close()
#
# if __name__ == "__main__":
#     MySock()

