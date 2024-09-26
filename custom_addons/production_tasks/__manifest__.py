{
    'name': 'Production Tasks',
    'version': '1.1',
    'depends': ['base'],
    'author': 'Artem Svistelnik',
    'category': 'Production',
    'description': """Module for managing production tasks and performers.""",
    'data': [
        'security/ir.model.access.csv',
        'views/production_tasks_action.xml',
        'views/production_tasks_task_views.xml',
        'views/production_tasks_performer_views.xml',
        'views/production_tasks_menus.xml',
    ],
    'installable': True,
    'application': True,
}