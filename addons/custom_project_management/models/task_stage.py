from odoo import models, fields

class TaskStage(models.Model):
    _name = 'custom.task.stage'
    _description = 'Custom Task Stage'

    name = fields.Char('Stage Name', required=True)
    sequence = fields.Integer('Sequence', default=10, help="Sequence order for stages.")
    color = fields.Integer('Color Index', help="Color index for kanban view.")
