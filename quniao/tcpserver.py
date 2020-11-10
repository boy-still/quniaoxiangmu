from socket import *
import sqlite3
import time
host = ''
port = 9000
DB_Name = 'quniaodata.db'
server_socket = socket(AF_INET, SOCK_STREAM)
server_addr = (host, port)
server_socket.bind(server_addr)
server_socket.listen(5)
def tcpserver():
    while (True):
            print('waiting for connect...')
            try:
                    client_socket,client_addr = server_socket.accept()
                    client_socket.settimeout(5)
                    print('a client connect from:', client_addr)
                    client_socket.send('Hello.client!'.encode())
                    data = client_socket.recv(1024)
                    print('recv data is', data.decode())
                    if 'quit' in data.decode():
                            client_socket.close()
                            #server_socket.close()
                    if 'bird' in data.decode():
                            conn = sqlite3.connect(DB_Name)
                            print('连接数据库%s成功' % (DB_Name))
                            try:
                                    timedata = ''
                                    cursor = conn.cursor()
                                    localtime = time.localtime(time.time())
                                    for i in range(0,4):
                                        if localtime[i]<10:
                                                timestr ='0'+str(localtime[i])
                                        else:
                                                timestr =str(localtime[i])
                                        timedata += timestr
                                    SQL = "INSERT INTO INDEX_QUNIAO(TIME) VALUES('%s');"%timedata
                                    cursor.execute(SQL)
                                    conn.commit()
                                    print('插入数据到表STUDENT成功')
                            except Exception as e:
                                    print(e)
                                    # 回滚
                                    conn.rollback()
                                    print('插入数据到表QUNIAODATA失败')
                            finally:
                                    # 关闭数据库
                                    conn.close()
                                    client_socket.close()
                                    #server_socket.close()

            except Exception as e:
                print(e)
if __name__ == '__main__':
    tcpserver()