from odoo import models, fields

class Performer(models.Model):
    _name = 'production_tasks.performer'
    _description = 'Performer'

    name = fields.Char(string='Performer Name', required=True)
