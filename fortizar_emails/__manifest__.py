{
    'name': "Fortizar email module",

    'summary': """
    Fortizar module that sets up the necessary emails
    """,

    'description': """
    """,

    'author': "Fortizar Kft.",
    'website': "https://www.fortizar.hu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'views/message_notification_email.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
