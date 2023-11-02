# -*- coding: utf-8 -*-
# from odoo import http


# class Quanlysach(http.Controller):
#     @http.route('/quanlysach/quanlysach', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quanlysach/quanlysach/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quanlysach.listing', {
#             'root': '/quanlysach/quanlysach',
#             'objects': http.request.env['quanlysach.quanlysach'].search([]),
#         })

#     @http.route('/quanlysach/quanlysach/objects/<model("quanlysach.quanlysach"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quanlysach.object', {
#             'object': obj
#         })
