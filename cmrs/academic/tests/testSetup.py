import time
import unittest2 as unittest
from zExceptions import BadRequest

from zope.component import getSiteManager

from Products.CMFCore.utils import getToolByName

from base import CMRS_ACADEMIC_INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = CMRS_ACADEMIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testTypesInstalled(self):
        portal_types = getToolByName(self.portal, 'portal_types')
        assert 'AcademicFolder' in portal_types.objectIds(), portal_types.objectIds()
        assert 'Academic' in portal_types.objectIds(), portal_types.objectIds()

    def testCatalogIndexesAdded(self):
        catalog = self.portal.portal_catalog
        assert 'family_name' in catalog.indexes()

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = CMRS_ACADEMIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        try:
            portal_setup.runAllImportStepsFromProfile('profile-cmrs.academic:default')
        except BadRequest:
            # if tests run too fast, duplicate profile import id makes test fail
            time.sleep(0.5)
            portal_setup.runAllImportStepsFromProfile('profile-cmrs.academic:default')
