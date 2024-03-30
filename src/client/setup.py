from setuptools import find_packages, setup

package_name = 'client'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sudhindra',
    maintainer_email='sudhindrasahoo2005@gmail.com',
    description='Detecting and identifying aruco markers',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client_execuatble = client.client_member_function:main'
        ],
    },
)
