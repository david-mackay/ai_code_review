from setuptools import setup, find_packages

setup(
    name='name_of_product',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'name_of_product = name_of_product.entry_points.main:main'
        ]
    }
)