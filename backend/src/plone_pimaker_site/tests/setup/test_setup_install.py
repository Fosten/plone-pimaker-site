from plone_pimaker_site import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if plone_pimaker_site is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IPLONE_PIMAKER_SITELayer is registered."""
        from plone_pimaker_site.interfaces import IPLONE_PIMAKER_SITELayer

        assert IPLONE_PIMAKER_SITELayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20230719001"
