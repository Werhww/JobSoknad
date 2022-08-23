from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.storage.jsonstore import JsonStore
from datetime import datetime
from datetime import timedelta

Builder.load_file('widgets.kv')
loginstorage  = JsonStore('logindata.json')
foodstorage = JsonStore('foodstorage.json')
drinkstorage = JsonStore('drinkstorage.json')

class Main(Widget):
	add_food = None

	def add_item(self, *args):
		if not self.add_food:
			self.add_food = MDDialog(
				title="Add Food",
				type="custom",
				content_cls=Add_food(),
				buttons=[
					MDFlatButton(
						text="CANCEL"
					),
					MDFlatButton(
						text="Add"
	 				),
				],
			)
		self.add_food.open()

	karbotall = ObjectProperty(None)
	def kalkulate(self):
		if self.ids.karbotall.text == "":
			self.ids.insulinsvar.text = ("Du må ta 0 Enheter Insulin")
		else:
			if loginstorage.exists('delantall'):
				Karbotall2 = int(self.ids.karbotall.text)
				self.karboantall = loginstorage.get('delantall')['tall']
				if self.karboantall == 1:
					self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
					self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

				elif self.karboantall == 2:
					
					time = int(loginstorage.get('delanall1')['time'])
					minutt =  int(loginstorage.get('delanall1')['minutt'])
					time2 = int(loginstorage.get('delanall2')['time'])
					minutt2 =  int(loginstorage.get('delanall2')['minutt'])
					hournow = int(hour)
					minuttnow = int(minute)
					time_hournow1 = hournow - time2

					if time_hournow1 > 0:
						self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
						self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					elif time_hournow1 == 0:
						if time2 <= hournow and minutt2 <= minuttnow:	
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )
					else:
						time_hournow2 = hournow - time

						if time_hournow2 > 0:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )


						elif time <= hournow and minutt <= minuttnow:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						else:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )
							
				elif self.karboantall == 3:
					
					time = int(loginstorage.get('delanall1')['time'])
					minutt =  int(loginstorage.get('delanall1')['minutt'])
					time2 = int(loginstorage.get('delanall2')['time'])
					minutt2 =  int(loginstorage.get('delanall2')['minutt'])
					time3 = int(loginstorage.get('delanall3')['time'])
					minutt3 =  int(loginstorage.get('delanall3')['minutt'])
					hournow = int(hour)
					minuttnow = int(minute)
					time_hournow1 = hournow - time3

					if time_hournow1 > 0:
						self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
						self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					elif time_hournow1 == 0:
						if time3 <= hournow and minutt3 <= minuttnow:	
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					else:
						time_hournow2 = hournow - time2
						if time_hournow2 > 0:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						elif time_hournow2 == 0:
							if time2 <= hournow and minutt2 <= minuttnow:	
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						else:
							time_hournow3 = hournow - time

							if time_hournow3 > 0:
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							elif time <= hournow and minutt <= minuttnow:
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							else:
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )


				elif self.karboantall == 4:
					
					time = int(loginstorage.get('delanall1')['time'])
					minutt =  int(loginstorage.get('delanall1')['minutt'])
					time2 = int(loginstorage.get('delanall2')['time'])
					minutt2 =  int(loginstorage.get('delanall2')['minutt'])
					time3 = int(loginstorage.get('delanall3')['time'])
					minutt3 =  int(loginstorage.get('delanall3')['minutt'])
					time4 = int(loginstorage.get('delanall4')['time'])
					minutt4 = int(loginstorage.get('delanall4')['minutt'])
					hournow = int(hour)
					minuttnow = int(minute)
					time_hournow1 = hournow - time4

					if time_hournow1 > 0:
						self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
						self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					elif time_hournow1 == 0:
						if time4 <= hournow and minutt4 <= minuttnow:	
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					else:
						time_hournow2 = hournow - time3
						if time_hournow2 > 0:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						elif time_hournow2 == 0:
							if time3 <= hournow and minutt3 <= minuttnow:	
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						else:
							time_hournow3 = hournow - time2
							if time_hournow3 > 0:
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							elif time_hournow3 == 0:
								if time2 <= hournow and minutt2 <= minuttnow:	
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							else:
								time_hournow4 = hournow - time

								if time_hournow4 > 0:
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

								elif time <= hournow and minutt <= minuttnow:
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

								else:
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

				elif self.karboantall == 5:
					
					time = int(loginstorage.get('delanall1')['time'])
					minutt =  int(loginstorage.get('delanall1')['minutt'])
					time2 = int(loginstorage.get('delanall2')['time'])
					minutt2 =  int(loginstorage.get('delanall2')['minutt'])
					time3 = int(loginstorage.get('delanall3')['time'])
					minutt3 =  int(loginstorage.get('delanall3')['minutt'])
					time4 = int(loginstorage.get('delanall4')['time'])
					minutt4 = int(loginstorage.get('delanall4')['minutt'])
					time5 = int(loginstorage.get('delanall5')['time'])
					minutt5 = int(loginstorage.get('delanall5')['minutt'])
					hournow = int(hour)
					minuttnow = int(minute)
					time_hournow1 = hournow - time5

					if time_hournow1 > 0:
						self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall5')['delingstall']) 
						self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					elif time_hournow1 == 0:
						if time5 <= hournow and minutt5 <= minuttnow:	
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall5')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					else:
						time_hournow2 = hournow - time4
						if time_hournow2 > 0:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						elif time_hournow2 == 0:
							if time4 <= hournow and minutt4 <= minuttnow:	
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						else:
							time_hournow3 = hournow - time3
							if time_hournow3 > 0:
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
								self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							elif time_hournow3 == 0:
								if time3 <= hournow and minutt3 <= minuttnow:	
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							else:
								time_hournow2 = hournow - time2

								if time_hournow2 > 0:
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

								elif time2 <= hournow and minutt2 <= minuttnow:
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
									self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

								else:
									time_hournow4 = hournow - time

									if time_hournow4 > 0:
										self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
										self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

									elif time <= hournow and minutt <= minuttnow:	
										self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
										self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )
									else:
										self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall5')['delingstall']) 
										self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

				elif self.karboantall == 6:
					
					time = int(loginstorage.get('delanall1')['time'])
					minutt =  int(loginstorage.get('delanall1')['minutt'])
					time2 = int(loginstorage.get('delanall2')['time'])
					minutt2 =  int(loginstorage.get('delanall2')['minutt'])
					time3 = int(loginstorage.get('delanall3')['time'])
					minutt3 =  int(loginstorage.get('delanall3')['minutt'])
					time4 = int(loginstorage.get('delanall4')['time'])
					minutt4 = int(loginstorage.get('delanall4')['minutt'])
					time5 = int(loginstorage.get('delanall5')['time'])
					minutt5 = int(loginstorage.get('delanall5')['minutt'])
					time6 = int(loginstorage.get('delanall6')['time'])
					minutt6 = int(loginstorage.get('delanall6')['minutt'])
					hournow = int(hour)
					minuttnow = int(minute)
					time_hournow = hournow - time6

					if time_hournow > 0:
						self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall6')['delingstall']) 
						self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					elif time_hournow == 0:
						if time6 <= hournow and minutt6 <= minuttnow:	
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall6')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

					else:
						time_hournow1 = hournow - time5
						if time_hournow1 > 0:
							self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall5')['delingstall']) 
							self.ids.insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						elif time_hournow1 == 0:
							if time5 <= hournow and minutt5 <= minuttnow:	
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall5')['delingstall']) 
								self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

						else:
							time_hournow2 = hournow - time4
							if time_hournow2 > 0:
								self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
								self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

							elif time_hournow2 == 0:
								if time4 <= hournow and minutt4 <= minuttnow:	
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall4')['delingstall']) 
									self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )
										
							else:
								time_hournow3 = hournow - time3
								if time_hournow3 > 0:
									self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
									self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )


								elif time_hournow3 == 0:
									if time3 <= hournow and minutt3 <= minuttnow:	
										self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall3')['delingstall']) 
									self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

								else:
									time_hournow2 = hournow - time2

									if time_hournow2 > 0:
										self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
										self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

									elif time2 <= hournow and minutt2 <= minuttnow:
										self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall2')['delingstall']) 
										self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

									else:
										time_hournow4 = hournow - time

										if time_hournow4 > 0:
											self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
											self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

										elif time <= hournow and minutt <= minuttnow:
											self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall1')['delingstall']) 
											self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

										else:
											self.Karbohydrater = (Karbotall2 / loginstorage.get('delanall6')['delingstall']) 
											self.ids.Insulinsvar.text = ("Du må ta " + str(format(self.Karbohydrater, '.1f')) + " Enheter Insulin" )

			else:
				self.ids.insulinsvar.text = ("Du må logge in for å bruke kalkulatoren")

	def show_menu(self):
		window_size = str(Window.size)
		WindowWitdh,WindowHeigth = window_size.split(",")
		Height = WindowHeigth.split(")")
		Witdh = WindowWitdh.split("(")
		global showmenu
		showmenu = Mainmenu()

		showmenu = Popup(title="Menu", content=showmenu, size_hint=(None,None), size=((int(Witdh[1]) / 3), Height[0]), pos_hint={'y': 0, 'x':0})

		showmenu.open()

class Add_food(BoxLayout):
	pass

class ContentNavigationDrawer(GridLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    def open_datatabel(*args):
    	mat_datatable()

class FoodTab(MDFloatLayout, MDTabsBase):

	def __init__(self, **kwargs):
		super(FoodTab, self).__init__(**kwargs)

		if foodstorage.exists('all_food'):
			mat_antall = (int(foodstorage.get('all_food')['antall']))
		else:
			foodstorage.put('all_food', antall=(0))
			mat_antall = (int(foodstorage.get('all_food')['antall']))

		foodstorage.put( 1, foodname=('eple'), foodcarbo=('15'), amount=("per slice"), ext_time=("X"), ext_prosent=("X"))
		foodstorage.put('all_food', antall=(1))


		if mat_antall > 0:
			if mat_antall == 1:
				try:

					self.food_tabel = MDDataTable(
						pos_hint={'center_y': 0.5, 'center_x': 0.5},
						size_hint=(1, 1),
						column_data=[
							("Name", dp(30)),
							("Carbohydrates", dp(30)),
							("Amount", dp(30)),
							("Extended Time", dp(30)),
							("Extended Prosented", dp(30)),
						],
						row_data=[
							(foodstorage.get(1)['foodname'], 
							foodstorage.get(1)['foodcarbo'], 
							foodstorage.get(1)['amount'], 
							foodstorage.get(1)['ext_time'], 
							foodstorage.get(1)['ext_prosent'])for i in range(2)
						],
					)

					self.add_widget(self.food_tabel)

				except ValueError:
					print("pop")
			else:
				try:
					mat_antall = range(int(foodstorage.get('all_food')['antall']))
					self.food_tabel = MDDataTable(
						pos_hint={'center_y': 0.5, 'center_x': 0.5},
						size_hint=(1, 1),
						column_data=[
							("Name", dp(30)),
							("Carbohydrates", dp(30)),
							("Amount", dp(30)),
							("Extended Time", dp(30)),
							("Extended Prosented", dp(30)),
						],
						row_data=[
							(foodstorage.get(1 + i)['foodname'], 
							foodstorage.get(1 + i)['foodcarbo'], 
							foodstorage.get(1 + i)['amount'], 
							foodstorage.get(1 + i)['ext_time'], 
							foodstorage.get(1 + i)['ext_prosent'])for i in mat_antall
						],
					)

					self.add_widget(self.food_tabel)

				except ValueError:
					print("pop")

		else:
			self.food_tabel = MDDataTable(
				pos_hint={'center_y': 0.5, 'center_x': 0.5},
				size_hint=(1, 1),
				column_data=[
					("Name", dp(30)),
					("Carbohydrates", dp(30)),
					("Extended Insulin", dp(30)),
					("Extended Time", dp(30)),
					("Extended Prosented", dp(30)),
				],
				row_data=[
					()
				],
			)

			self.add_widget(self.food_tabel)

class DrinksTab(MDFloatLayout, MDTabsBase):

	def __init__(self, **kwargs):
		super(DrinksTab, self).__init__(**kwargs)

		self.drinks_tabel = MDDataTable(
			pos_hint={'center_y': 0.5, 'center_x': 0.5},
			size_hint=(1, 1),
			column_data=[
				("Name", dp(30)),
				("Carbohydrates", dp(30)),
				("Extended Insulin", dp(30)),
				("Extended Time", dp(30)),
				("Extended Prosented", dp(30)),
			],
			row_data=[
				("dd", "ff", "yes", "2", "5%",) for i in range(0,5)
			],
		)

		self.add_widget(self.drinks_tabel)
		
class loginwindow(FloatLayout):
	name = ObjectProperty(None)
	antalldelingstall = 0
	def sliderdeltall(self, *args):
		global antalldelingstall

		self.antalldelingstall = args[1]
		self.deltallbl.text = str(int(args[1]))

	def showlogin2(self):
			global popupwindow2

			if self.antalldelingstall == 1:
				show2 = loginwindow2_1()

				popupwindow2 = Popup(title="Login", content=show2, size_hint=(None,None), size=(Window.size))

				popupwindow2.open()
				loginstorage.put('you', name=(self.name.text))

			elif self.antalldelingstall == 2:
				show2 = loginwindow2_2()

				popupwindow2 = Popup(title="Login", content=show2, size_hint=(None,None), size=(Window.size))

				popupwindow2.open()
				loginstorage.put('you', name=(self.name.text))

			elif self.antalldelingstall == 3:
				show2 = loginwindow2_3()

				popupwindow2 = Popup(title="Login", content=show2, size_hint=(None,None), size=(Window.size))

				popupwindow2.open()
				loginstorage.put('you', name=(self.name.text))

			elif self.antalldelingstall == 4:
				show2 = loginwindow2_4()

				popupwindow2 = Popup(title="Login", content=show2, size_hint=(None,None), size=(Window.size))

				popupwindow2.open()
				loginstorage.put('you', name=(self.name.text))

			elif self.antalldelingstall == 5:
				show2 = loginwindow2_5()

				popupwindow2 = Popup(title="Login", content=show2, size_hint=(None,None), size=(Window.size))

				popupwindow2.open()
				loginstorage.put('you', name=(self.name.text))

			elif self.antalldelingstall == 6:
				show2 = loginwindow2_6()

				popupwindow2 = Popup(title="Login", content=show2, size_hint=(None,None), size=(Window.size))

				popupwindow2.open()
				loginstorage.put('you', name=(self.name.text))
			else:
				self.deltallbl.text = str("Du må bevege Slideren")

	def close(self):
		popupwindowstart.dismiss()
		popupwindow.dismiss()

class loginwindow2_1(FloatLayout):
	deltalltext1 = ObjectProperty(None)
	def login(self):
		try:
			deltall1 = int(self.deltalltext1.text)
			loginstorage.put('delanall1', delingstall=(deltall1))
			loginstorage.put('delantall', tall= 1)
			loginstorage.put('login')
			if loginstorage.exists('delanall2'):
				loginstorage.delete('delanall2')
			if loginstorage.exists('delanall3'):
				loginstorage.delete('delanall3')
			if loginstorage.exists('delanall4'):
				loginstorage.delete('delanall4')
			if loginstorage.exists('delanall5'):
				loginstorage.delete('delanall5')
			if loginstorage.exists('delanall6'):
				loginstorage.delete('delanall6')

			popupwindowstart.dismiss()
			popupwindow.dismiss()
			popupwindow2.dismiss()
		except ValueError:
			self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
			self.ids.error.text = ("Error: Du må skrive tall som\n 1 og 2 i Delingstall vinduet")

class loginwindow2_2(FloatLayout):
	deltalltext1 = ObjectProperty(None)
	deltalltext2 = ObjectProperty(None)
	timer1 = ObjectProperty(None)
	minuter1 = ObjectProperty(None)
	timer2 = ObjectProperty(None)
	minuter2 = ObjectProperty(None)

	def login(self):
		try:
			deltall1 = int(self.deltalltext1.text)
			deltall2 = int(self.deltalltext2.text)
			timer11 = int(self.timer1.text)
			minuter11 = int(self.minuter1.text)
			timer22 = int(self.timer2.text)
			minuter22 = int(self.minuter2.text)
			time_1 = 24 - timer11
			time_2 = 24 - timer22
			minutt_1 = 60 - minuter11
			minutt_2 = 60 - minuter22

			if timer11 < timer22:
				if time_1 < 0  or time_2 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif time_1 == 0  or time_2 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif minutt_1 < 0 or minutt_2 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				elif minutt_1 == 0 or minutt_2 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")


				else:
					loginstorage.put('delanall1', delingstall=(deltall1), time=(timer11), minutt=(minuter11))
					loginstorage.put('delanall2', delingstall=(deltall2), time=(timer22), minutt=(minuter22))
					loginstorage.put('delantall', tall= 2)
					loginstorage.put('login')
					if loginstorage.exists('delanall3'):
						loginstorage.delete('delanall3')
					if loginstorage.exists('delanall4'):
						loginstorage.delete('delanall4')
					if loginstorage.exists('delanall5'):
						loginstorage.delete('delanall5')
					if loginstorage.exists('delanall6'):
						loginstorage.delete('delanall6')

					popupwindowstart.dismiss()
					popupwindow.dismiss()
					popupwindow2.dismiss()
			elif timer11 == timer22:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Det må være en time\n forskjell mellom timene")

			else:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 1 mår være \nlavere enn Timer 2")

		except ValueError:
			self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
			self.ids.error.text = ("Error: \n Du må fylle ut alle vinduene,\n og de må inneholde tall")

class loginwindow2_3(FloatLayout):
	deltalltext1 = ObjectProperty(None)
	deltalltext2 = ObjectProperty(None)
	deltalltext3 = ObjectProperty(None)
	timer1 = ObjectProperty(None)
	minuter1 = ObjectProperty(None)
	timer2 = ObjectProperty(None)
	minuter2 = ObjectProperty(None)
	timer3 = ObjectProperty(None)
	minuter3 = ObjectProperty(None)

	def login(self):
		try:
			deltall1 = int(self.deltalltext1.text)
			deltall2 = int(self.deltalltext2.text)
			deltall3 = int(self.deltalltext3.text)
			timer11 = int(self.timer1.text)
			minuter11 = int(self.minuter1.text)
			timer22 = int(self.timer2.text)
			minuter22 = int(self.minuter2.text)
			timer33 = int(self.timer3.text)
			minuter33 = int(self.minuter3.text)
			time_1 = 24 - timer11
			time_2 = 24 - timer22
			time_3 = 24 - timer33
			minutt_1 = 60 - minuter11
			minutt_2 = 60 - minuter22
			minutt_3 = 60 - minuter33

			if timer11 < timer22 and timer22 < timer33:
				if time_1 < 0  or time_2 < 0 or time_3 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif time_1 == 0  or time_2 == 0 or time_3 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif minutt_1 < 0 or minutt_2 < 0 or minutt_3 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				elif minutt_1 == 0 or minutt_2 == 0  or minutt_3 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")


				else:
					loginstorage.put('delanall1', delingstall=(deltall1), time=(timer11), minutt=(minuter11))
					loginstorage.put('delanall2', delingstall=(deltall2), time=(timer22), minutt=(minuter22))
					loginstorage.put('delanall3', delingstall=(deltall3), time=(timer33), minutt=(minuter33))
					loginstorage.put('delantall', tall= 3)
					loginstorage.put('login')
					if loginstorage.exists('delanall4'):
						loginstorage.delete('delanall4')
					if loginstorage.exists('delanall5'):
						loginstorage.delete('delanall5')
					if loginstorage.exists('delanall6'):
						loginstorage.delete('delanall6')

					popupwindowstart.dismiss()
					popupwindow.dismiss()
					popupwindow2.dismiss()
			elif timer11 == timer22 or timer22 == timer33:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Det må være en time\n forskjell mellom timene")

			elif timer11 > timer22:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 1 må være \nlavere enn Timer 2")

			elif timer22 > timer33:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 2 må være \nlavere enn Timer 3")

		except ValueError:
			self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
			self.ids.error.text = ("Error: \n Du må fylle ut alle vinduene,\n og de må inneholde tall")

class loginwindow2_4(FloatLayout):
	deltalltext1 = ObjectProperty(None)
	deltalltext2 = ObjectProperty(None)
	deltalltext3 = ObjectProperty(None)
	deltalltext4 = ObjectProperty(None)
	timer1 = ObjectProperty(None)
	minuter1 = ObjectProperty(None)
	timer2 = ObjectProperty(None)
	minuter2 = ObjectProperty(None)
	timer3 = ObjectProperty(None)
	minuter3 = ObjectProperty(None)
	timer4 = ObjectProperty(None)
	minuter4 = ObjectProperty(None)

	def login(self):
		try:
			deltall1 = int(self.deltalltext1.text)
			deltall2 = int(self.deltalltext2.text)
			deltall3 = int(self.deltalltext3.text)
			deltall4 = int(self.deltalltext4.text)
			timer11 = int(self.timer1.text)
			minuter11 = int(self.minuter1.text)
			timer22 = int(self.timer2.text)
			minuter22 = int(self.minuter2.text)
			timer33 = int(self.timer3.text)
			minuter33 = int(self.minuter3.text)
			timer44 = int(self.timer4.text)
			minuter44 = int(self.minuter4.text)

			time_1 = 24 - timer11
			time_2 = 24 - timer22
			time_3 = 24 - timer33
			time_4 = 24 - timer44
			minutt_1 = 60 - minuter11
			minutt_2 = 60 - minuter22
			minutt_3 = 60 - minuter33
			minutt_4 = 60 - minuter44

			if timer11 < timer22 and timer22 < timer33 and timer44 < timer44:

				if time_1 < 0  or time_2 < 0 or time_3 < 0 or time_4 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif time_1 == 0  or time_2 == 0 or time_3 == 0 or time_4 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif minutt_1 < 0 or minutt_2 < 0 or minutt_3 < 0 or minutt_4 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				elif minutt_1 == 0 or minutt_2 == 0  or minutt_3 == 0 or minutt_4 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				else:
					loginstorage.put('delanall1', delingstall=(deltall1), time=(timer11), minutt=(minuter11))
					loginstorage.put('delanall2', delingstall=(deltall2), time=(timer22), minutt=(minuter22))
					loginstorage.put('delanall3', delingstall=(deltall3), time=(timer33), minutt=(minuter33))
					loginstorage.put('delanall4', delingstall=(deltall4), time=(timer44), minutt=(minuter44))
					loginstorage.put('delantall', tall= 4)
					loginstorage.put('login')
					if loginstorage.exists('delanall5'):
						loginstorage.delete('delanall5')
					if loginstorage.exists('delanall6'):
						loginstorage.delete('delanall6')

					popupwindowstart.dismiss()
					popupwindow.dismiss()
					popupwindow2.dismiss()

			elif timer11 == timer22 or timer22 == timer33 or timer33 == timer44:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Det må være en time\n forskjell mellom timene")

			elif timer11 > timer22:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 1 må være \nlavere enn Timer 2")

			elif timer22 > timer33:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 2 må være \nlavere enn Timer 3")

			elif timer33 > timer44:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 3 må være \nlavere enn Timer 4")

		except ValueError:
			self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
			self.ids.error.text = ("Error: \n Du må fylle ut alle vinduene,\n og de må inneholde tall")

class loginwindow2_5(FloatLayout):
	deltalltext1 = ObjectProperty(None)
	deltalltext2 = ObjectProperty(None)
	deltalltext3 = ObjectProperty(None)
	deltalltext4 = ObjectProperty(None)
	deltalltext5 = ObjectProperty(None)
	timer1 = ObjectProperty(None)
	minuter1 = ObjectProperty(None)
	timer2 = ObjectProperty(None)
	minuter2 = ObjectProperty(None)
	timer3 = ObjectProperty(None)
	minuter3 = ObjectProperty(None)
	timer4 = ObjectProperty(None)
	minuter4 = ObjectProperty(None)
	timer5 = ObjectProperty(None)
	minuter5 = ObjectProperty(None)

	def login(self):
		try:
			deltall1 = int(self.deltalltext1.text)
			deltall2 = int(self.deltalltext2.text)
			deltall3 = int(self.deltalltext3.text)
			deltall4 = int(self.deltalltext4.text)
			deltall5 = int(self.deltalltext5.text)
			timer11 = int(self.timer1.text)
			minuter11 = int(self.minuter1.text)
			timer22 = int(self.timer2.text)
			minuter22 = int(self.minuter2.text)
			timer33 = int(self.timer3.text)
			minuter33 = int(self.minuter3.text)
			timer44 = int(self.timer4.text)
			minuter44 = int(self.minuter4.text)
			timer55 = int(self.timer5.text)
			minuter55 = int(self.minuter5.text)

			time_1 = 24 - timer11
			time_2 = 24 - timer22
			time_3 = 24 - timer33
			time_4 = 24 - timer44
			time_5 = 24 - timer55
			minutt_1 = 60 - minuter11
			minutt_2 = 60 - minuter22
			minutt_3 = 60 - minuter33
			minutt_4 = 60 - minuter44
			minutt_5 = 60 - minuter55

			if timer11 < timer22 and timer22 < timer33 and timer44 < timer44 and timer44 < timer55:
				if time_1 < 0  or time_2 < 0 or time_3 < 0 or time_4 < 0 or time_5 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif time_1 == 0  or time_2 == 0 or time_3 == 0 or time_4 == 0 or time_5 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif minutt_1 < 0 or minutt_2 < 0 or minutt_3 < 0 or minutt_4 < 0 or minutt_5 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				elif minutt_1 == 0 or minutt_2 == 0  or minutt_3 == 0 or minutt_4 == 0 or minutt_5 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				else:
					loginstorage.put('delanall1', delingstall=(deltall1), time=(timer11), minutt=(minuter11))
					loginstorage.put('delanall2', delingstall=(deltall2), time=(timer22), minutt=(minuter22))
					loginstorage.put('delanall3', delingstall=(deltall3), time=(timer33), minutt=(minuter33))
					loginstorage.put('delanall4', delingstall=(deltall4), time=(timer44), minutt=(minuter44))
					loginstorage.put('delanall5', delingstall=(deltall5), time=(timer55), minutt=(minuter55))
					loginstorage.put('delantall', tall= 5)
					loginstorage.put('login')
					if loginstorage.exists('delanall6'):
						loginstorage.delete('delanall6')

					popupwindowstart.dismiss()
					popupwindow.dismiss()
					popupwindow2.dismiss()

			elif timer11 == timer22 or timer22 == timer33 or timer33 == timer44 or timer44 == timer55:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Det må være en time\n forskjell mellom timene")

			elif timer11 > timer22:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 1 må være \nlavere enn Timer 2")

			elif timer22 > timer33:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 2 må være \nlavere enn Timer 3")

			elif timer33 > timer44:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 3 må være \nlavere enn Timer 4")

			elif timer44 > timer55:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 4 må være \nlavere enn Timer 5")

		except ValueError:
			self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
			self.ids.error.text = ("Error: \n Du må fylle ut alle vinduene,\n og de må inneholde tall")

class loginwindow2_6(FloatLayout):
	deltalltext1 = ObjectProperty(None)
	deltalltext2 = ObjectProperty(None)
	deltalltext3 = ObjectProperty(None)
	deltalltext4 = ObjectProperty(None)
	deltalltext5 = ObjectProperty(None)
	deltalltext6 = ObjectProperty(None)
	timer1 = ObjectProperty(None)
	minuter1 = ObjectProperty(None)
	timer2 = ObjectProperty(None)
	minuter2 = ObjectProperty(None)
	timer3 = ObjectProperty(None)
	minuter3 = ObjectProperty(None)
	timer4 = ObjectProperty(None)
	minuter4 = ObjectProperty(None)
	timer5 = ObjectProperty(None)
	minuter5 = ObjectProperty(None)
	timer6 = ObjectProperty(None)
	minuter6 = ObjectProperty(None)

	def login(self):
		try:
			deltall1 = int(self.deltalltext1.text)
			deltall2 = int(self.deltalltext2.text)
			deltall3 = int(self.deltalltext3.text)
			deltall4 = int(self.deltalltext4.text)
			deltall5 = int(self.deltalltext5.text)
			deltall6 = int(self.deltalltext6.text)
			timer11 = int(self.timer1.text)
			minuter11 = int(self.minuter1.text)
			timer22 = int(self.timer2.text)
			minuter22 = int(self.minuter2.text)
			timer33 = int(self.timer3.text)
			minuter33 = int(self.minuter3.text)
			timer44 = int(self.timer4.text)
			minuter44 = int(self.minuter4.text)
			timer55 = int(self.timer5.text)
			minuter55 = int(self.minuter5.text)
			timer66 = int(self.timer6.text)
			minuter66 = int(self.minuter6.text)

			time_1 = 24 - timer11
			time_2 = 24 - timer22
			time_3 = 24 - timer33
			time_4 = 24 - timer44
			time_5 = 24 - timer55
			time_6 = 24 - timer66
			minutt_1 = 60 - minuter11
			minutt_2 = 60 - minuter22
			minutt_3 = 60 - minuter33
			minutt_4 = 60 - minuter44
			minutt_5 = 60 - minuter55
			minutt_6 = 60 - minuter66

			if timer11 < timer22 and timer22 < timer33 and timer44 < timer44 and timer44 < timer55 and timer55 < timer66:

				if time_1 < 0  or time_2 < 0 or time_3 < 0 or time_4 < 0 or time_5 < 0 or time_6 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif time_1 == 0  or time_2 == 0 or time_3 == 0 or time_4 == 0 or time_5 == 0 or time_6 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Timer må være lavere en 24!")

				elif minutt_1 < 0 or minutt_2 < 0 or minutt_3 < 0 or minutt_4 < 0 or minutt_5 < 0 or minutt_6 < 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				elif minutt_1 == 0 or minutt_2 == 0  or minutt_3 == 0 or minutt_4 == 0 or minutt_5 == 0 or minutt_6 == 0:
					self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
					self.ids.error.text = ("Error: Minutter må være lavere en 60!")

				else:
					loginstorage.put('delanall1', delingstall=(deltall1), time=(timer11), minutt=(minuter11))
					loginstorage.put('delanall2', delingstall=(deltall2), time=(timer22), minutt=(minuter22))
					loginstorage.put('delanall3', delingstall=(deltall3), time=(timer33), minutt=(minuter33))
					loginstorage.put('delanall4', delingstall=(deltall4), time=(timer44), minutt=(minuter44))
					loginstorage.put('delanall5', delingstall=(deltall5), time=(timer55), minutt=(minuter55))
					loginstorage.put('delanall6', delingstall=(deltall6), time=(timer66), minutt=(minuter66))
					loginstorage.put('delantall', tall= 6)
					loginstorage.put('login')

					popupwindowstart.dismiss()
					popupwindow.dismiss()
					popupwindow2.dismiss()

			elif timer11 == timer22 or timer22 == timer33 or timer33 == timer44 or timer44 == timer55 or timer55 == timer66:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Det må være en time\n forskjell mellom timene")

			elif timer11 > timer22:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 1 må være \nlavere enn Timer 2")

			elif timer22 > timer33:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 2 må være \nlavere enn Timer 3")

			elif timer33 > timer44:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 3 må være \nlavere enn Timer 4")

			elif timer44 > timer55:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 4 må være \nlavere enn Timer 5")

			elif timer55 > timer66:
				self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
				self.ids.error.text = ("Error: Timer 5 må være \nlavere enn Timer 6")

		except ValueError:
			self.ids.loginbtn.pos_hint = {'x':0.7, 'y':0}
			self.ids.error.text = ("Error: \n Du må fylle ut alle vinduene,\n og de må inneholde tall")

def showloginstart(*args):
	global popupwindowstart
	show3 = loginwindow()

	popupwindowstart = Popup(title="Login", content=show3, size_hint=(None,None), size=(Window.size))

	popupwindowstart.open()

def showlogin1():
	global popupwindow
	show = loginwindow()

	popupwindow = Popup(title="Login", content=show, size_hint=(None,None), size=(Window.size))

	popupwindow.open()

if loginstorage.exists('login'):
	print("Du er logget inn")
else:
	Clock.schedule_once(showloginstart, 1)



class DiabetesApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Teal"
		self.theme_cls.primary_hue = "400"
		self.now = datetime.now()
		Clock.schedule_interval(self.update_clock, 1)

		return Main()

	def update_clock(self, *args):
		global hour
		global minute
		self.now = self.now + timedelta(seconds = 1)
		self.my_label = self.now.strftime('%H:%M:%S')
		self.time = self.my_label
		hour,minute,second = self.time.split(":")



if __name__ == '__main__':
    DiabetesApp().run()