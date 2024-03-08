from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros_dds_monitor'

setup(
    name='ros_dds_monitor',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='MikeDegany',
    maintainer_email="mike.degany@gmail.com",
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = ros_dds_monitor.publisher_member_function:main',
                'listener = ros_dds_monitor.subscriber_member_function:main',
                # 'monitor = ros_dds_monitor.launch:generate_launch_description'
        ],
    },
)
