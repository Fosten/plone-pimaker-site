from plone_pimaker_site.testing import PLONE_PIMAKER_SITE_INTEGRATION_TESTING
from pytest_plone import fixtures_factory


pytest_plugins = ["pytest_plone"]


globals().update(fixtures_factory(((PLONE_PIMAKER_SITE_INTEGRATION_TESTING, "integration"),)))
