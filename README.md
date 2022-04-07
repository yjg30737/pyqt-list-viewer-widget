# pyqt-list-viewer-widget
PyQt widget which consist two widgets: file list widget and viewer widget

## Requirements
* PyQt5 >= 5.8

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-file-list-widget.git --upgrade`

## Method Overview
* `setView(view)` - Set the view
* `setExtensions(extensions: list)` - Set the extensions you want to accept. ex) ['.txt', '.doc']
* `addDirectory(dirname: str, cur_filename: str = '')` - Add the files in `dirname` directory. Set `cur_filename` argument if you want to make list set current filename.
* `setDirectory(dirname: str, cur_filename: str = '')` - Clear the list and add the directory.
* `addFilenames(filenames: list, cur_filename: str = '')`
* `setFilenames(filenames: list, cur_filename: str = '')`
* `getListWidget()`
* `getViewerWidget()`
* `isAddAsDirectory() -> bool`
* `setAddAsDirectory(f: bool)`
* `setWindowTitleBasedOnCurrentFileEnabled(f: bool, prefix: str = '')`

## Included Packages
* <a href="https://github.com/yjg30737/simplePyQt5.git">simplePyQt5</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>
* <a href="https://github.com/yjg30737/pyqt-checkbox-file-list-widget.git">pyqt-checkbox-file-list-widget</a>
* <a href="https://github.com/yjg30737/pyqt-viewer-widget.git">pyqt-viewer-widget</a>
