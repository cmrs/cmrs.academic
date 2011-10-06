from zope.component import getMultiAdapter

from Acquisition import aq_inner

from plone.app.layout.navigation.root import getNavigationRoot

from Products.CMFPlone import utils
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.browser.navigation import get_view_url
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class GlobalSectionsViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/cmrs_sections.pt')

    def update(self):
        context = aq_inner(self.context)
        portal_tabs_view = getMultiAdapter((context, self.request),
                                           name='portal_tabs_view')
        portal_tabs = portal_tabs_view.topLevelTabs()
        self.portal_tabs = portal_tabs[:1]
        query = {}
        rootPath = getNavigationRoot(context)
        query['path'] = {'query' : rootPath, 'depth' : 1}
        query['portal_type'] = ['SectionFolder', 'AcademicFolder', 'TestimonialFolder']
        query['sort_on'] = 'getObjPositionInParent'
        query['review_state'] = 'published'
        portal_catalog = getToolByName(context, 'portal_catalog')
        results = portal_catalog.searchResults(query)
        for result in results:
            id, item_url = get_view_url(result)
            if id not in ['Members',]:
                data = {'name' : utils.pretty_title_or_id(context, result),
                        'id' : result.getId,
                        'url' : item_url,
                        'description': result.Description}
                self.portal_tabs.append(data)
        if len(portal_tabs) > 1:
            self.portal_tabs.append(portal_tabs[1])

        self.selected_tabs = self.selectedTabs(portal_tabs=self.portal_tabs)
        self.selected_portal_tab = self.selected_tabs['portal']

    def selectedTabs(self, default_tab='index_html', portal_tabs=()):
        plone_url = getToolByName(self.context, 'portal_url')()
        plone_url_len = len(plone_url)
        request = self.request
        valid_actions = []

        url = request['URL']
        path = url[plone_url_len:]

        for action in portal_tabs:
            if not action['url'].startswith(plone_url):
                # In this case the action url is an external link. Then, we
                # avoid issues (bad portal_tab selection) continuing with next
                # action.
                continue
            action_path = action['url'][plone_url_len:]
            if not action_path.startswith('/'):
                action_path = '/' + action_path
            if path.startswith(action_path + '/'):
                # Make a list of the action ids, along with the path length
                # for choosing the longest (most relevant) path.
                valid_actions.append((len(action_path), action['id']))

        # Sort by path length, the longest matching path wins
        valid_actions.sort()
        if valid_actions:
            return {'portal' : valid_actions[-1][1]}

        return {'portal' : default_tab}
