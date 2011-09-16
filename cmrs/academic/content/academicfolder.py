from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType

from cmrs.academic.config import PROJECTNAME
from cmrs.academic.interfaces.academicfolder import IAcademicFolder

from schemata import AcademicFolderSchema

class AcademicFolder(ATFolder):
    """Folder to contain academic objects"""

    security = ClassSecurityInfo()

    implements(IAcademicFolder)

    meta_type = 'AcademicFolder'
    _at_rename_after_creation = True

    schema = AcademicFolderSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

    security.declarePublic('getSectionFolder')
    def getSectionFolder(self):
        return self

registerType(AcademicFolder, PROJECTNAME)
