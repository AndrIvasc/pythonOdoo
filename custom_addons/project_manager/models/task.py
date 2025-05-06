from odoo import models, fields


class Task(models.Model):
    _name = 'project.manager.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('project.manager.project', string='Project')
    assigned_employee_ids = fields.Many2many('res.users', string='Assigned Employees')

    state = fields.Selection([
        ('created', 'Created'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='created')