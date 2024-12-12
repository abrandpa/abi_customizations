{
    'name': 'ABI Customizations',
    'version': '17.0.1.0.0',
    'category': 'Custom',
    'summary': 'Custom modifications for A Brand Inc',
    'description': """
        Custom modifications for A Brand Inc including:
        * Customized POS session sales report
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/report_saledetails.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'Proprietary',
}
