from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

class AcademicView(BrowserView):  

    template = ViewPageTemplateFile('templates/academic_view.pt')

    def __call__(self):
        return self.template() 
