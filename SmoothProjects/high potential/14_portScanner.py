# Third party interference
# import socket

# target = "www.carouselforge.app"
# ip = socket.gethostbyname(target)

# # Scan ports from 1 to 1024
# for port in range(1, 1025):
#     s = socket.socket()
#     s.settimeout(0.5)  # Quick timeout so the script doesn't hang forever
    
#     # connect_ex returns 0 if the connection was successful
#     if s.connect_ex((ip, port)) == 0:
#         print(f"Port {port} OPEN")
        
#     s.close()


# Use in own computer
import socket

target = "127.0.0.1"  # Your own computer

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        try:
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} OPEN")

        finally:
            s.close()

except Exception as e:
    print("Error:", e)