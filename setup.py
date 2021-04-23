import setuptools


setuptools.setup(
    name='lunar_test',
    version='0.0.5',
    author='RimoChan',
    author_email='the@librian.net',
    description='lunar_test',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/lunar-Ci',
    packages=['lunar_test'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'lunar-python>=1.0.29',
    ],
    python_requires='>=3.6',
)
