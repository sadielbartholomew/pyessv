# -*- coding: utf-8 -*-
"""
.. module:: pyessv.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Python Earth Science Standard Vocabulary library intializer.

.. moduleauthor:: IPSL (ES-DOC) <dev@esdocumentation.org>

"""
from pyessv._archive import load
from pyessv._archive import save

from pyessv._constants import DIR_ARCHIVE
from pyessv._constants import ENCODING_DICT
from pyessv._constants import ENCODING_JSON
from pyessv._constants import ENTITY_TYPE_AUTHORITY
from pyessv._constants import ENTITY_TYPE_COLLECTION
from pyessv._constants import ENTITY_TYPE_SCOPE
from pyessv._constants import ENTITY_TYPE_TERM
from pyessv._constants import GOVERNANCE_STATUS_ACCEPTED
from pyessv._constants import GOVERNANCE_STATUS_DEPRECATED
from pyessv._constants import GOVERNANCE_STATUS_PENDING
from pyessv._constants import GOVERNANCE_STATUS_REJECTED

from pyessv._exceptions import ParsingError
from pyessv._exceptions import ValidationError
from pyessv._exceptions import InvalidAssociationError

from pyessv._factory import create_authority
from pyessv._factory import create_collection
from pyessv._factory import create_scope
from pyessv._factory import create_term

from pyessv._model import Authority
from pyessv._model import Collection
from pyessv._model import Scope
from pyessv._model import Term

from pyessv._parser import parse
from pyessv._parser import parse_namespace

from pyessv._validation import get_errors
from pyessv._validation import is_valid
from pyessv._validation import validate_entity as validate



# Auto-initialize.
from pyessv import _initializer
_initializer.init()
