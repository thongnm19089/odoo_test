{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing" "/Odoo-15-Development-Essentials",
    "version": "15.0.1.0.0",
    "depends": ["base"],
    "data": [
        "views/library_menu.xml",
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/book_list_template.xml",
        "data/book_demo.xml",
    ],
    "category": "Services/Library",
    "application": True,
}
