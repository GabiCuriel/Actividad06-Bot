import web
import config

db = config.db


def get_all_verano():
    try:
        return db.select('verano')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_verano(id_verano):
    try:
        return db.select('verano', where='id_verano=$id_verano', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_verano(id_verano):
    try:
        return db.delete('verano', where='id_verano=$id_verano', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_verano(consejos):
    try:
        return db.insert('verano',consejos=consejos)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_verano(id_verano,consejos):
    try:
        return db.update('verano',id_verano=id_verano,
consejos=consejos,
                  where='id_verano=$id_verano',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
