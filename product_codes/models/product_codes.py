from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    old_code = fields.Char(string='Old Code')
    provider_code = fields.Char(string='Provider Code')
    custom_code = fields.Char(string='Custom Code')
