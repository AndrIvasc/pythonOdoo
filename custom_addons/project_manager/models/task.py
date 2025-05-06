from odoo import models, fields, api


class Task(models.Model):
    _name = 'project.manager.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('project.manager.project', string='Project')
    assigned_employee_ids = fields.Many2many('res.users', string='Assigned Employees')
    state = fields.Selection(
        [
            ('created', '1. Created'),
            ('in_progress', '2. In Progress'),
            ('done', '3. Done')
        ],
        string='State',
        default='created',
        group_expand='_expand_states'  # This enables custom grouping!
    )

    def _expand_states(self, states, domain, order):
        return ['created', 'in_progress', 'done']
