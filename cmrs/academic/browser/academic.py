from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AcademicView(BrowserView):  

    template = ViewPageTemplateFile('templates/academic_view.pt')

    def __call__(self):
        return self.template() 

    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.context.Title()
        if 'scale' not in kwargs:
            kwargs['scale'] = 'mini'
        return self.context.getField('academicPortrait').tag(self.context, **kwargs)
