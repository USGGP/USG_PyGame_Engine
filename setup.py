from setuptools import setup

setup(
  [
    name='usg_pygame_engine',
    version='0.0.1',
    description='usg simple engine for create pygame',
    url='git@github.com:Naptwen/USG_PyGame_Engine.git',
    author='useop gim',
    author_email='please contact me via git',
    license='GNU Affero v3',
    packages=['usg_game_pack'],
    zip_safe=False,
    install_requires=[
      PySimpleGUI >= 3.0.0
      pygame >= 2.0.0
      pandas >= 1.0.0
      numpy >= 1.0.0
  ]
)
