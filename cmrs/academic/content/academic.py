from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

from cmrs.academic.config import PROJECTNAME
from cmrs.academic.interfaces.academic import IAcademic

from schemata import AcademicSchema

class Academic(ATCTContent):
    """An Academic"""

    security = ClassSecurityInfo()

    implements(IAcademic)

    meta_type = 'Academic'
    _at_rename_after_creation = True

    schema = AcademicSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

    security.declarePublic('getAcademicName')
    def getAcademicName(self):
        name = self.getPersonalName() + ' ' + self.getFamilyName()
        return name

    security.declarePublic('Title')
    def Title(self):
        pre_nominal = self.getPreNominal()
        if pre_nominal:
            name = pre_nominal + ' '
        else:
            name = ''
        name = name + self.getPersonalName() + ' ' + self.getFamilyName()
        post_nominals = self.getPostNominals()
        for post_nominal in post_nominals:
            name = name + ' ' + post_nominal + ','
        if name[-1:] == ',':
            name = name[:-1]
        return name

registerType(Academic, PROJECTNAME)
