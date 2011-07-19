import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import CMRS_ACADEMIC_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Test academic folder content type"""
    layer = CMRS_ACADEMIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('AcademicFolder', 'af1')
        af1 = getattr(self.portal, 'af1')
        assert 'af1' in self.portal.objectIds()
