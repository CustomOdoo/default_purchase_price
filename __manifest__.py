# -*- coding: utf-8 -*-
{
    'name': "purchase default price",

    'summary': """
        Purchase default price on product""",

    'description': """
        This module gets the default product price on purchase order line when no 
        vendor price is specified on the product.
    """,

    'author': "AthmanZiri",
    'website': "https://www.innovus.co.ke",

    'category': 'Purchase',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    'application': True,
    'installable': True,
}