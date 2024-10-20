{
    'name': 'Custom Project Management',
    'version': '1.0',
    'depends': ['project','resource','base'],  
    'author': 'nitin',
    'data': [
        'security/ir.model.access.csv',
        'views/task_stage_views.xml',
        'data/task_stage_data.xml',  # Include the data file here
        'views/milestone_views.xml',  # Include the milestone views
        'views/resource_availability_views.xml',  # Include the resource availability views
        'views/workload_dashboard_views.xml',  # Include workload dashboard views
        'views/time_entry_views.xml',  # Include time entry views
        'views/project_task_views.xml',  # Include project task view updates
        'views/timesheet_views.xml',
        'data/scheduled_actions.xml',
        'data/email_templates.xml',





    ],
    'installable': True,
    'application': True,
}
