from setuptools import setup, find_packages


CLASSIFIERS = [
]


entry_points = {
    'console_scripts': [
        'hackercafe=hackercafe.main:main'
    ]
}


install_requires = [
]

tests_require = [
]


setup(
    name="hackercafe",
    version='1.0.1',
    description='Python client for HackerCafe',
    url='https://www.hackerearth.com',
    author='Sreeram Boyapati',
    author_email='sreeram@hackerearth.com',
    license='MIT',
    packages=find_packages(),
    keywords=['hackerarth', 'hackercafe'],
    classifiers=CLASSIFIERS,
    zip_safe=True,
    include_package_data=True,
    entry_points=entry_points,
    install_requires=install_requires,
)
