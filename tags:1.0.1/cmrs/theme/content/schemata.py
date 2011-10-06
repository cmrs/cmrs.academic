from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import AnnotationStorage
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import LinesField
from Products.Archetypes.atapi import LinesWidget
from Products.Archetypes.atapi import MultiSelectionWidget
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import SelectionWidget
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import TextField

from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.content.image import ATImageSchema

SectionFolderSchema = ATFolderSchema.copy() + Schema((

))

SectionImageFolderSchema = ATFolderSchema.copy() + Schema((

))

BannerImageSchema = ATImageSchema.copy() + Schema((

))

BannerImageSchema['image'].widget.description = """The image must be 930 pixels wide and 180 pixels tall,
                                                   otherwise the image will be stretched."""

finalizeATCTSchema(BannerImageSchema)

SectionImageSchema = ATImageSchema.copy() + Schema((

))

SectionImageSchema['image'].sizes['portlet'] = (191, 10000)
finalizeATCTSchema(SectionImageSchema)
