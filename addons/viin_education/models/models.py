from odoo import models, fields, api


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education Student'

    name = fields.Char(string = "Tên học sinh")
    vstudent_code = fields.Char(string = "Mã HS")
    class_id = fields.Many2one('education.class',string= "Lớp")
  