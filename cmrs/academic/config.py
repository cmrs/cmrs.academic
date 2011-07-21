from Products.Archetypes.atapi import DisplayList

PROJECTNAME = 'cmrs.academic'

ADD_PERMISSIONS = {
    'Academic': 'CmrsAcademic: Add Academic',
    'AcademicFolder': 'CmrsAcademic: Add AcademicFolder',
}

PRE_NOMINAL = DisplayList((
    ('', ''),
    ('Dr', 'Dr'),
    ('Miss', 'Miss'),
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Prof', 'Prof'),
    ('Sir', 'Sir'),
))
