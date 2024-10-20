from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Field to store time entries related to the task
    time_entry_ids = fields.One2many('project.time.entry', 'task_id', string='Time Entries')
    user_id = fields.Many2one('res.users', string='Assigned to')    
    milestone_id = fields.Many2one('project.milestone', string='Milestone')



    # Method to send notifications for completed tasks
    @api.model
    def send_task_completion_notification(self):
        # Find completed tasks
        completed_tasks = self.search([('stage_id', '=', self.env.ref('project.stage_done').id)])
        for task in completed_tasks:
            if task.user_id:
                # Get the email template for task completion
                template = self.env.ref('your_module.task_completion_email_template')
                if template:
                    template.send_mail(task.id, force_send=True)

    # Method to notify about approaching deadlines
    @api.model
    def notify_approaching_deadlines(self):
        # Find tasks that are approaching their deadlines
        approaching_tasks = self.search([
            ('end_date', '<=', fields.Datetime.now() + timedelta(days=2)),
            ('stage_id', '!=', self.env.ref('project.stage_done').id)
        ])
        for task in approaching_tasks:
            if task.user_id:
                # Get the email template for approaching deadlines
                template = self.env.ref('your_module.approaching_deadline_email_template')
                if template:
                    template.send_mail(task.id, force_send=True)

    # Override action_complete to trigger notifications when a task is completed
    def action_complete(self):
        res = super(ProjectTask, self).action_complete()
        self.send_task_completion_notification()  # Notify when tasks are completed
        return res

    # Scheduled action to notify about approaching deadlines
    @api.model
    def _schedule_notify_approaching_deadlines(self):
        self.notify_approaching_deadlines()
