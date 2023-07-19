from plone_pimaker_site import PACKAGE_NAME

import pytest


class TestSetupUninstall:
    @pytest.fixture(autouse=True)
    def uninstalled(self, installer):
        installer.uninstall_product(PACKAGE_NAME)

    def test_product_uninstalled(self, installer):
        """Test if plone_pimaker_site is cleanly uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False

    def test_browserlayer_removed(self, browser_layers):
        """Test that ICaseStudyLayer is removed."""
        from plone_pimaker_site.interfaces import IPLONE_PIMAKER_SITELayer

        assert IPLONE_PIMAKER_SITELayer not in browser_layers
