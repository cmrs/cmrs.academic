from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

from cmrs.academic.config import PROJECTNAME
from cmrs.academic.interfaces.academic import IAcademic

from schemata import AcademicSchema

class Academic(ATNewsItem):
    """An Academic"""

    security = ClassSecurityInfo()

    implements(IAcademic)

    meta_type = 'Academic'
    _at_rename_after_creation = True

    schema = AcademicSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

registerType(Academic, PROJECTNAME)
