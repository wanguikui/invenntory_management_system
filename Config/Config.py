
class Config():
    DEBUG=True
    SECRET_KEY= 'khkhkhkhhkhkhkhkhkhkh12'

class Development(Config):
#database://user:password@host:port/databasename

    SQLALCHEMY_DATABASE_URI='postgresql://postgres:wagatagati12!@127.0.0.1:5432/inventory_management_system'


class Production(Config):
    pass



