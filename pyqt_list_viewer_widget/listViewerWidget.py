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
        self.__fileListWidget = FileWidget()
        self.__fileListWidget.showSignal.connect(self.__showFileToViewer)
        self.__fileListWidget.removeSignal.connect(self.__removeSomeFilesFromViewer)

        self.__fileListWidget.showSignal.connect(self.showSignal)
        self.__fileListWidget.removeSignal.connect(self.removeSignal)
        self.__fileListWidget.closeSignal.connect(self.closeListSignal)

        self.__viewerWidget = ViewerWidget()
        self.__viewerWidget.prevSignal.connect(self.__selectCurrentFileItemInList)
        self.__viewerWidget.nextSignal.connect(self.__selectCurrentFileItemInList)

        self.__viewerWidget.prevSignal.connect(self.prevSignal)
        self.__viewerWidget.nextSignal.connect(self.nextSignal)
        self.__viewerWidget.closeSignal.connect(self.closeViewerSignal)

        splitter = QSplitter()
        splitter.addWidget(self.__fileListWidget)
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

    def setExtensions(self, extensions: list):
        self.__extensions = extensions
        self.__viewerWidget.setExtensionsExceptForImage(extensions)
        self.__fileListWidget.setExtensions(extensions)

    def setDirectory(self, dirname: str, cur_filename: str = ''):
        self.addDirectory(dirname, cur_filename)

    def addDirectory(self, dirname: str, cur_filename: str = ''):
        filenames = [os.path.join(dirname, filename).replace(os.path.sep, posixpath.sep) for filename in
                     os.listdir(dirname)]
        self.addFilenames(filenames, cur_filename)

    def setFilenames(self, filenames: list, cur_filename: str = ''):
        cur_filename = filenames[0] if cur_filename == '' else cur_filename
        self.__viewerWidget.setFilenames(filenames, cur_filename)
        self.__fileListWidget.setFilenames(filenames, cur_filename)

    def addFilenames(self, filenames: list, cur_filename: str = ''):
        cur_filename = filenames[0] if cur_filename == '' else cur_filename
        self.__viewerWidget.addFilenames(filenames, cur_filename)
        self.__fileListWidget.addFilenames(filenames, cur_filename)

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