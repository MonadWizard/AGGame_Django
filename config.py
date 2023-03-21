import os

# database config
os.environ['DB_NAME'] = 'aggamedb'
os.environ['DB_USERNAME'] = 'aggame'
os.environ['DB_PASSWORD'] = '?!aggame'
os.environ['DB_HOST'] = '192.168.1.14'
os.environ['DB_PORT'] = '9999'

# secret key
os.environ['SECRET_KEY'] = 'django-insecure-(lup8yovk+3ff!nx2l3ifiptosss75qw2lwppkjn+fd=guii1_'

# email config
os.environ['EMAIL_SERVER_HOST'] = "smtp.gmail.com"
os.environ['EMAIL_SERVER_PORT'] = str(587)
os.environ['EMAIL_SERVER_EMAIL_ADDRESS'] = 'ag.erp@adnanfoundation.com '
os.environ['EMAIL_SERVER_EMAIL_PASSWORD'] = 'jjNBHyt&^$536554'

# cors WhiteList
os.environ['CORS_ORIGIN_WHITELIST'] = str([
    "http://127.0.0.1:8080"
])
