from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType
from Products.CMFCore.utils import getToolByName

from cmrs.theme.config import PROJECTNAME
from cmrs.theme.interfaces.sectionfolder import ISectionFolder

from schemata import SectionFolderSchema

class SectionFolder(ATFolder):
    """A top level section folder"""

    security = ClassSecurityInfo()

    implements(ISectionFolder)

    meta_type = 'SectionFolder'
    _at_rename_after_creation = True

    schema = SectionFolderSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

    security.declarePublic('getSectionFolder')
    def getSectionFolder(self):
        return self

registerType(SectionFolder, PROJECTNAME)
