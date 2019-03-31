import web
import config

db = config.db


def get_all_invierno():
    try:
        return db.select('invierno')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_invierno(id_invierno):
    try:
        return db.select('invierno', where='id_invierno=$id_invierno', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_invierno(id_invierno):
    try:
        return db.delete('invierno', where='id_invierno=$id_invierno', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_invierno(consejos):
    try:
        return db.insert('invierno',consejos=consejos)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_invierno(id_invierno,consejos):
    try:
        return db.update('invierno',id_invierno=id_invierno,
consejos=consejos,
                  where='id_invierno=$id_invierno',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
