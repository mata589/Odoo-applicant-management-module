{
    'name': 'Applicant Management',
    'version': '1.3',
    'category': 'Human Resources',
    'summary': 'Custom module for managing applicants',
    'description': """
    This module handles applicant management for our univesity.
    """,
    'author': 'Kizito Richard',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/applicant_views.xml',
      
        

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}