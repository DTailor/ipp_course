import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

import app


class AppTest(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.app = QApplication(sys.argv)
        self.form = app.App()

    def test_defaults_step_one(self):
        self.assertEqual(self.form.windowTitle(), 'App Title')
        self.assertEqual(self.form.ui.name_input_label.text(), 'Your Name')
        self.assertEqual(self.form.ui.name_input.text(), '')


if __name__ == "__main__":
    unittest.main()
