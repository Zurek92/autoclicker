from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    reqs = [req[:-1] if req.endswith('\n') else req for req in file.readlines()]

setup(
    name="autoclicker",
    version="0.1",
    packages=find_packages(),
    author='Dawid Żurawski',
    author_email='dawid.zurawski@protonmail.com',
    url='https://github.com/Zurek92/autoclicker',
    include_package_data=True,
    install_requires=reqs,
    entry_points={'console_scripts': ['autoclicker=autoclicker.main:autoclicker']}
)
