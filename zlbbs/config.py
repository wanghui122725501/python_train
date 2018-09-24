
DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'zlbbs'
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %(DB_USERNAME,\
                                                         DB_PASSWORD,\
                                                         DB_HOST,\
                                                         DB_PORT,\
                                                         DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATION = False