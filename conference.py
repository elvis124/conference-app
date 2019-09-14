#importing all the modules needed to run functions
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'multisamples', '1')
Config.set('postproc','desktop','1')
Config.set('kivy','exit_on_escape','1')
Config.set('kivy','log_enable','1')
Config.set('kivy', 'log_maxfiles', '+1')
Config.set('widgets', 'scroll_friction','float')
Config.set('widgets', 'scroll_distance', '4')
Config.set('graphics','borderless','0')
Config.set('graphics','rotation','0')
Config.set('graphics','full_screen','1')
Config.set('graphics','allow_screensaver','1')
Config.set('graphics','kivy_clock','free_all')
Config.set('widgets', 'scroll_distance', '4')
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.spelling import SpellingBase
from kivy.core.window import Window
from easygui import msgbox
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.checkbox import CheckBox
Window.clearcolor=(0,0,0,0)
from kivy.uix.checkbox import CheckBox
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.switch import Switch
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
import os
import sys
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty,NumericProperty
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.interactive import InteractiveLauncher
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.core.image import Image
from kivy.graphics import Color,Rectangle, Line
from kivy.uix.listview import ListItemButton, ListView, ListItemLabel
from kivy.uix. behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.loader import Loader
from kivy.support import install_twisted_reactor
from kivy.adapters.models import SelectableDataItem
from kivy.storage.jsonstore import JsonStore
from kivy.uix.dropdown import DropDown
from kivy.graphics import Line, SmoothLine
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.uix.spinner import Spinner
from kivy.base import EventLoop
from kivy.factory import Factory
from kivy.storage.jsonstore import JsonStore
EventLoop.window.title = 'maseno conference'
from kivy.loader import Loader
from kivy.uix.gridlayout import GridLayout, GridLayoutException, nmax, nmin
from collections import defaultdict
from kivy.uix.modalview import ModalView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton
from kivy.uix.spinner import Spinner
import sys
from datetime import datetime, time, date
from kivy.loader import Loader

Builder.load_file('conference.kv')

class Homescroll(BoxLayout):
	def __init__(self, **kwargs):
		super(Homescroll, self). __init__(**kwargs)
		self.bind(size=self._update_rect, pos=self._update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)
#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos = self.pos

#home screen layout codes
class Home(Screen):
	def __init__(self, **kwargs):
		super(Home, self). __init__(**kwargs)
		self.bind(size=self._update_rect, pos=self._update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)
#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos = self.pos
class Contacus(StackLayout):
	def __init__(self, **kwargs):
		super(Contacus, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos	
#class for vice chacelloer message
class Vicechancellor(StackLayout):
	cancel=ObjectProperty(None)
	def __init__(self, **kwargs):
		super(Vicechancellor, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#==================Director message=============
class Dvc(StackLayout):
	cancel=ObjectProperty(None)
	def __init__(self, **kwargs):
		super(Dvc, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
class Director_research(StackLayout):
	cancel=ObjectProperty(None)
	def __init__(self, **kwargs):
		super(Director_research, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#second screen 
class Conference(Screen):
	def __init__(self, **kwargs):
		super(Conference, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#=========================menu=================================================================================
	def confer(self, *args):
		self.ids['display'].clear_widgets()
		self.label2 = Label(text='Welcome Messages', size_hint=(1, .1), bold=True, font_size=18, color=[.3,.4,.6,1])
		self.but = Button(text='The Vice Chancellor', size_hint=(1, .2),font_size=14,on_press=self.vice_chancellor,background_color=[1,1,1,0], color=[.3, .4,.6, 1])
		self.but2 = Button(text='DVC-PRI',size_hint=(1, .1) ,font_size=14,on_press=self.dvc_pri,background_color=[1,1,1,0], color=[.3,.4,.6,1])
		self.but3 = Button(text='Director Research and innovation', size_hint=(1, .1), on_press=self.director,font_size=14, background_color=[1,1,1,0], color=[.3,.4,.6,1])
		self.but4 = Button(text='Speakers', font_size=18,bold=True,size_hint=(1, .1),background_color=[1,1,1,0], color=[.3,.4,.6,1])
		self.but5 = Button(text='Event Schedule', font_size=18,bold=True,size_hint=(1, .1),background_color=[1,1,1,0], color=[.3,.4,.6,1])
		self.but6 = Button(text='Conference Organizers', font_size=18,bold=True,size_hint=(1, .1),background_color=[1,1,1,0], color=[.3,.4,.6,1])
		self.lay=StackLayout(rows=7, orientation='tb-lr', size_hint=(1, 1))
		for i in [ self.label2, self.but, self.but2, self.but3, self.but4, self.but5, self.but6]:
			self.lay.add_widget(i)
		self.ids['display'].add_widget(self.lay)
	def themes(self, *args):
		self.ids['display'].clear_widgets()
		self.b1 = Button(text='Food and Nutrition Security', size_hint=(1, .1),font_size=14, background_color=[1,1,1,0], color=[.3, .4, .6,1])
		self.b2 = Button(text='Maternal, Child Health and Nutrition', size_hint=(1, .1),font_size=14, background_color=[1,1,1,0], color=[.3,.4, .6,1])
		self.b3 = Button(text='Societal Dynamics: Technology, Culture, Language and Crime',size_hint=(1, .1), font_size=14, background_color=[1,1,1,0], color=[.3, .4,.6, 1])
		self.grid = StackLayout(rows=3, orientation='tb-lr', size_hint=(1,1))
		for w in [ self.b1, self.b2, self.b3]:
			self.grid.add_widget(w)
		self.ids['display'].add_widget(self.grid)
	def travel(self, *args):
		self.ids['display'].clear_widgets()
		self.bb1 = Button(text='Accommodation', font_size=14,size_hint=(1, .1), background_color=[1,1,1,0], color=[.3, .4, .6,1])
		self.bb2 = Button(text='Health Needs', font_size=14,size_hint=(1, .1), background_color=[1,1,1,0], color=[.3, .4, .6, 1])
		self.bb3 = Button(text='Tour Kisumu', font_size=14,size_hint=(1, .1), background_color=[1,1,1,0], color=[.3, .4, .6, 1])
		self.gr = StackLayout(rows=3, orientation='tb-lr', size_hint=(1,1))
		for t in [ self.bb1, self.bb2, self.bb3]:
			self.gr.add_widget(t)
		self.ids['display'].add_widget(self.gr)
#vice chancellor message
	def vice_chancellor(self, *args):
		self.vice = Vicechancellor(cancel=self.dismiss)
		self.pop = Popup(title='Vice Chancellor Message',title_align='center', separator_color=[255,200,100,1],title_color=[0,1,0,1], content=self.vice, size_hint=(1, .7))
		self.pop.open()
		Clock.schedule_once(self.pop.dismiss, 60)
	def dismiss(self, *args):
		self.pop.dismiss()
#Dvc message
	def dvc_pri(self, *args):
		self.dvc=Dvc(cancel=self.dis)
		self.popp = Popup(title='DVC PRI MESSAGE', title_align='center', content=self.dvc,size_hint=(1, .7))
        self.popp.open()
        Clock.schedule_once(self.popp.dismiss, 60)
	def dis(self, *args):
		self.popp.dismiss()
#===================Director research===================================================================
	def director(self, *args):
		self.director = Director_research(cancel=self.diss)
		self.pop1 = Popup(title='Director Research and Innovation', title_align='center', content=self.director, size_hint=(1, .7))
        self.pop1.open()
        Clock.schedule_once(self.pop1.dismiss, 60)
	def diss(self, *args):
		self.pop1.dismiss()
#===================end======================================================


	def contact(self, *args):
		self.ids['display'].clear_widgets()
		self.con = Contacus()
		self.ids['display'].add_widget(self.con)

#=========================================popups===============================================================

#===============================================================================================================

#=================================================================================================================


#class for displaying the contents
class Countdown(GridLayout):
	def __init__(self, **kwargs):
		super(Countdown, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#second
class Secondpart(GridLayout):
	def __init__(self, **kwargs):
		super(Secondpart, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#Third
class Thirdpart(BoxLayout):
	def __init__(self, **kwargs):
		super(Thirdpart, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#display part
class Displaypart(StackLayout):
	def __init__(self, **kwargs):
		super(Displaypart, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#classs for menubuttons
class Menubuttons(GridLayout):
	def __init__(self, **kwargs):
		super(Menubuttons, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos



#function for registering
class Registerpart(BoxLayout):
	def __init__(self, **kwargs):
		super(Registerpart, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#=======================================abstract===============================
class Abstract(Screen):
	def __init__(self, **kwargs):
		super(Abstract, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos

class Conferenceregister(Screen):
	def __init__(self, **kwargs):
		super(Conferenceregister, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
class Welcomemessages(Screen):
	def __init__(self, **kwargs):
		super(Welcomemessages, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#=============================================================================
#screen manager 
class ScreenSwitcher(ScreenManager):
	def __init__(self, **kwargs):
		super(ScreenSwitcher, self). __init__(**kwargs)
		self.bind(size=self. _update_rect, pos=self. _update_rect)
		self.rect=Rectangle(size=self.size, pos=self.pos)

#function to update the screen size
	def _update_rect(self, *args):
		self.rect.size=self.size
		self.rect.pos=self.pos
#class for the manin screen
class Mainscreen(GridLayout):
	manager = ObjectProperty(None)

#class for compling the app
class MasenoConference(App):
    def build(self, *args):
        self.title='maseno conference '
        self.icon='icons/first.png'
        self.use_kivy_settings=False
        return Mainscreen()
    




if __name__=='__main__':
    MasenoConference().run()
