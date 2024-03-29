from setuptools import setup
import os
from glob import glob

package_name = 'drone_publish'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('../launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tayaran Drones',
    maintainer_email='vagrant@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "DroneTalker = drone_publish.DroneTalker:main",
            "DataFusionListener = drone_publish.DataFusionListener:main",
            "SampleService = drone_publish.SampleService:main",
            "DroneClient = drone_publish.DroneClient:main"
        ],
    },
)
