# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields, models


class TestResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner']

    is_tester = fields.Boolean(
        'Is Tester',
        readonly=True,
        store=False,
        compute='_compute_is_tester'
    )

    tests_expected = fields.Integer(
        'Tests Expected Within 30 days',
        readonly=True,
        store=False,
        compute='_compute_tests_expected',
    )

    @api.one
    def _compute_is_tester(self):
        self.is_tester = bool(self.env['test.test'].search_count([('tester', '=', self.id)]))

    @api.one
    def _compute_tests_expected(self):
        query = '''
          SELECT count(tts.id)
          FROM test_test_session as tts
            INNER JOIN test_test as tt
              on tts.test = tt.id
            INNER JOIN res_partner as rp
              on tt.tester = rp.id
          WHERE tt.tester = %s
            AND tts.start_date < NOW() + INTERVAL %s
            AND tts.end_date > NOW()
          '''
        self.env.cr.execute(query, [self.id, '1 month'])
        self.tests_expected = self.env.cr.fetchone()[0]
