from Acquisition import aq_inner
from random import choice
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _

from cmrs.theme.interfaces import ISectionImagePortlet

class Assignment(base.Assignment):
    implements(ISectionImagePortlet)

    def __init__(self, interval=10):
        self.interval = interval

    @property
    def title(self):
        return _(u"Section Image Carousel")

class AddForm(base.AddForm):
    form_fields = form.Fields(ISectionImagePortlet)
    label = _(u"Add Section Image Carousel Portlet")
    description = _(u"This portlet displays images in a carousel.")

    def create(self, data):
        return Assignment(interval=data.get('interval', 5))

class EditForm(base.EditForm):
    form_fields = form.Fields(ISectionImagePortlet)
    label = _(u"Add Section Image Carousel Portlet")
    description = _(u"This portlet displays images in a carousel.")

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        self.anonymous = portal_state.anonymous()  # whether or not the current user is Anonymous
        self.portal_url = portal_state.portal_url()  # the URL of the portal object
        
    def render(self):
        return self._template()

    def getRandomImages(self):
        """Get up to two random images"""
        try:
            section_folder = self.context.getSectionFolder()
        except AttributeError:
            # we are not within a section folder so return
            section_folder = None
        if self.context.portal_type == 'HomePage':
            # if we are the homepage, get the portal root
            section_folder = getToolByName(self.context, 'portal_url').getPortalObject()
        if not section_folder:
            return
        folder = section_folder.getFolderContents({'portal_type':'SectionImageFolder'})
        if not folder:
            return
        folder = folder[0].getObject()
        folder_images = folder.getFolderContents({'portal_type':'SectionImage',})
        if not folder_images:
            return
        results = []
        if len(folder_images) < 3:
            for image in folder_images:
                results.append(image.getObject())
            return results
        results.append(choice(folder_images).getObject())
        results.append(choice(folder_images).getObject())
        while results[0] == results[1]:
            results[1] = choice(folder_images).getObject()
        return results
