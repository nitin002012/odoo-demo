from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProjectTimeEntry(models.Model):
    _name = 'project.time.entry'
    _description = 'Project Time Entry'

    task_id = fields.Many2one('project.task', string='Task', required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string='User', required=True, default=lambda self: self.env.user)
    date = fields.Date('Date', required=True)
    hours = fields.Float('Hours', required=True)
    description = fields.Text('Description')

    @api.constrains('hours')
    def _check_hours(self):
        for entry in self:
            if entry.hours <= 0:
                raise ValidationError("Hours must be greater than zero.")
            
@api.model
def create_time_entry(self, hours, date):
    for task in self:
        self.env['project.time.entry'].create({
            'task_id': task.id,
            'hours': hours,
            'date': date,
        })

