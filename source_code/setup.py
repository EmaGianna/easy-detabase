import setuptools

setuptools.setup(name='easy-detabase',
                 version='1.0',
                 description='easy-detabase interact with deta base service',
                 url='https://github.com/EmaGianna/easy-detabase',
                 author='Emanuel Giannattasio',
                 install_requires=['deta','pandas'],
                 author_email='',
                 packages=setuptools.find_packages(),
                 zip_safe=False)