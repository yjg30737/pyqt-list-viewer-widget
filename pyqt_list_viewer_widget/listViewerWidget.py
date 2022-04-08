import os, posixpath

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QSplitter, QHBoxLayout
from pyqt_viewer_widget import ViewerWidget

from pyqt_list_viewer_widget.fileWidget import FileWidget


class ListViewerWidget(QWidget):
    prevSignal = pyqtSignal()
    nextSignal = pyqtSignal()
    closeViewerSignal = pyqtSignal()

    showSignal = pyqtSignal(str)
    removeSignal = pyqtSignal(list)
    closeListSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__addAsDirectory = False

    def __initUi(self):
        self.__fileWidget = FileWidget()
        self.__fileWidget.showSignal.connect(self.__showFileToViewer)
        self.__fileWidget.removeSignal.connect(self.__removeSomeFilesFromViewer)

        self.__fileWidget.showSignal.connect(self.showSignal)
        self.__fileWidget.removeSignal.connect(self.removeSignal)
        self.__fileWidget.closeSignal.connect(self.closeListSignal)

        self.__fileListWidget = self.__fileWidget.getListWidget()

        self.__viewerWidget = ViewerWidget()
        self.__viewerWidget.prevSignal.connect(self.__selectCurrentFileItemInList)
        self.__viewerWidget.nextSignal.connect(self.__selectCurrentFileItemInList)

        self.__viewerWidget.prevSignal.connect(self.prevSignal)
        self.__viewerWidget.nextSignal.connect(self.nextSignal)
        self.__viewerWidget.closeSignal.connect(self.closeViewerSignal)

        splitter = QSplitter()
        splitter.addWidget(self.__fileWidget)
        splitter.addWidget(self.__viewerWidget)
        splitter.setSizes([200, 400])

        lay = QHBoxLayout()
        lay.addWidget(splitter)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def __selectCurrentFileItemInList(self):
        idx = self.__viewerWidget.getCurrentIndex()
        self.__fileListWidget.setCurrentItem(idx)
        self.__viewerWidget.setFocus()

    def __showFileToViewer(self, filename: str):
        self.__viewerWidget.setCurrentFilename(filename)

    def __removeSomeFilesFromViewer(self, filenames: list):
        self.__viewerWidget.removeSomeFilesFromViewer(filenames)
        self.__selectCurrentFileItemInList()

    def setView(self, view):
        self.__viewerWidget.setView(view)

    def setExtensions(self, extensions: list):
        self.__extensions = extensions
        self.__viewerWidget.setExtensions(extensions)
        self.__fileListWidget.setExtensions(extensions)

    def setDirectory(self, dirname: str, cur_filename: str = ''):
        self.__viewerWidget.setDirectory(dirname, cur_filename)
        self.__fileListWidget.setDirectory(dirname, cur_filename)

    def addDirectory(self, dirname: str, cur_filename: str = ''):
        self.__viewerWidget.addDirectory(dirname, cur_filename)
        self.__fileListWidget.addDirectory(dirname, cur_filename)

    def setFilenames(self, filenames: list, cur_filename: str = ''):
        self.__viewerWidget.setFilenames(filenames, cur_filename)
        self.__fileListWidget.setFilenames(filenames, cur_filename)

    def addFilenames(self, filenames: list, cur_filename: str = ''):
        self.__viewerWidget.addFilenames(filenames, cur_filename)
        self.__fileListWidget.addFilenames(filenames, cur_filename)

    def getFileWidget(self):
        return self.__fileWidget

    def getListWidget(self):
        return self.__fileListWidget

    def getViewerWidget(self):
        return self.__viewerWidget

    def isAddAsDirectory(self) -> bool:
        return self.__addAsDirectory

    def setAddAsDirectory(self, f: bool):
        self.__addAsDirectory = f

    def setWindowTitleBasedOnCurrentFileEnabled(self, f: bool, prefix: str = ''):
        self.__viewerWidget.setWindowTitleBasedOnCurrentFileEnabled(f, prefix)