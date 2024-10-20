from odoo import models, fields

class Milestone(models.Model):
    _name = 'custom.milestone'
    _description = 'Milestone'

    name = fields.Char('Milestone Name', required=True)
    description = fields.Text('Description')
    task_ids = fields.One2many('project.task', 'milestone_id', string='Tasks')

    # New project_id field to link milestones to projects
    project_id = fields.Many2one('project.project', string='Project')

    # Optional fields
    planned_date = fields.Date('Planned Date')
    actual_date = fields.Date('Actual Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('achieved', 'Achieved'),
        ('overdue', 'Overdue')
    ], default='draft', string='Status')
