# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class myapp(models.Model):
#     _name = 'myapp.myapp'
#     _description = 'myapp.myapp'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
