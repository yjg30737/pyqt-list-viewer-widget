# pyqt-list-viewer-widget
PyQt widget which consist two widgets: file list widget and viewer widget

## Requirements
* PyQt5 >= 5.8

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-file-list-widget.git --upgrade`

## Method Overview
* `setView(view)` - Set the view.
* `setExtensions(extensions: list)` - Set the extensions you want to accept. ex) ['.txt', '.doc']
* `addDirectory(dirname: str, cur_filename: str = '')` - Add the files in `dirname` directory. Set `cur_filename` argument if you want to make list set current filename.
* `setDirectory(dirname: str, cur_filename: str = '')` - Clear the list and add the directory.
* `addFilenames(filenames: list, cur_filename: str = '')`
* `setFilenames(filenames: list, cur_filename: str = '')`
* `getFileWidget()` - Return `FileWidget` on the left side of whole widget. 
* `getListWidget()` - Return `FileListWidget`, list widget containing files placed in the `FileWidget`)
* `getViewerWidget()` - Return `ViewerWidget` on the right side of whole widget.
* `setAddAsDirectory(f: bool)` - If this is set `True`, adding a file in certain directory is not only add the file itself, but also add the other files.
* `isAddAsDirectory() -> bool`
* `setWindowTitleBasedOnCurrentFileEnabled(f: bool, prefix: str = '')` - If this is set `True` and prefix is being set, window title's format is set like `Prefix - 1.png` -> `Prefix - 2.png` ...
* `setBottomWidgetVisible(f: bool)` - Toggle the visibility of bottom widget (navigation widget) of viewer widget.
* `getCurrentFilename() -> str`

## Included Packages
* <a href="https://github.com/yjg30737/simplePyQt5.git">simplePyQt5</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>
* <a href="https://github.com/yjg30737/pyqt-checkbox-file-list-widget.git">pyqt-checkbox-file-list-widget</a>
* <a href="https://github.com/yjg30737/pyqt-viewer-widget.git">pyqt-viewer-widget</a>

## App Included This Package
* <a href="https://github.com/yjg30737/pyqt-html-viewer">pyqt-html-viewer</a>
* <a href="https://github.com/yjg30737/pyqt-svg-viewer">pyqt-svg-viewer</a>
