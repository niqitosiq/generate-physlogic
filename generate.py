import random
import MySQLdb
j = 4
iteration = 40
massiv = []
symbolsmass = 'qwertyuiopasdfghjklzxcvbnm1234567890'
def generate(iteration):
	for y in range(iteration):
		dig = ''
		i = 0
		while i<16:
			for k in range(j):
				dig += symbolsmass[random.randint(0,35)]
				i+=1
			if i!=16:
				dig+='-'

		massiv.append(dig)

def appendMysql(extend):
	file = open('password')
	password = file.read()
	db = MySQLdb.connect(host="localhost", user="root", passwd=password, db="physlogic", charset='utf8')
	cursor = db.cursor()
	try: 
		cursor.execute("""INSERT INTO keylogger (keylog, name, location) VALUES (%s, %s, %s)""", (extend, "Unauthorised", "Unauthorised"))
		db.commit()
	except:
		db.rollback()


generate(iteration)
for i in massiv:
	appendMysql(i)