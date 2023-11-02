
from odoo import models, fields, api


class Sach(models.Model):
    _name = 'model_quanlysach'
    _auto = True
    _description = 'quanlysach.quanlysach'

    ten_sach = fields.Char()
    ngay_xuat_ban = fields.Char()
    tac_gia = fields.Char()
    mo_ta = fields.Char()
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
