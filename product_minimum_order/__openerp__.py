# -*- coding: utf-8 -*-
{
    'name': "Product Minimum Order Quantity",
    'summary': """
        Specify the minimum order quantity of an item""",
    'description': """
        This module adds the functionality to control the minimum order quantity
        in a sales order line. The default number is set to 0. You can change this 
		value under the product from for individual products.
		Get in touch with us through info@exploredatasystems.com if you need more help.
    """,
    'author': "Explore Data Systems",
    'website': "http://www.exploredatasystems.com",
    'category': 'Sales Management',
    #Change the version every release for apps.
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [
        'base','sale'
    ],
    # always loaded
    'data': [
        'views/product_view.xml',	
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    # only loaded in test
    'test': [
    ],
}
