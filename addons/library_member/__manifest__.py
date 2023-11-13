{
    "name": "Library Members",
    "license": "AGPL-3",
    "description": "Manage members borrowing books.",
    "author": "Daniel Reis",
    "depends": ["library_app", "mail"],
    "application": False,
    "data": [
        # 'security/ir.model.access.csv',
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
}
