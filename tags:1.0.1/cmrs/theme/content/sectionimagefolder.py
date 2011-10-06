from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType
from Products.CMFCore.utils import getToolByName

from cmrs.theme.config import PROJECTNAME
from cmrs.theme.interfaces.sectionimagefolder import ISectionImageFolder

from schemata import SectionImageFolderSchema

class SectionImageFolder(ATFolder):
    """A folder within a section for storing images"""

    security = ClassSecurityInfo()

    implements(ISectionImageFolder)

    meta_type = 'SectionImageFolder'
    _at_rename_after_creation = True

    schema = SectionImageFolderSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

registerType(SectionImageFolder, PROJECTNAME)
