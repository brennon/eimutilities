__author__ = 'Brennon Bortz'

import unittest
import doctest
import os

files = []
root_dir = 'eim/'

for root, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == '__init__.py' or filename[-3:] != '.py':
            continue
        f = os.path.join(root, filename)
        f = f.replace('/', '.')
        f = f[:-3]
        files.append(f)

suite = unittest.TestSuite()
for module in files:
    suite.addTest(doctest.DocTestSuite(module))
unittest.TextTestRunner(verbosity=5).run(suite)
