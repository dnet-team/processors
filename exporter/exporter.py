# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from . import translators


# Module API

class Exporter(object):

    # Public

    def __init__(self, warehouse, database):
        self.__warehouse = warehouse
        self.__database = database

    def export(self, translator):
        translator = getattr(translators, translator.capitalize())(
            self.__warehouse, self.__database)
        translator.translate()
