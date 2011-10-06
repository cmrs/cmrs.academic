import transaction
from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.image import ATImage
from Products.ATContentTypes.content.image import ATImage
from Products.CMFCore import permissions
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from cmrs.theme.config import PROJECTNAME
from cmrs.theme.interfaces.sectionimage import ISectionImage

from schemata import SectionImageSchema

class SectionImage(ATImage):
    """An image for a section"""

    security = ClassSecurityInfo()

    implements(ISectionImage)

    meta_type = 'SectionImage'
    _at_rename_after_creation = True

    schema = SectionImageSchema

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)

registerType(SectionImage, PROJECTNAME)
