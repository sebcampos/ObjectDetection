from bluetooth import *
import socket


class BluetoothClient:
	hotsMacAddress = 'E4:5F:01:AE:44:CA'
	port 



class BluetoothClientBlueZ:
	
	server_sock = BluetoothSocket( RFCOMM )
	server_sock.bind(("", PORT_ANY))
	server_sock.listen(1)
	port = server_sock.getsockname()[1]
	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
	
	advertise_service(
		server_sock,
		"TestServer",
		service_id = uuid,
		service_classes = [ uuid, SERIAL_PORT_CLASS ],
		profiles = [ SERIAL_PORT_PROFILE ]
	)
	
	print(f"waiting for connection on port {port}")
	
	
	client_sock, client_info = server_sock.accept()
	print(f"Accepted connection from {client_info}")
	
	try:
		while True:
			data = client_sock.recv(1024)
			if len(data) == 0:
				break
			print(f"recieved [{data}]")
	except IOError:
		pass
	
	print("disconnected")
	
	client_sock.close()
	server_sock.close()
	print("End")
	
