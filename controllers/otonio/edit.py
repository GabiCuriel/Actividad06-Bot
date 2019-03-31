import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_otonio, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_otonio) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_otonio, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_otonio) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_otonio, **k):

    @staticmethod
    def POST_EDIT(id_otonio, **k):
        
    '''

    def GET(self, id_otonio, **k):
        message = None # Error message
        id_otonio = config.check_secure_val(str(id_otonio)) # HMAC id_otonio validate
        result = config.model.get_otonio(int(id_otonio)) # search for the id_otonio
        result.id_otonio = config.make_secure_val(str(result.id_otonio)) # apply HMAC for id_otonio
        return config.render.edit(result, message) # render otonio edit.html

    def POST(self, id_otonio, **k):
        form = config.web.input()  # get form data
        form['id_otonio'] = config.check_secure_val(str(form['id_otonio'])) # HMAC id_otonio validate
        # edit user with new data
        result = config.model.edit_otonio(
            form['id_otonio'],form['consejos'],
        )
        if result == None: # Error on udpate data
            id_otonio = config.check_secure_val(str(id_otonio)) # validate HMAC id_otonio
            result = config.model.get_otonio(int(id_otonio)) # search for id_otonio data
            result.id_otonio = config.make_secure_val(str(result.id_otonio)) # apply HMAC to id_otonio
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/otonio') # render otonio index.html
