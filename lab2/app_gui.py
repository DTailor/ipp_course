from PyQt4 import QtCore, QtGui
from random import randint


def debug_trace():
  '''Set a tracepoint in the Python debugger that works with Qt'''
  from PyQt4.QtCore import pyqtRemoveInputHook
  from ipdb import set_trace
  pyqtRemoveInputHook()
  set_trace()

class App_Gui(object):
    def setup(self, App):
        self.app = App
        App.setObjectName("App")
        App.resize(500, 350)
        self.user_name_input = ''
        App.setWindowTitle('App Title')
        self.gridLayout = QtGui.QGridLayout(App)
        self.name_input_label = QtGui.QLabel(App)
        self.name_input = QtGui.QLineEdit(App)
        self.to_stage_two = QtGui.QPushButton('Next')
        self.to_stage_one = QtGui.QPushButton('Back')
        

        self.price_update = QtGui.QLineEdit(App)
        self.price_update.setEnabled(False)
        self.price_total = '20'
        self.to_stage_three = QtGui.QPushButton('Next')

        self.feta = QtGui.QCheckBox('Feta')
        self.parmesan = QtGui.QCheckBox('Parmesan')
        self.mozarella = QtGui.QCheckBox('Mozarella')
        self.dor_blue = QtGui.QCheckBox('Dor Blue')
        self.edam = QtGui.QCheckBox('Edam')
        self.brinza = QtGui.QCheckBox('Brinza')

        self.bacon = QtGui.QCheckBox('Bacon')
        self.prosciutto = QtGui.QCheckBox('Prosciutto')
        self.salami = QtGui.QCheckBox('Salami')
        self.chicken = QtGui.QCheckBox('Chicken Breast')

        self.fresh_mush = QtGui.QCheckBox('Fresh Mushrooms')
        self.smoc_mush = QtGui.QCheckBox('Smocked Mushrooms')
        self.onion = QtGui.QCheckBox('Red Onion')
        self.tomato = QtGui.QCheckBox('Tomato')
        self.garlic = QtGui.QCheckBox('Garlic')
        self.rucola = QtGui.QCheckBox('Rucola')
        self.mar_go = QtGui.QCheckBox('Marin. Gogo')
        self.corn = QtGui.QCheckBox('Corn')
        self.parsley = QtGui.QCheckBox('Parsley')
        self.ch_pepper = QtGui.QCheckBox('Chili Pepper')

        self.feta.clicked.connect(lambda: self.add_product(self.feta))
        self.parmesan.clicked.connect(lambda: self.add_product(self.parmesan))
        self.mozarella.clicked.connect(lambda: self.add_product(self.mozarella))
        self.dor_blue.clicked.connect(lambda: self.add_product(self.dor_blue))
        self.edam.clicked.connect(lambda: self.add_product(self.edam))

        self.bacon.clicked.connect(lambda: self.add_product(self.bacon))
        self.brinza.clicked.connect(lambda: self.add_product(self.brinza))
        self.prosciutto.clicked.connect(lambda: self.add_product(self.prosciutto))
        self.salami.clicked.connect(lambda: self.add_product(self.salami))
        self.chicken.clicked.connect(lambda: self.add_product(self.chicken))
        self.fresh_mush.clicked.connect(lambda: self.add_product(self.fresh_mush))
        self.smoc_mush.clicked.connect(lambda: self.add_product(self.smoc_mush))
        self.onion.clicked.connect(lambda: self.add_product(self.onion))
        self.tomato.clicked.connect(lambda: self.add_product(self.tomato))

        self.garlic.clicked.connect(lambda: self.add_product(self.garlic))
        self.rucola.clicked.connect(lambda: self.add_product(self.rucola))
        self.mar_go.clicked.connect(lambda: self.add_product(self.mar_go))
        self.corn.clicked.connect(lambda: self.add_product(self.corn))
        self.parsley.clicked.connect(lambda: self.add_product(self.parsley))
        self.ch_pepper.clicked.connect(lambda: self.add_product(self.ch_pepper))

        self.finish_string_label = QtGui.QLabel(App)

        self.draw_step_one()

    def clear_step_two(self):
        first = [self.feta, self.parmesan, self.mozarella, self.dor_blue, self.edam, self.brinza]
        second = [self.bacon, self.prosciutto, self.salami, self.chicken]
        third = [self.fresh_mush, self.smoc_mush, self.onion, self.tomato, self.garlic, self.rucola, self.mar_go, self.corn, self.parsley, self.ch_pepper]

        for btn in first:
            btn.setParent(None)

        for btn in second:
            btn.setParent(None)

        for btn in third:
            btn.setParent(None)

        self.price_update.setParent(None)
        self.to_stage_three.setParent(None)
        self.to_stage_one.setParent(None)

    def draw_step_one(self):
        App = self.app

        try:
            self.clear_step_two()
        except:
            pass
        self.name_input_label.setObjectName("Name Input Label")
        self.gridLayout.addWidget(self.name_input_label, 1, 0, 1, 1)
        self.name_input_label.setText('Your Name')
        
        self.name_input.setObjectName("Name Input")
        self.name_input.setText(self.user_name_input)
        self.gridLayout.addWidget(self.name_input, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.to_stage_two, 2, 0, 1, 2)

        self.to_stage_two.clicked.connect(self.draw_step_two)

    def draw_step_two(self):
        App = self.app
        # Remove step 1
        self.user_name_input = self.name_input.text()
        self.name_input_label.setParent(None)
        self.name_input.setParent(None)
        self.to_stage_two.setParent(None)

        # Set step 2
        self.price_update.setObjectName("Price Update")
        self.price_update.setText(self.price_total)
        self.gridLayout.addWidget(self.price_update, 5, 1)

        self.gridLayout.addWidget(self.to_stage_one, 5, 0)
        self.to_stage_one.clicked.connect(self.draw_step_one)

        self.gridLayout.addWidget(self.to_stage_three, 5, 2)
        self.to_stage_three.clicked.connect(self.draw_step_three)

        # First Row (Cheese)
        self.feta.price = 5
        self.gridLayout.addWidget(self.feta, 2, 0)
        self.feta.group = 1

        self.parmesan.price = 5
        self.gridLayout.addWidget(self.parmesan, 2, 1)
        self.parmesan.group = 1

        self.mozarella.price = 5
        self.gridLayout.addWidget(self.mozarella, 2, 2)
        self.mozarella.group = 1

        self.dor_blue.price = 5
        self.gridLayout.addWidget(self.dor_blue, 2, 3)
        self.dor_blue.group = 1

        self.edam.price = 5
        self.gridLayout.addWidget(self.edam, 2, 4)
        self.edam.group = 1

        self.brinza.price = 5
        self.gridLayout.addWidget(self.brinza, 2, 5)
        self.brinza.group = 1

        # Second row (Meat)
        self.bacon.price = 6
        self.gridLayout.addWidget(self.bacon, 3, 0)
        self.bacon.group = 2

        self.prosciutto.price = 6
        self.gridLayout.addWidget(self.prosciutto, 3, 1)
        self.prosciutto.group = 2

        self.salami.price = 6
        self.gridLayout.addWidget(self.salami, 3, 2)
        self.salami.group = 2

        self.chicken.price = 6
        self.gridLayout.addWidget(self.chicken, 3, 3)
        self.chicken.group = 2

        # Third row (Meat)
        self.fresh_mush.price = 7
        self.gridLayout.addWidget(self.fresh_mush, 4, 0)
        self.fresh_mush.group = 3

        self.smoc_mush.price = 7
        self.gridLayout.addWidget(self.smoc_mush, 4, 1)
        self.smoc_mush.group = 3

        self.onion.price = 7
        self.gridLayout.addWidget(self.onion, 4, 2)
        self.onion.group = 3

        self.tomato.price = 7
        self.gridLayout.addWidget(self.tomato, 4, 3)
        self.tomato.group = 3

        self.tomato.garlic = 7
        self.gridLayout.addWidget(self.tomato, 4, 4)
        self.garlic.group = 3

        self.rucola.price = 7
        self.gridLayout.addWidget(self.rucola, 4, 5)
        self.rucola.group = 3

        self.rucola.price = 7
        self.gridLayout.addWidget(self.mar_go, 4, 6)
        self.mar_go.group = 3

        self.corn.price = 7
        self.gridLayout.addWidget(self.corn, 4, 7)
        self.corn.group = 3

        self.corn.price = 7
        self.gridLayout.addWidget(self.parsley, 4, 8)
        self.parsley.group = 3

        self.ch_pepper.price = 7
        self.gridLayout.addWidget(self.ch_pepper, 4, 9)
        self.ch_pepper.group = 3

    def add_product(self,btn):
        first = [self.feta, self.parmesan, self.mozarella, self.dor_blue, self.edam, self.brinza]
        second = [self.bacon, self.prosciutto, self.salami, self.chicken]
        third = [self.fresh_mush, self.smoc_mush, self.onion, self.tomato, self.garlic, self.rucola, self.mar_go, self.corn, self.parsley, self.ch_pepper]
        # debug_trace()
        allow = True
        checked = 0
        if btn.group == 1:
            for button in first:
                if button.checkState() == 2:
                    checked += 1
                    if checked >= 4:
                        allow = False

        if btn.group == 2:
            for button in second:
                if button.checkState() == 2:
                    checked += 1
                    if checked >= 3:
                        allow = False

        if btn.group == 3:
            for button in third:
                if button.checkState() == 2:
                    checked += 1
                    if checked >= 6:
                        allow = False
                        
        if btn.checkState() == 2:
        # button checked
            if allow:
                self.price_update.setText(str(int(self.price_update.text())+btn.price)) 
            else:
                btn.setCheckState(0)
        else:
            self.price_update.setText(str(int(self.price_update.text())-btn.price)) 

        self.price_total = self.price_update.text()
        return

    def draw_step_three(self):
        self.clear_step_two()
        self.gridLayout.addWidget(self.finish_string_label,1, 0, 1, 1)
        self.finish_string_label.setText('%s you have to pay %s money units. Order ID: %s' % (self.user_name_input, self.price_total, randint(100, 999)))