from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

class TestCase(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import oxford.testimonial
        self.loadZCML(package=oxford.testimonial)
        import oxford.homepage
        self.loadZCML(package=oxford.homepage)
        import keble.layout
        self.loadZCML(package=keble.layout)
        import cmrs.academic
        self.loadZCML(package=cmrs.academic)
        import cmrs.course
        self.loadZCML(package=cmrs.course)
        import cmrs.theme
        self.loadZCML(package=cmrs.theme)

        # Install product and call its initialize() function
        z2.installProduct(app, 'oxford.testimonial')
        z2.installProduct(app, 'oxford.homepage')
        z2.installProduct(app, 'keble.layout')
        z2.installProduct(app, 'cmrs.academic')
        z2.installProduct(app, 'cmrs.course')
        z2.installProduct(app, 'cmrs.theme')

        # Note: you can skip this if my.product is not a Zope 2-style
        # product, i.e. it is not in the Products.* namespace and it
        # does not have a <five:registerPackage /> directive in its
        # configure.zcml.

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'cmrs.theme:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'cmrs.theme')

        # Note: Again, you can skip this if my.product is not a Zope 2-
        # style product

CMRS_THEME_FIXTURE = TestCase()
CMRS_THEME_INTEGRATION_TESTING = IntegrationTesting(bases=(CMRS_THEME_FIXTURE,), name="CmrsTheme:Integration")
