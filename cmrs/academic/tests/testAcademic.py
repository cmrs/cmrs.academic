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

class TestSchema(unittest.TestCase):
    """Tes academic content type"""
    layer = CMRS_ACADEMIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('AcademicFolder', 'af1')
        self.af1 = getattr(self.portal, 'af1')

    def testAcademicName(self):
        self.af1.invokeFactory('Academic', 'a1')
        a1 = getattr(self.af1, 'a1')
        a1.setPersonalName('John')
        a1.setFamilyName('Smith')
        assert a1.getPersonalName() == 'John'
        assert a1.getFamilyName() == 'Smith'
        assert a1.getAcademicName() == 'John Smith'

    def testPostNominals(self):
        self.af1.invokeFactory('Academic', 'a1')
        a1 = getattr(self.af1, 'a1')
        a1.setPostNominals(['MA', 'PhD'])
        assert a1.getPostNominals() == ('MA', 'PhD'), a1.getPostNominals()

    def testJobTitle(self):
        self.af1.invokeFactory('Academic', 'a1')
        a1 = getattr(self.af1, 'a1')
        a1.setJobTitle('Academics job title')
        assert a1.getJobTitle() == ('Academics job title')
