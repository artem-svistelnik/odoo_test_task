import datetime

from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductionTask(models.Model):
    _name = 'production_tasks.task'
    _description = 'Production Task'

    name = fields.Char(string='Task Name', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='State', default='draft')

    performer_id = fields.Many2one('production_tasks.performer', string='Performer')

    start_time = fields.Datetime(string='Start Time', readonly=True)
    end_time = fields.Datetime(string='End Time', readonly=True)
    duration = fields.Char(string='Duration', compute='_compute_duration_display')

    def action_start_task(self):
        for task in self:
            if task.state != 'draft':
                raise UserError('The task is already started or completed!')
            task.state = 'in_progress'
            task.start_time = datetime.datetime.utcnow()

    def action_complete_task(self):
        for task in self:
            if task.state != 'in_progress':
                raise UserError('The task is not started or already completed!')
            task.end_time = datetime.datetime.utcnow()
            task.state = 'done'

    @api.depends('start_time', 'end_time')
    def _compute_duration_display(self):
        for task in self:
            if task.start_time and task.end_time:
                delta = task.end_time - task.start_time
                hours, remainder = divmod(delta.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                task.duration = f"{int(hours)}-H; {int(minutes)}-M; {int(seconds)}-S;"
            else:
                task.duration = '0-H; 0-M; 0-S;'