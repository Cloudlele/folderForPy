from http.server import BaseHTTPRequestHandler, HTTPServer
import time, socket
import pypyodbc
import json

hostName = socket.gethostbyname(socket.gethostname())
hostPort = 9000
dataDic = dict()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            connection = pypyodbc.connect(driver='{SQL Server}', server='DESKTOP-7GE22QK\SQLEXPRESS',
                                          database='TravelAgency')
            cursor = connection.cursor()
            SQLQuery = ("""Select Employees.PIP, Employees.Years, Employees.Phone
                    From Employees""")
            cursor.execute(SQLQuery)
            result = cursor.fetchall()
            connection.close()
            name = list()
            year = list()
            phone = list()
            for i in result:
                name.append(str(i[0]))
                year.append(str(i[1]))
                phone.append(str(i[2]))
            dataDic['Pip'] = name
            dataDic['Years'] = year
            dataDic['Phone'] = phone
            print(dataDic)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>%s</p>" % dataDic, "CP1251"))

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode('utf-8')
        print(post_body.strip().split())
        iter = int()
        for id, i in enumerate(post_body.split()):
            if 'name' in i:
                iter = id
            if id == iter+1:
                print(i)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))