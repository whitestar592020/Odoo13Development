from odoo import models, fields


class LanguageSkills(models.Model):
    _name = 'language.skills'

    name = fields.Char(string="Language", required=True, translate=True)
    level = fields.Char(string="Level", translate=True)
    education_center = fields.Char(string="Education Center", translate=True)
    description = fields.Text(string="Description", translate=True)

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
