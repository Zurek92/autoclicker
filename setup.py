from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    reqs = [req[:-1] if req.endswith('\n') else req for req in file.readlines()]

setup(
    name="autoclicker",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    entry_points={'console_scripts': ['autoclicker=autoclicker.main:autoclicker']}
)
