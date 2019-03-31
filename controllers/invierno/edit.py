import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_invierno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_invierno) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_invierno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_invierno) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_invierno, **k):

    @staticmethod
    def POST_EDIT(id_invierno, **k):
        
    '''

    def GET(self, id_invierno, **k):
        message = None # Error message
        id_invierno = config.check_secure_val(str(id_invierno)) # HMAC id_invierno validate
        result = config.model.get_invierno(int(id_invierno)) # search for the id_invierno
        result.id_invierno = config.make_secure_val(str(result.id_invierno)) # apply HMAC for id_invierno
        return config.render.edit(result, message) # render invierno edit.html

    def POST(self, id_invierno, **k):
        form = config.web.input()  # get form data
        form['id_invierno'] = config.check_secure_val(str(form['id_invierno'])) # HMAC id_invierno validate
        # edit user with new data
        result = config.model.edit_invierno(
            form['id_invierno'],form['consejos'],
        )
        if result == None: # Error on udpate data
            id_invierno = config.check_secure_val(str(id_invierno)) # validate HMAC id_invierno
            result = config.model.get_invierno(int(id_invierno)) # search for id_invierno data
            result.id_invierno = config.make_secure_val(str(result.id_invierno)) # apply HMAC to id_invierno
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/invierno') # render invierno index.html
