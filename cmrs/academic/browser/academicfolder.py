from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class AcademicFolderView(BrowserView):  

    template = ViewPageTemplateFile('templates/academic_list.pt')

    def __call__(self):
        return self.template() 

    def getAcademics(self):
        """Return the academics as objects, sorted by family name
        """
        academics = self.context.getFolderContents(contentFilter={'portal_type':'Academic',
                                                                  'sort_on':'getObjPositionInParent'},
                                                   full_objects=True)
        return academics
