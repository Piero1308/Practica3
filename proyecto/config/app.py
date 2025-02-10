from config.database import *
from config.mail import *

class App:

    def __init__(self,path):
        stmp_server,port,user,password=[
                'sandbox.smtp.mailtrap.io',
                2525,
                'aebdf59080aaf3',
                'b41b1d98df55cd'
                ]
        self.bd:Database=Database(path)        
        self.mail=Mail(stmp_server,port,user,password)