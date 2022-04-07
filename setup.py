from setuptools import setup, find_packages

setup(
    name='pyqt-list-viewer-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_list_viewer_widget.ico': ['close.svg', 'remove.svg']},
    description='PyQt widget which consist of file list widget and viewer widget',
    url='https://github.com/yjg30737/pyqt-list-viewer-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'simplePyQt5 @ git+https://git@github.com/yjg30737/simplePyQt5.git@master',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main',
        'pyqt-checkbox-file-list-widget @ git+https://git@github.com/yjg30737/pyqt-checkbox-file-list-widget.git@main',
        'pyqt-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-viewer-widget.git@main'
    ]
)