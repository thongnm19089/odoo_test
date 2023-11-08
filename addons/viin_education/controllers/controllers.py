# -*- coding: utf-8 -*-
# from odoo import http


# class ViinEducation(http.Controller):
#     @http.route('/viin_education/viin_education', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viin_education/viin_education/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viin_education.listing', {
#             'root': '/viin_education/viin_education',
#             'objects': http.request.env['viin_education.viin_education'].search([]),
#         })

#     @http.route('/viin_education/viin_education/objects/<model("viin_education.viin_education"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viin_education.object', {
#             'object': obj
#         })
