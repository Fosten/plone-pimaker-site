"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "plone_pimaker_site"

_ = MessageFactory("plone_pimaker_site")

logger = logging.getLogger("plone_pimaker_site")
