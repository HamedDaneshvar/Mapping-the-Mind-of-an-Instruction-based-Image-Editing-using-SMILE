from setuptools import setup, find_packages

setup(name='iie_smile',
      version='0.0.0.1',
      description='Mapping the Mind of an Instruction-based Image Editing using SMILE',
      url='https://github.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE',
      author='Zeinab Dehghani (Corresponding), Koorosh Aslansefat, Adil Khan, Adín Ramírez Rivera, Franky Geotge, Muhammad Khalid',
      author_email='Z.DEHGHANI-2023@hull.ac.uk',
      license='BSD',
      packages=find_packages(exclude=['js', 'node_modules', 'tests']),
      python_requires='>=3.5',
      install_requires=[
          'matplotlib',
          'numpy',
          'scipy',
          'tqdm >= 4.29.1',
          'scikit-learn>=0.18',
          'scikit-image>=0.12',
          'pyDOE2==1.3.0',
          'twine==1.13.0'
      ],
      extras_require={
          'dev': ['pytest', 'flake8'],
      },
      include_package_data=True,
      zip_safe=False)
