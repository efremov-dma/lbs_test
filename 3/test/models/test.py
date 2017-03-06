# -*- coding: utf-8 -*-

from odoo import models, fields


class Test(models.Model):
    _name = 'test.test'
    _description = 'Test'

    name = fields.Char('Test Name', index=True, required=True)
    purpose = fields.Text('Test Purpose')
    tester = fields.Many2one('res.partner', 'Test', required=True, ondelete='cascade')
