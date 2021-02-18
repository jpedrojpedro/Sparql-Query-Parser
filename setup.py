from setuptools import setup


setup(
    name='Sparql-Query-Parser',
    version='v0.0.1',
    description='SPARQL query parser to json',
    long_description='SPARQL query parser to json',
    license='Apache License 2.0',
    author='ZwEin27',
    url='https://github.com/jpedrojpedro/Sparql-Query-Parser',
    download_url='https://github.com/jpedrojpedro/Sparql-Query-Parser/releases',
    platforms=['any'],
    python_requires='>=3.8.2',
    packages=['sqparser'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['python', 'sparql', 'parser'],
    project_urls={
        'Home': 'https://github.com/jpedrojpedro/Sparql-Query-Parser',
    }
)
