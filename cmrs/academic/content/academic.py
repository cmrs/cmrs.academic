import transaction
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

    security.declarePrivate('_renameAfterCreation')
    def _renameAfterCreation(self, check_auto_id=False):
        plone_tool = getToolByName(self, 'plone_utils', None)
        # Can't rename without a subtransaction commit when using
        # portal_factory!
        transaction.savepoint(optimistic = True)
        new_id = self.getAcademicName()
        new_id = plone_tool.normalizeString(new_id)
        if new_id in self.aq_parent.objectIds():
            new_id = self.getFamilyName()
            plone_tool.normalizeString(new_id)
        self.setId(new_id)

    security.declarePrivate('at_post_create_script')
    def at_post_edit_script(self):
        self._renameAfterCreation()

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

    security.declarePublic('Description')
    def Description(self):
        return self.getJobTitle()

    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.Title()
        if 'scale' not in kwargs:
            kwargs['scale'] = 'mini'
        return self.getField('academicPortrait').tag(self, **kwargs)

registerType(Academic, PROJECTNAME)
