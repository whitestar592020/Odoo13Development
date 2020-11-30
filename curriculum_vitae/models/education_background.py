from odoo import models, fields


class EducationBackground(models.Model):
    _name = 'education.background'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name", translate=True)

    country = fields.Char(string="Country", translate=True)
    certification = fields.Char(string="Certification", translate=True)
    description = fields.Char(string="Description", translate=True)
    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
