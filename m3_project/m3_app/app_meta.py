from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from .actions import UsersPack


def register_urlpatterns():
	return [url(*controller.urlpattern)]


def register_actions():
	return controller.packs.extend([
    	    UsersPack(),
	])

def register_desktop_menu():
	desktop.uificate_the_controller(
		controller,
		menu_root=desktop.MainMenu.SubMenu('Пользователи'),
	)
