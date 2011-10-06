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
from cmrs.theme.interfaces.bannerimage import IBannerImage

from schemata import BannerImageSchema

class BannerImage(ATImage):
    """An image for the banner"""

    security = ClassSecurityInfo()

    implements(IBannerImage)

    meta_type = 'BannerImage'
    _at_rename_after_creation = True

    schema = BannerImageSchema

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)

registerType(BannerImage, PROJECTNAME)
