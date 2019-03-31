import web
import config

db = config.db


def get_all_primavera():
    try:
        return db.select('primavera')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_primavera(id_primavera):
    try:
        return db.select('primavera', where='id_primavera=$id_primavera', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_primavera(id_primavera):
    try:
        return db.delete('primavera', where='id_primavera=$id_primavera', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_primavera(consejos):
    try:
        return db.insert('primavera',consejos=consejos)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_primavera(id_primavera,consejos):
    try:
        return db.update('primavera',id_primavera=id_primavera,
consejos=consejos,
                  where='id_primavera=$id_primavera',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
