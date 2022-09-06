from setuptools import setup

setup(name='GenManDemoGUI',
      version='0.1',
      description='Demo LMCO Generative Manufacturing Graphical User Interface',
      url='https://github.com/anikimmel/LMCOgui',
      author='CMU',
      author_email='akimmel@andrew.cmu.edu',
      license='MIT',
      packages=['LMCOgui'],
      install_requires=[
          'json',
          'subprocess',
          'math',
          'PySimpleGUI',
          'os',
          'requests'
      ],
      zip_safe=False)