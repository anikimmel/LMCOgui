from setuptools import setup

setup(name='GenManDemoGUI',
      version='0.3',
      description='Demo LMCO Generative Manufacturing Graphical User Interface',
      url='https://github.com/anikimmel/LMCOgui',
      author='CMU',
      author_email='akimmel@andrew.cmu.edu',
      license='MIT',
      packages=['Objects', 'Utility', 'ExampleCode'],
      install_requires=[
          'PySimpleGUI'
      ],
      zip_safe=False)
