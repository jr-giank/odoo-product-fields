from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    old_code = fields.Char(string='Old code', copy=False)
    provider_code = fields.Char(string='Provider code', copy=False)
    custom_code = fields.Char(string='Custom code')

    @api.constrains('custom_code')
    def _check_custom_code_format(self):
        for record in self:
            if record.custom_code and not re.match(r'^\d{4}\.\d{2}\.\d{2}$', record.custom_code):
                raise ValidationError("Custom code must follow the format 9999.99.99")
