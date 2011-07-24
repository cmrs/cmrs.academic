from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class AcademicFolderView(BrowserView):  

    template = ViewPageTemplateFile('templates/academic_list.pt')

    def __call__(self):
        return self.template() 

    def tag(self):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.context.Title()
        if 'scale' not in kwargs:
            kwargs['scale'] = 'mini'
        return self.context.getField('academicPortrait').tag(self.context, **kwargs)

    def getAcademics(self):
        """Return the academics as objects, sorted by family name
        """
        academics = self.context.getFolderContents(contentFilter={'portal_type':'Academic',
                                                                  'sort_on':'sortable_title'},
                                                   full_objects=True)
        return academics
