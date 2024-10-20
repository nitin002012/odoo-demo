from odoo import models, fields, api

class ResourceAvailability(models.Model):
    _name = 'resource.availability'
    _description = 'Resource Availability'

    user_id = fields.Many2one('res.users', string='User', required=True)
    start_date = fields.Datetime('Available From', required=True)
    end_date = fields.Datetime('Available Until', required=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('busy', 'Busy'),
    ], default='available')

    # New fields for workload management
    max_tasks = fields.Integer('Maximum Tasks', required=True, default=5)
    current_task_count = fields.Integer('Current Task Count', compute='_compute_current_task_count', store=True)

    @api.depends('user_id')
    def _compute_current_task_count(self):
        for record in self:
            record.current_task_count = self.env['project.task'].search_count([
                ('user_id', '=', record.user_id.id),
                ('state', '!=', 'done'),  # Exclude completed tasks
            ])
