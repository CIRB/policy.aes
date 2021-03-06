from setuptools import setup, find_packages
import os

version = '1.0.4.dev0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='policy.aes',
      version=version,
      description="'policy of Activites ExtraScolaires site'",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['policy', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plonetheme.acuccle',
          'collective.ckeditor',
          'quintagroup.analytics',
          'collective.easyslider',
          'Products.CMFPlomino',
          'Products.TinyMCE',
          'plomino.tinymce',
          'collective.js.datatables',
          'Products.PloneFormGen',
          'collective.gallery',
          'collective.recaptcha',
          'Solgema.fullcalendar',
          #'wildcard.fixpersistentutilities'
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
