import socket

HOST = "127.0.0.1"
PORT = 25565

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Подключено к {addr}")

        while True:
            # Получаем название файла от клиента
            file_name = conn.recv(1024).decode('utf-8').strip()
            if file_name != '':
                print(f"Получено название файла: {file_name}")

                try:
                    # Открываем файл для чтения
                    with open(file_name) as file:
                        # Читаем содержимое файла
                        file_content = file.read() + "\n"

                        # Отправляем содержимое файла обратно клиенту
                        conn.sendall(file_content.encode('utf-8'))

                except FileNotFoundError:
                    # Если файл не найден, отправляем сообщение об ошибке
                    error_message = "404 Not Found\n"
                    conn.sendall(error_message.encode('utf-8'))
