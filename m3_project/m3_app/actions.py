from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from .views import UsersEditWindow
from .models import User


class UsersPack(ObjectPack):
    model = User

    add_to_menu = True
    # add_window = UsersEditWindow
    # add_window = edit_window = ModelEditWindow.fabricate(model)
    add_window = edit_window = UsersEditWindow
