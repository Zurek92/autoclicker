from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    reqs = [req[:-1] if req.endswith('\n') else req for req in file.readlines()]

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name="autoclicker",
    version="0.2",
    packages=find_packages(),
    author='Dawid Żurawski',
    author_email='dawid.zurawski@protonmail.com',
    url='https://github.com/Zurek92/autoclicker',
    include_package_data=True,
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'autoclicker=autoclicker.main:autoclicker',
            'aclk=autoclicker.main:autoclicker',
        ]
    },
    description='A simple project to auto control mouse.',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
