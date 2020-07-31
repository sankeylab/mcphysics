__version__ = '1.3.3' # Keep this on the first line



from distutils.core import setup
setup(name           = 'McPhysics',
      version        = __version__,
      description    = 'Useful tools for the McGill Undergraduate Physics Labs',
      author         = 'Jack Sankey',
      author_email   = 'jack.sankey@gmail.com',
      url            = 'https://github.com/sankeylab/mcphysics',
      packages       = ['mcphysics'],
      package_dir    = {'mcphysics' : '.'}
     )
