
class Config():
    DEBUG=True
    SECRET_KEY= 'khkhkhkhhkhkhkhkhkhkh12'

class Development(Config):
#database://user:password@host:port/databasename

    SQLALCHEMY_DATABASE_URI='postgresql://postgres:wagatagati12!@127.0.0.1:5432/inventory_management_system'


class Production(Config):
    SQLALCHEMY_DATABASE_URI='postgres://gilkahqjevhnwe:16cf303eb194d57d2ed6514153ce474dca171a7914266a5b09c4df9d520e70ed@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d6sa56nv73mkjh'
    SECRET_KEY='mnmnmnmnmnmnmnmnmnmnm12'




