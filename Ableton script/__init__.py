# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live
from K16 import K16

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return K16(c_instance)


# local variables:
# tab-width: 4
