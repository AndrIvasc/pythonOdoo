{
    'name': 'Project Manager',
    'version': '1.0',
    'summary': 'Manage projects and tasks with assigned employees',
    'sequence': 10,
    'description': """Custom module to manage projects, tasks, and track progress.""",
    'category': 'Project',
    'author': 'Your Name',
    'website': 'https://yourportfolio.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/task_views.xml',
    ],
    'application': True,
}
