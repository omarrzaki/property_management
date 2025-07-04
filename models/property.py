from odoo import models, fields, api


class Property(models.Model):
    _name = 'property'
    _description = 'Property Management'
    name = fields.Char(string="أسم العقار")
    location = fields.Char(string="موقع العقار")
    price = fields.Float(string="السعر")
    description = fields.Text(string="وصف")
    state = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('inactive', 'Inactive')
    ], string="State", default='available')

    def action_mark_as_rented(self):
        for rec in self:
            rec.state = 'rented'

    def action_return_to_available(self):
        for rec in self:
            rec.state = 'available'


