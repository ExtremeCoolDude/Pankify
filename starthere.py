#!/usr/bin/python

from guii import *
import guii

def main():
    app = QApplication(sys.argv)
    pankify = GUILazy()
    pankify.show()
    sys.exit (app.exec_())

if __name__ == '__main__':
    main()