# Copyright 2022 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Update Wizard Payment Mode',
    'version': '14.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Add Payment Mode to Invoice Update Wizard',
    'author': 'Akretion',
    'website': 'https://github.com/akretion/odoo-usability',
    'depends': ['account_invoice_update_wizard', 'account_payment_partner'],
    'data': ['wizard/account_move_update_view.xml'],
    'installable': True,
    'auto_install': True,
}
