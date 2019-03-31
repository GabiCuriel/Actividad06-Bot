import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_invierno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_invierno) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_invierno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_invierno) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_invierno, **k):

    @staticmethod
    def POST_DELETE(id_invierno, **k):
    '''

    def GET(self, id_invierno, **k):
        message = None # Error message
        id_invierno = config.check_secure_val(str(id_invierno)) # HMAC id_invierno validate
        result = config.model.get_invierno(int(id_invierno)) # search  id_invierno
        result.id_invierno = config.make_secure_val(str(result.id_invierno)) # apply HMAC for id_invierno
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_invierno, **k):
        form = config.web.input() # get form data
        form['id_invierno'] = config.check_secure_val(str(form['id_invierno'])) # HMAC id_invierno validate
        result = config.model.delete_invierno(form['id_invierno']) # get invierno data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_invierno = config.check_secure_val(str(id_invierno))  # HMAC user validate
            id_invierno = config.check_secure_val(str(id_invierno))  # HMAC user validate
            result = config.model.get_invierno(int(id_invierno)) # get id_invierno data
            result.id_invierno = config.make_secure_val(str(result.id_invierno)) # apply HMAC to id_invierno
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/invierno') # render invierno delete.html 
