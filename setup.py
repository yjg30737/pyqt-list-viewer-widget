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
        'simplePyQt5>=0.0.1',
        'pyqt-svg-button>=0.0.1',
        'pyqt-checkbox-file-list-widget>=0.0.1',
        'pyqt-viewer-widget>=0.0.1'
    ]
)