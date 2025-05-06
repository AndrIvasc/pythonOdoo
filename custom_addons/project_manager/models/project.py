from odoo import models, fields

class Project(models.Model):
    _name = 'project.manager.project'
    _description = 'Project'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    task_ids = fields.One2many('project.manager.task', 'project_id', string='Tasks')


