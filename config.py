import os

# database config
os.environ['DB_NAME'] = 'aggamedb'
os.environ['DB_USERNAME'] = 'aggame'
os.environ['DB_PASSWORD'] = '?!aggame'

# os.environ['DB_HOST'] = '192.168.1.14'
os.environ['DB_HOST'] = '103.19.131.206'
os.environ['DB_PORT'] = '9999'
# os.environ['DB_HOST'] = 'localhost'
# os.environ['DB_PORT'] = '5432'

# secret key
os.environ['SECRET_KEY'] = 'django-insecure-(lup8yovk+3ff!nx2l3ifiptosss75qw2lwppkjn+fd=guii1_'

# email config
os.environ['EMAIL_SERVER_HOST'] = "smtp.gmail.com"
os.environ['EMAIL_SERVER_PORT'] = str(587)
os.environ['EMAIL_SERVER_EMAIL_ADDRESS'] = 'ag.erp@adnanfoundation.com '
os.environ['EMAIL_SERVER_EMAIL_PASSWORD'] = 'jjNBHyt&^$536554'

# cors WhiteList
# os.environ['CORS_ORIGIN_WHITELIST'] = str([
#     "http://127.0.0.1:8005",
#     "http://192.168.1.22:8005",
#     "http://192.168.1.11:8005",
#     "http://192.168.1.17:8005",
# ])



CORS_ORIGIN_ALLOW_ALL = True




INSTALLED_APPS =  ['django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auth_user_app',
    'team_app',
    'game_app',
    'tournament_app',
    'home_app',
    'dashboard_app','channels',
    'daphne',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',]
