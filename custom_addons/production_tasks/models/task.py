from odoo import models, fields

class Task(models.Model):
    _name = 'production_tasks.task'
    _description = 'Production Task'

    name = fields.Char(string='Task Name', required=True)
