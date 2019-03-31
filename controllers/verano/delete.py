import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_verano, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_verano) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_verano, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_verano) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_verano, **k):

    @staticmethod
    def POST_DELETE(id_verano, **k):
    '''

    def GET(self, id_verano, **k):
        message = None # Error message
        id_verano = config.check_secure_val(str(id_verano)) # HMAC id_verano validate
        result = config.model.get_verano(int(id_verano)) # search  id_verano
        result.id_verano = config.make_secure_val(str(result.id_verano)) # apply HMAC for id_verano
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_verano, **k):
        form = config.web.input() # get form data
        form['id_verano'] = config.check_secure_val(str(form['id_verano'])) # HMAC id_verano validate
        result = config.model.delete_verano(form['id_verano']) # get verano data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_verano = config.check_secure_val(str(id_verano))  # HMAC user validate
            id_verano = config.check_secure_val(str(id_verano))  # HMAC user validate
            result = config.model.get_verano(int(id_verano)) # get id_verano data
            result.id_verano = config.make_secure_val(str(result.id_verano)) # apply HMAC to id_verano
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/verano') # render verano delete.html 
