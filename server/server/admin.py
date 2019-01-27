from datetime import datetime

from flask import (
    Blueprint
)

from flask import current_app, g, redirect, url_for, request, abort
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.menu import MenuLink



def is_accessible():
    if g.get('user', None) is None:
        return False

    if g.user.email in current_app.config['AUTHORIZED_ADMINS'] or g.user.is_admin:
        return True

    return False


class RootAdminView(AdminIndexView):
    def is_accessible(self):
        return is_accessible()

    @expose('/')
    def index(self):
        
        users = []
        
        return self.render('admin_index.html', dt=datetime.now().strftime('%d %M %Y - %H %m %s'), users=users)


admin = Admin(name='server', index_view=RootAdminView(name='Home', url='/admin', endpoint='admin'))
mod = Blueprint('server-admin', __name__)


def init_app(app):
    admin.init_app(app)

    admin.add_link(MenuLink("server", "/"))

    

    app.register_blueprint(mod)
