# -*- coding: utf-8 -*-
{
    'name': "property_management",
    'sequence': -100,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Omar Ahmed",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/property_view.xml',
        'report/property_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
