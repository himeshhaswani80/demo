from openerp import api,fields,models

class company(models.Model):
    _name='company'
    name=fields.Char(string='Company Name',size=44)
    address=fields.Text(String='Address')
    employee_ids=fields.One2many('company.employee','company_id',string='employee')

class employee(models.Model):
    _name='company.employee'
    name=fields.Char(string='Employee Name',size=44)
    position=fields.Many2one("company.position",String='position')
    company_id=fields.Many2one("company")

class position(models.Model):
    _name='company.position'
    name=fields.Char(string='Position Name',size=44)
    