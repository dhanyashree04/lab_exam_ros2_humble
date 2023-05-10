from setuptools import setup
import os
from glob import glob


package_name = 'my_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name), glob('urdf/*')),
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
            'move=my_bot.move:main',
            'test=my_bot.test:main',
            'road=my_bot.road:main',
            'road_follow=my_bot.road_follow:main'
        ],
    },
)
