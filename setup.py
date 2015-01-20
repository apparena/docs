from setuptools import setup, find_packages


setup(
    name='readthedocs',
    version="1.0",
    description='App-Arena App-Manager API',
    #long_description=readme,
    author='Sebastian Buckpesch',
    author_email='s.buckpesch@app-arena.com',
    url='http://www.app-arena.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
