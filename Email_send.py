import smtplib
import pymongo


class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        """logging into Gmail"""
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body, to):
        headers = ["From: " + self.email,"Subject: " + subject,"To: " + to,"",""]
        headers = "\r\n".join(headers)
        self.session.sendmail(self.email,to,headers + "\r\n\r\n" + body)



eid="   " #put your email Id
password="  " # password

"""Initialising the class"""
gm = Gmail(eid,password)
sub="Subject"
msg="   "
"""Sending the message"""
rec="""enter the sender email id"""
#gm.send_message(sub,msg,rec)
jobs=[]
client=pymongo.MongoClient()
db=client.jobs
cursor=db.monsterindia.find({'$text':{'$search':'java'}})
for dat in cursor:
    jobs.append(dat)

msg=str(dat)
gm.send_message(sub,msg,rec)
