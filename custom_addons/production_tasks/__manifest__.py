{
    'name': 'Production Tasks',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Artem Svistelnik',
    'category': 'Production',
    'description': """Module for managing production tasks and performers.""",
    'data': [

        'security/ir.model.access.csv',
        'views/production_tasks_menus.xml',
        'views/task_views.xml',
        # 'views/performer_views.xml',
        # 'data/data.xml',
    ],
    'installable': True,
    'application': True,
}