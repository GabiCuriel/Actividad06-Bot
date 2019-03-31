import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_otonio, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_otonio) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_otonio, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_otonio) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_otonio, **k):

    @staticmethod
    def POST_DELETE(id_otonio, **k):
    '''

    def GET(self, id_otonio, **k):
        message = None # Error message
        id_otonio = config.check_secure_val(str(id_otonio)) # HMAC id_otonio validate
        result = config.model.get_otonio(int(id_otonio)) # search  id_otonio
        result.id_otonio = config.make_secure_val(str(result.id_otonio)) # apply HMAC for id_otonio
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_otonio, **k):
        form = config.web.input() # get form data
        form['id_otonio'] = config.check_secure_val(str(form['id_otonio'])) # HMAC id_otonio validate
        result = config.model.delete_otonio(form['id_otonio']) # get otonio data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_otonio = config.check_secure_val(str(id_otonio))  # HMAC user validate
            id_otonio = config.check_secure_val(str(id_otonio))  # HMAC user validate
            result = config.model.get_otonio(int(id_otonio)) # get id_otonio data
            result.id_otonio = config.make_secure_val(str(result.id_otonio)) # apply HMAC to id_otonio
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/otonio') # render otonio delete.html 
