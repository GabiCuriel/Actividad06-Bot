import web
import config

db = config.db


def get_all_otonio():
    try:
        return db.select('otonio')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_otonio(id_otonio):
    try:
        return db.select('otonio', where='id_otonio=$id_otonio', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_otonio(id_otonio):
    try:
        return db.delete('otonio', where='id_otonio=$id_otonio', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_otonio(consejos):
    try:
        return db.insert('otonio',consejos=consejos)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_otonio(id_otonio,consejos):
    try:
        return db.update('otonio',id_otonio=id_otonio,
consejos=consejos,
                  where='id_otonio=$id_otonio',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
