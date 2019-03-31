import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_primavera, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_primavera) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_primavera, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_primavera) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_primavera, **k):

    @staticmethod
    def POST_DELETE(id_primavera, **k):
    '''

    def GET(self, id_primavera, **k):
        message = None # Error message
        id_primavera = config.check_secure_val(str(id_primavera)) # HMAC id_primavera validate
        result = config.model.get_primavera(int(id_primavera)) # search  id_primavera
        result.id_primavera = config.make_secure_val(str(result.id_primavera)) # apply HMAC for id_primavera
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_primavera, **k):
        form = config.web.input() # get form data
        form['id_primavera'] = config.check_secure_val(str(form['id_primavera'])) # HMAC id_primavera validate
        result = config.model.delete_primavera(form['id_primavera']) # get primavera data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_primavera = config.check_secure_val(str(id_primavera))  # HMAC user validate
            id_primavera = config.check_secure_val(str(id_primavera))  # HMAC user validate
            result = config.model.get_primavera(int(id_primavera)) # get id_primavera data
            result.id_primavera = config.make_secure_val(str(result.id_primavera)) # apply HMAC to id_primavera
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/primavera') # render primavera delete.html 
