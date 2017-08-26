from html.parser import HTMLParser
from string import punctuation
import pymysql.cursors
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tg = ''
		self.cunter=0
		self.phone=''
		self.dtime=''
		self.timedur=''
	def handle_starttag(self, tag, attrs):
		self.tg = tag
		#print("Encountered a start tag:", tag)
	
	def handle_endtag(self, tag):
		if tag == 'tr':
			y=0
			#print("Encountered an end tag :", tag)
	
	def handle_data(self, data):
		if(self.tg == 'td'):
			self.cunter= self.cunter+1;
			self.tg= ' '
			#exec(open('C:/Users/Sophomore/Dropbox/APythonCode/sql.py').read())
			#exec(open('C:/Users/Sophomore/Dropbox/APythonCode/parse_html2.py').read())
			data=data.strip()
			print("Encountered :", data)
			if(self.cunter == 1):
				self.dtime=data
			elif(self.cunter == 2):
				self.phone=data
			elif(self.cunter == 3):
				self.timedur=data
			# Connect to the database
			if(self.cunter == 3):
				self.cunter=0;
				connection = pymysql.connect(host='localhost',
				user='didar',
				password='Sophomore@99',
				db='bookmanage',
				charset='utf8mb4',
				cursorclass=pymysql.cursors.DictCursor)
				try:
					with connection.cursor() as cursor:
						# Create a new record
						#x='Tuk'
						sql = '''INSERT INTO `phone_number` (`phone`, `dtime`, `timedur`) VALUES ('{}', '{}l', '{}')'''.format(self.phone,self.dtime,self.timedur)
						#sql = "INSERT INTO `books` (`name`, `owner`, `purchase`) VALUES ('Tukunjil', 'Zafar Iqbal', STR_TO_DATE('17/07/2013 18:33:55', '%d/%m/%Y %H:%i:%s'))"
						cursor.execute(sql)
						# connection is not autocommit by default. So you must commit to save
						# your changes.
						connection.commit()
					
					with connection.cursor() as cursor:
						# Read a single record
						sql = "SELECT * FROM `books`"
						cursor.execute(sql)
						results = cursor.fetchall()
						for row in results:
							name = row['name']
							owner = row['owner']
							purchase = row['purchase']
							
						  # Now print fetched result
							#print ("name = %s,owner = %s,purchase = %s" % (name, owner, purchase))
						
				finally:
					connection.close()
			
			return

parser = MyHTMLParser()
"""
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
"""
parser.feed(open('C:/Users/Sophomore/Dropbox/APythonCode/test5.html').read())