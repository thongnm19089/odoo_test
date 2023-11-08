
from odoo import models, fields, api

class Sach(models.Model):
    _name = 'db_sach'
    # _auto = True
    # _table = 'db_sach'
    _description = 'Quản lý sách'
    
    ten_sach = fields.Char(string = "Tên sách" ,search =True)
    img = fields.Binary(string='image' , attachment =True)
    ngay_xuat_ban = fields.Datetime(string = "Ngày xuất bản")
    the_loai = fields.Selection([('tieu_thuyet' , 'Tiểu Thiết'),('chuyen_tranh' , 'Chuyện Tranh'),('co_tich','Cổ Tích')], string = 'Thể loại', default ='Tiểu Thuyết' )
    tac_gia = fields.Char(string = "Tác giả",  groups='quanlysach.group_manager')
    mo_ta = fields.Char(string = "Mô tả")

    # Trường One2many để liên kết với Giá sách
#     sach_id = fields.One2many('db.gia_sach', string='Giá sách')

# class GiaSach(models.Model):
#     _name = 'db_gia_sach'
#     _description = 'Quản lý giá sách'
    
#     gia_ban = fields.Float(string='Giá bán', required=True)
#     so_luong = fields.Integer(string='Số lượng', default=0)

#     # Thêm trường Many2one để liên kết với sách
#     sach_id = fields.Many2one('db_sach', string='Sách')
    

