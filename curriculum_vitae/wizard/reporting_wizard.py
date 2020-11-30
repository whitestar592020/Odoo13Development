from odoo import models, fields, api


class ReportingWizard(models.Model):
    _name = 'reporting.wizard'

    cv_type = fields.Selection([
        ('simple', 'Simple'),
        ('standard', 'Standard'),
    ], string="Curriculum Vitae Type", default="standard")

    @api.depends('simple_cv_form')
    def _get_simple_cv_data(self):
        for rec in self:
            rec.simple_job_type = rec.simple_cv_form.job_type
            rec.simple_gender = rec.simple_cv_form.gender
            rec.simple_image = rec.simple_cv_form.cv_image

    simple_cv_form = fields.Many2one('curriculum.vitae.simple', string="Simple CV From")
    simple_job_type = fields.Char(string="Job Type", compute=_get_simple_cv_data)
    simple_gender = fields.Char(string="Gender", compute=_get_simple_cv_data)
    simple_image = fields.Binary(string="CV Image", compute=_get_simple_cv_data)

    @api.depends('standard_cv_form')
    def _get_standard_cv_data(self):
        for rec in self:
            rec.standard_job_type = rec.standard_cv_form.job_type
            rec.standard_gender = rec.standard_cv_form.gender
            rec.standard_image = rec.standard_cv_form.image

    standard_cv_form = fields.Many2one('curriculum.vitae', string="Standard CV From")
    standard_job_type = fields.Char(string="Job Type", compute=_get_standard_cv_data)
    standard_gender = fields.Char(string="Gender", compute=_get_standard_cv_data)
    standard_image = fields.Binary(string="CV Image", compute=_get_standard_cv_data)

    def print_curriculum_vitae_pdf(self):
        for rec in self:
            if rec.cv_type == 'simple':
                return self.env.ref('curriculum_vitae.reporting_cv_simple_pdf').report_action(self)
            if rec.cv_type == 'standard':
                return self.env.ref('curriculum_vitae.reporting_cv_standard_pdf').report_action(self)

    def print_curriculum_vitae_excel(self):
        for rec in self:
            if rec.cv_type == 'simple':
                return self.env.ref('curriculum_vitae.reporting_cv_simple_excel').report_action(self)
            if rec.cv_type == 'standard':
                return self.env.ref('curriculum_vitae.reporting_cv_standard_excel').report_action(self)
