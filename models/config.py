import web

db_host = 'localhost'
db_name = 'demo_bot'
db_user = 'utec'
db_pw = 'utec.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )