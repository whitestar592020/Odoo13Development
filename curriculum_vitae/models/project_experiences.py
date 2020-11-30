from odoo import models, fields


class ProjectExperiences(models.Model):
    _name = 'project.experiences'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Project Name", translate=True)
    position = fields.Char(string="Position", translate=True)
    responsibilities = fields.Char(string="Responsibilities", translate=True)
    programming_languages = fields.Char(string="Programming Languages", translate=True)
    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")
    description = fields.Text(string="Description", translate=True)

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
