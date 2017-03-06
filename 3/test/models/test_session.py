# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class TestSession(models.Model):
    _name = 'test.test_session'
    _description = 'Test Session'

    test = fields.Many2one('test.test', 'Test', required=True, ondelete='cascade')
    start_date = fields.Datetime('Start Date', required=True)
    end_date = fields.Datetime('End Date', required=True)
    duration = fields.Integer(readonly=True, store=False, compute='_compute_duration', help='Duration in seconds')

    @api.one
    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        date_format = '%Y-%m-%d %H:%M:%S'
        delta = datetime.strptime(self.end_date, date_format) - datetime.strptime(self.start_date, date_format)
        self.duration = delta.seconds
