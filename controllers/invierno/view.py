import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_invierno):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_invierno) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_invierno):
    '''

    def GET(self, id_invierno):
        id_invierno = config.check_secure_val(str(id_invierno)) # HMAC id_invierno validate
        result = config.model.get_invierno(id_invierno) # search for the id_invierno data
        return config.render.view(result) # render view.html with id_invierno data
