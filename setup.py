from distutils.core import setup
setup(
  name = 'discordtools',         
  packages = ['discordtools'],   
  version = '1.0',      
  license='MIT',
  description = 'A libary that installs all discord related python packages',
  author = 'DarthOCE',                   
  author_email = 'darthocelogging@gmail.com',
  url = 'https://github.com/darthoce/discordtools',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['discordbuttons', 'slashcommand', 'discord'],
  install_requires=[            
          'discord',
          'discord_components',
          'discord-py-slash-command'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)