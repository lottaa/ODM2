__author__ = 'Stephanie'

import sys
import os

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(this_file))))
sys.path.insert(0, directory)

from ODM2 import serviceBase
import ODM2.ExtensionProperties.model as m
from ODMconnection import SessionFactory



class deleteExtensionProperties (serviceBase):
   def test(self):
        return None