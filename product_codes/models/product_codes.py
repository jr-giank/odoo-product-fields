from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    old_code = fields.Char(string='Old code')
    provider_code = fields.Char(string='Provider code')
    custom_code = fields.Char(string='Custom code')
