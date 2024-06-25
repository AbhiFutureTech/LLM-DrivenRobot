from setuptools import setup, find_packages

setup(
    name='Robotics',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license=open('LICENSE').read(),
    zip_safe=False,
    description="Robotic Tasks via Large Language Models.",
    author='Abhijit Patil',
    author_email='abhianantapatil@gmail.com',
    url='https://github.com/patilabhi20/Robotic-Tasks-via-Large-Language-Models',
   #  install_requires=[line for line in open('requirements.txt').readlines() if "@" not in line],
    keywords=['Large Language Models', 'Simulation', 'Vision Language Grounding', 'Robotics', 'Manipulation'],
)
