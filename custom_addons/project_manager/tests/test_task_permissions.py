from odoo.tests.common import TransactionCase


class TestTaskPermissions(TransactionCase):
    def setUp(self):
        super().setUp()

        self.admin_user = self.env.ref('base.user_admin')
        self.regular_user = self.env['res.users'].create({
            'name': 'Test Regular',
            'login': 'test_regular',
            'email': 'test_regular@example.com',
            'groups_id': [(6, 0, [self.env.ref('project_manager.group_project_user').id])],
        })

        self.project = self.env['project.manager.project'].create({
            'name': 'Test Project',
        })

        self.task_admin = self.env['project.manager.task'].with_user(self.admin_user).create({
            'name': 'Admin Task',
            'project_id': self.project.id,
            'assigned_employee_ids': [(6, 0, [self.admin_user.id])]
        })

        self.task_regular = self.env['project.manager.task'].with_user(self.admin_user).create({
            'name': 'User Task',
            'project_id': self.project.id,
            'assigned_employee_ids': [(6, 0, [self.regular_user.id])]
        })

    def test_admin_sees_all_tasks(self):
        tasks = self.env['project.manager.task'].with_user(self.admin_user).search([])
        self.assertEqual(len(tasks), 2)

    def test_regular_user_sees_only_their_tasks(self):
        tasks = self.env['project.manager.task'].with_user(self.regular_user).search([])
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks.name, 'User Task')