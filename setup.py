import setuptools

with open('README.md', 'r') as fh:
  long_desc = fh.read()

setuptools.setup(
  name                          = 'Ittigorn',
  version                       = '0.0.1',
  auther                        = 'Ittigorn Tradussadee',
  auther_email                  = 'ittigorn.tra@gmail.com',
  description                   = 'My helper classes library',
  long_description              = long_desc,
  long_description_content_type = 'text/markdown',
  url                           = 'https://github.com/ittigorn-tra/Ittigorn',
  packages                      = setuptools.find_packages(),
  classifiers                   = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT license',
    'Operating Systems :: OS Independent',
  ],
  python_requires               = '>=3.7',
)