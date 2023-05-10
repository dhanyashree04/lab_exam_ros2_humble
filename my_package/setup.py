from setuptools import setup
import os 
from glob import glob 


package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
     (os.path.join('share', package_name), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhanyashree',
    maintainer_email='dhanyashree@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            'sample = my_package.sample:main',
            'publisher= my_package.publisher:main',
            'subscriber= my_package.subscriber:main',
            'control= my_package.turtle_controller:main',
            'three_node= my_package.three_node:main',
            'turtle_circle= my_package.turtle_circle:main',
            'turtle_triangle= my_package.turtle_triangle:main',
            'turtle_spawn= my_package.turtle_spawn:main',
            'turtle_kill= my_package.turtle_kill:main'
            
            
        ],
    },
)
