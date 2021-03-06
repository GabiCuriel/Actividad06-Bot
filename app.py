# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/invierno', 'application.controllers.invierno.index.Index',
    '/invierno/view/(.+)', 'application.controllers.invierno.view.View',
    '/invierno/edit/(.+)', 'application.controllers.invierno.edit.Edit',
    '/invierno/delete/(.+)', 'application.controllers.invierno.delete.Delete',
    '/invierno/insert', 'application.controllers.invierno.insert.Insert',
    '/otonio', 'application.controllers.otonio.index.Index',
    '/otonio/view/(.+)', 'application.controllers.otonio.view.View',
    '/otonio/edit/(.+)', 'application.controllers.otonio.edit.Edit',
    '/otonio/delete/(.+)', 'application.controllers.otonio.delete.Delete',
    '/otonio/insert', 'application.controllers.otonio.insert.Insert',
    '/primavera', 'application.controllers.primavera.index.Index',
    '/primavera/view/(.+)', 'application.controllers.primavera.view.View',
    '/primavera/edit/(.+)', 'application.controllers.primavera.edit.Edit',
    '/primavera/delete/(.+)', 'application.controllers.primavera.delete.Delete',
    '/primavera/insert', 'application.controllers.primavera.insert.Insert',
    '/verano', 'application.controllers.verano.index.Index',
    '/verano/view/(.+)', 'application.controllers.verano.view.View',
    '/verano/edit/(.+)', 'application.controllers.verano.edit.Edit',
    '/verano/delete/(.+)', 'application.controllers.verano.delete.Delete',
    '/verano/insert', 'application.controllers.verano.insert.Insert',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
