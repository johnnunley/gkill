# This file is part of gkill.
# 
# gkill is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# gkill is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with gkill.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MainWindow(QWidget):
  def __init__(self):
    super(MainWindow,self).__init__()
    self.init_ui()
  def init_ui(self):
    mainTable = QTableWidget()
    
    stopButton = QPushButton("Stop Process")
    killButton = QPushButton("Kill Process")
    pauseButton = QPushButton("Pause Process")
    buttonbox = QHBoxLayout()
    buttonbox.addWidget(stopButton)
    buttonbox.addWidget(killButton)
    buttonbox.addWidget(pauseButton)   

    vbox =  QVBoxLayout()
    vbox.addWidget(mainTable)
    vbox.addLayout(buttonbox)

    self.setLayout(vbox)
    self.setWindowTitle("gkill")
    self.show()

def main():
  qapp = QApplication(sys.argv)
  window = MainWindow()
  return qapp.exec_()

if __name__  == '__main__':
  main()
