from odoo import http
from odoo.http import request

class Books(http.Controller):
    @http.route("/library/books", auth="public", website=True)
    def list_books(self, **kwargs):
        # Sử dụng mô hình "library.book"
        Book = request.env["library.book"].sudo().search([])

        # Trả về template với danh sách sách
        return http.request.render(
            "library_app.book_list_template",
            {"books": Book}
        )
