from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class CurriculumVitae(models.Model):
    _name = 'curriculum.vitae'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary(string="Image")
    name = fields.Char(string="Name", required=True, translate=True)
    job_type = fields.Selection([
        ('customer_service', 'Customer Service'),
        ('system_analyser', 'System Analyser'),
        ('software_developer', 'Software Developer'),
        ('web_developer', 'Web Developer'),
        ('quality_assurance', 'Quality Assurance')
    ], string="Job Type", default="software_developer", required=True)
    mobile = fields.Char(string="Mobile", translate=True)
    email = fields.Char(string="Email")

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth > date.today():
                raise ValidationError("Your date of birth must not over than today.")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            dob = rec.date_of_birth
            number_of_year = today.year - dob.year
            if today.month < dob.month or(today.month == dob.month and today.day < dob.day):
                number_of_year -= 1
            rec.age = number_of_year

    age = fields.Integer(string="Age", group_operator=False, compute=_compute_age, translate=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True, default=date.today())
    nrc = fields.Char(string="NRC", translate=True)
    nationality = fields.Char(string="Country", translate=True)
    religion = fields.Char(string="Religion", translate=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", default='male', required=True)
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married')
    ], string="Marital Status", default="single", required=True)
    current_address = fields.Text(string="Current Address", translate=True)
    objectives = fields.Text(string="Objectives", translate=True)

    education_background_lines = fields.One2many('education.background', 'curriculum_vitae_id',
                                                 states={'done': [('readonly', True)]})
    employment_history_lines = fields.One2many('employment.history', 'curriculum_vitae_id',
                                               states={'done': [('readonly', True)]})
    project_experiences_lines = fields.One2many('project.experiences', 'curriculum_vitae_id',
                                                states={'done': [('readonly', True)]})
    language_skills_lines = fields.One2many('language.skills', 'curriculum_vitae_id',
                                            states={'done': [('readonly', True)]})

    def print_curriculum_vitae_report(self):
        return self.env.ref('curriculum_vitae.curriculum_vitae_report_id').report_action(self)

    def print_curriculum_vitae_excel_report(self):
        return self.env.ref('curriculum_vitae.curriculum_vitae_excel_report_id').report_action(self)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
    ], string="Status", readonly=True, default='draft')

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def open_education_background(self):
        return {
            'name': 'Education Background',
            'type': 'ir.actions.act_window',
            'res_model': 'education.background',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [['curriculum_vitae_id', '=', self.id]]
        }

    def _compute_ebl_count(self):
        count = self.env['education.background'].search_count([('curriculum_vitae_id', '=', self.id)])
        for rec in self:
            rec.ebl_count = count

    ebl_count = fields.Integer(string="EBL count", compute=_compute_ebl_count)

    def open_employment_history(self):
        return {
            'name': 'Employment History',
            'type': 'ir.actions.act_window',
            'res_model': 'employment.history',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [('curriculum_vitae_id', '=', self.id)]
        }

    def _compute_ehl_count(self):
        count = self.env['employment.history'].search_count([('curriculum_vitae_id', '=', self.id)])
        for rec in self:
            rec.ehl_count = count

    ehl_count = fields.Integer(string="EHL count", compute=_compute_ehl_count)

    def open_project_experiences(self):
        return {
            'name': 'Project Experiences',
            'type': 'ir.actions.act_window',
            'res_model': 'project.experiences',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [('curriculum_vitae_id', '=', self.id)]
        }

    def _compute_pel_count(self):
        for rec in self:
            count = len(self.project_experiences_lines)
            rec.pel_count = count

    pel_count = fields.Integer(string="PEL count", compute=_compute_pel_count)

    def open_language_skills(self):
        return {
            'name': 'Language Skills',
            'type': 'ir.actions.act_window',
            'res_model': 'language.skills',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'target': 'new',
            'domain': [('curriculum_vitae_id', '=', self.id)]
        }

    def _compute_lsl_count(self):
        for rec in self:
            rec.lsl_count = len(self.language_skills_lines)

    lsl_count = fields.Integer(string="LSL count", compute=_compute_lsl_count)
