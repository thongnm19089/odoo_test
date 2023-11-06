
from odoo import models, fields, api

class Sach(models.Model):
    _name = 'db_sach'
    # _auto = True
    # _table = 'db_sach'
    _description = 'quanlysach.quanlysach'
    
    ten_sach = fields.Char(string = "Tên sách")
    img = fields.Binary(string='image' , attachment =True)
    ngay_xuat_ban = fields.Datetime(string = "Ngày xuất bản")
    the_loai = fields.Selection([('tieu_thuyet' , 'Tiểu Thiết'),('chuyen_tranh' , 'Chuyện Tranh'),('co_tich','Cổ Tích')], string = 'Thể loại', default ='Tiểu Thuyết' )
    tac_gia = fields.Char(string = "Tác giả")
    mo_ta = fields.Char(string = "Mô tả")

