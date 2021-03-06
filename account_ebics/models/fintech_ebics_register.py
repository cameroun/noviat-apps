# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
try:
    import fintech
except ImportError:
    fintech = None
    logging.debug('Failed to import fintech')
from sys import exc_info
from traceback import format_exception

from odoo.tools import config

_logger = logging.getLogger(__name__)

fintech_register_name = config.get('fintech_register_name')
fintech_register_keycode = config.get('fintech_register_keycode')
fintech_register_users = config.get('fintech_register_users')

try:
    if fintech:
        fintech.cryptolib = 'cryptography'
        fintech.register(
            fintech_register_name,
            fintech_register_keycode,
            fintech_register_users)
except RuntimeError, e:
    if e.message == "'register' can be called only once":
        pass
    else:
        _logger.error(e.message)
        fintech.register()
except:
    msg = "fintech.register error"
    tb = ''.join(format_exception(*exc_info()))
    msg += '\n%s' % tb
    _logger.error(msg)
    fintech.register()
