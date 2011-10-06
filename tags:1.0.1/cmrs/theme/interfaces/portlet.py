from zope.schema import Int

from plone.portlets.interfaces import IPortletDataProvider

from Products.CMFPlone import PloneMessageFactory as _

class ISectionImagePortlet(IPortletDataProvider):

    interval = Int(title=_(u'Change Interval'),
                       description=_(u'Number of seconds between image changes.'),
                       required=True,
                       default=10)
