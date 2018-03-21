# setup.py es un archivo necesario para publicar el proyecto
# y después usarlo con pip.
# Referencia: https://packaging.python.org/tutorials/distributing-packages/#setup-args

from setuptools import setup

setup(name="tec.ic.ia.pc1.g01",
      description="Inteligencia Artificial: Proyecto Corto I",
      long_description="Generador de datos según el Estado de la Nación",
      version="0.1.0",
      author="Julian Salinas, Brandon Dinarte, Armando López",
      license="GNU General Public License v3.0",
      keywords=['tec', 'ic', 'ia', "g01"],
      url='https://github.com/bdinarte/SimuladorVotantes',
      download_url="https://github.com/JulianSalinas/Sliding_Puzzle/tree/master/tec/",
      install_requires=['pandas'],
      python_requires='>=3',
      include_package_data=True,
      package_data={"": ["*.txt", "*.csv", ".xlsx"]}
      )
