from odoo import models, fields


class TaskFilterWizard(models.TransientModel):
    _name = 'task.filter.wizard'
    _description = 'Task Filter Wizard'

    project_id = fields.Many2one('project.manager.project', string='Project')
    employee_ids = fields.Many2many('res.users', string='Assigned Employees')
    date_from = fields.Date(string='Start Date')
    date_to = fields.Date(string='End Date')

    def action_filter_tasks(self):
        domain = []

        if self.project_id:
            domain.append(('project_id', '=', self.project_id.id))
        if self.employee_ids:
            domain.append(('assigned_employee_ids', 'in', self.employee_ids.ids))
        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))

        return {
            'name': 'Filtered Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'project.manager.task',
            'view_mode': 'tree,form,kanban',
            'domain': domain,
        }
