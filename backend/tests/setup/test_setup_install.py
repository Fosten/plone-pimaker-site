from plone.pimaker_site import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if plone.pimaker_site is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IBrowserLayer is registered."""
        from plone.pimaker_site.interfaces import IBrowserLayer

        assert IBrowserLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "1000"
