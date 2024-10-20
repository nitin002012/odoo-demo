from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Timesheet(models.Model):
    _name = 'custom.timesheet'
    _description = 'Timesheet'

    user_id = fields.Many2one('res.users', string='User', required=True)
    task_id = fields.Many2one('project.task', string='Task', required=True)
    date = fields.Date('Date', required=True)
    hours = fields.Float('Hours', required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='draft', string='Status')

    @api.constrains('hours')
    def _check_hours(self):
        for record in self:
            if record.hours <= 0:
                raise ValidationError("Hours must be greater than zero.")
    
    def submit_timesheet(self):
        for record in self:
            record.write({'state': 'submitted'})

    def approve_timesheet(self):
        for record in self:
            record.write({'state': 'approved'})

    def reject_timesheet(self):
        for record in self:
            record.write({'state': 'rejected'})

    def cancel_timesheet(self):
        for record in self:
            record.write({'state': 'draft'})



