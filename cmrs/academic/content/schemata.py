from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import AnnotationStorage
from Products.Archetypes.atapi import ImageField
from Products.Archetypes.atapi import ImageWidget
from Products.Archetypes.atapi import LinesField
from Products.Archetypes.atapi import LinesWidget
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import TextField
from Products.ATContentTypes import ATCTMessageFactory as _
from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.validation import V_REQUIRED

AcademicFolderSchema = ATFolderSchema.copy() + Schema((

))

AcademicSchema = ATContentTypeSchema.copy() + Schema((

    StringField('personalName',
        required = True,
        searchable = True,
        storage = AnnotationStorage(),
        widget = StringWidget(
            label='Personal Name',
        )
    ),

    StringField('familyName',
        required = True,
        searchable = True,
        storage = AnnotationStorage(),
        widget = StringWidget(
            label='Family Name',
        )
    ),

    LinesField('postNominals',
        required = False,
        searchable = False,
        storage = AnnotationStorage(),
        widget = LinesWidget(
            label='Post Nominals',
            description = """Add each post nominal on a seperate line""",
        )
    ),

    StringField('jobTitle',
        required = True,
        searchable = True,
        storage = AnnotationStorage(),
        widget = StringWidget(
            label='Job Title',
        )
    ),

    ImageField(
        name='academicPortrait',
        languageIndependent=True,
        storage=AnnotationStorage(),
        swallowResizeExceptions=zconf.swallowImageResizeExceptions.enable,
        pil_quality=zconf.pil_config.quality,
        pil_resize_algo=zconf.pil_config.resize_algo,
        max_size=zconf.ATImage.max_image_dimension,
        sizes= {
            'large'   : (768, 768),
            'preview' : (400, 400),
            'mini'    : (200, 200),
            'thumb'   : (128, 128),
            'tile'    :  (64, 64),
            'icon'    :  (32, 32),
            'listing' :  (16, 16),
        },
        validators=(('isNonEmptyFile', V_REQUIRED),
                    ('checkImageMaxSize', V_REQUIRED)),
        widget=ImageWidget(
            label='Academic Portrait',
            i18n_domain='cmrs.academic',
            show_content_type = False,
        ),
    ),

))

finalizeATCTSchema(AcademicSchema)
