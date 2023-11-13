# {
#    'name': "Education Management",
#    'summary': """Module education management""",
#    'description': """
#    What it does
#    ============
#    The module provides management education features.
#    Key Features
#    ============
#    * Students management
#    * Parents management
#    """,
#    'author': "Your name",
#    'website':  "http://www.yourcompany.com",
#    'category': 'Uncategorized',
#    'version': '0.1',
#    'depends': ['base'],
#    'data': ['views/education_student_views.xml'],
#    'demo': ['demo.xml'],
# }
# # -*- coding: utf-8 -*-
{
    'name': "education_student   ",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/sach_security.xml',

        # 'views/views.xml',
        'views/education_student_views.xml',
        # '/home/thongcute/Desktop/odoo-15.0/addons/quanlysach/static/src/css/custom_styles.css',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
