import socket
import pickle

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到指定的 IP 地址和端口号
s.bind(('0.0.0.0', 12345))

# 开始监听连接
s.listen()

while True:
    # 接受一个连接
    conn, addr = s.accept()

    # 接收数据
    data = conn.recv(1024)

    # 使用 pickle 反序列化数据
    data = pickle.loads(data)

    # 打印数据
    print(data)

    # 关闭连接
    conn.close()