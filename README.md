# Project Manager – Odoo Custom Module

A custom Odoo module to manage projects and tasks with user permissions and PDF reports.

## 🔧 Installation

git clone https://github.com/odoo/odoo --branch 13.0 --single-branch

### Step 1: Clone Odoo 13 Source Code

`bash
cd C:\Users\andre\PycharmProjects\pythonOdoo
git clone https://github.com/odoo/odoo --branch 13.0 --single-branch

Step 2: Set Up Python 3.7 and Virtual Environment
Use Python 3.7 as your interpreter.

Create and activate the virtual environment:
`bash
python -m venv .venv
.\.venv\Scripts\activate

Step 3: Install Dependencies
`bash
cd odoo
pip install -r requirements.txt

Step 4: Create Odoo Config File
Create a file named odoo.conf in the project root with the following content:

[options]
addons_path = addons,custom_addons
admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
xmlrpc_port = 8069
log_level = info

Step 5: Set Up PostgreSQL
Download: https://www.postgresql.org/download/

Use username: odoo, password: odoo

If needed, run:
CREATE USER odoo WITH PASSWORD 'odoo' SUPERUSER;

Step 6: Create Addons Folder
Create the custom_addons folder next to odoo:

pythonOdoo/
├── odoo/
├── custom_addons/
│   └── project_manager/

Step 7: Run Odoo in PyCharm
In Run > Edit Configurations, set:

Script Path: C:\Users\andre\PycharmProjects\pythonOdoo\odoo\odoo-bin

Parameters: -c ../odoo.conf

Working Directory: C:\Users\andre\PycharmProjects\pythonOdoo\odoo

Interpreter: .venv Python 3.7

Start the app and open http://localhost:8069
---------------------------------------------------------------------------------------------------------------------------------

Features
✅ Project and Task models

✅ Drag & drop kanban for task status

✅ User access restrictions

✅ Admin can see all, users only their tasks

✅ Automated test for permissions

✅ GitHub Actions pipeline to run tests on push to master

❌ Bonus: Popup/email on task status change (not working yet)
