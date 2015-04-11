from setuptools import setup

setup(name='SuiteGenerator',
      version='0.1',
      description='Shim for translating things',
      author='Mark Rothlisberger',
      author_email='rothlmar@gmail.com',
      url='http://suites-votech.rhcloud.com/',
      install_requires=['flask>0.10'],
      packages = ['suitetester']
      package_data = {'suitetester': ['templates/*.html', 'static/*']}
     )
