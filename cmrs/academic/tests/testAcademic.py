import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import CMRS_ACADEMIC_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Tes academic content type"""
    layer = CMRS_ACADEMIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('AcademicFolder', 'af1')
        af1 = getattr(self.portal, 'af1')
        af1.invokeFactory('Academic', 'a1')
        assert 'a1' in af1.objectIds()
