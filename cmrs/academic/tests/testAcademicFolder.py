from Acquisition import aq_inner
import unittest2 as unittest
from zope.component import getMultiAdapter

from plone.app.customerize import registration
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView as View

from cmrs.academic.interfaces.academicfolder import IAcademicFolder

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

class TestView(unittest.TestCase):
    """Test the view for academic folder content type"""
    layer = CMRS_ACADEMIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('AcademicFolder', 'af1')
        self.af1 = getattr(self.portal, 'af1')

    def testGetAcademicsReturnsNone(self):
        """ looking up and updating the manager should list our viewlet
        """
        af1 = self.af1
        view = getMultiAdapter((aq_inner(af1), self.portal.REQUEST), name='academic_list')
        view = view.__of__(af1)
        assert view.getAcademics() == []

    def testGetAcademicsReturnNone(self):
        """ looking up and updating the manager should list our viewlet
        """
        af1 = self.af1
        af1.invokeFactory('Academic', 'a1')
        view = getMultiAdapter((aq_inner(af1), self.portal.REQUEST), name='academic_list')
        view = view.__of__(af1)
        academics = view.getAcademics()
        assert len(academics) == 1
