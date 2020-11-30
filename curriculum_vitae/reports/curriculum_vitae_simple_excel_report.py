from odoo import models, api, _
import base64
import io


class CurriculumVitaeSimpleExcelReport(models.Model):
    _name = 'report.curriculum_vitae.cv_form_simple_excel_report_id'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        header_format = workbook.add_format({'font_size': 14, 'bold': True, 'align': 'center', 'valign': 'vcenter'})
        label_format = workbook.add_format({'font_size': 11, 'bold': True})

        sheet = workbook.add_worksheet("Curriculum Vitae Simple")
        sheet.set_column(0, 0, 25)
        sheet.set_column(1, 1, 50)
        sheet.set_column(2, 2, 20)
        sheet.set_row(0, 100)
        sheet.merge_range('A1:B1', 'CURRICULUM VITAE', header_format)

        cv_image = lines.cv_image
        image_data = base64.b64decode(cv_image)
        image = io.BytesIO(image_data)
        sheet.insert_image('C1', 'cv_image.png', {'image_data': image, 'x_scale': 0.6, 'y_scale': 0.6})

        sheet.write('A2', _('Name'), label_format)
        sheet.merge_range('B2:C2', lines.name)
        sheet.write('A3', _('NRC'), label_format)
        sheet.merge_range('B3:C3', lines.nrc)
        sheet.write('A4', _('Date of Birth'), label_format)
        sheet.merge_range('B4:C4', lines.date_of_birth,
                          workbook.add_format({'num_format': 'dd/mm/yyyy', 'align': 'left'}))
        sheet.write('A5', _('Place of Birth'), label_format)
        sheet.merge_range('B5:C5', lines.place_of_birth)
        sheet.write('A6', _('Nationality'), label_format)
        sheet.merge_range('B6:C6', lines.nationality)

        sheet.write('A7', _('Gender'), label_format)
        sheet.merge_range('B7:C7', lines.gender)
        sheet.write('A8', _('Qualification'), label_format)
        sheet.merge_range('B8:C8', lines.qualification)
        sheet.write('A9', _('Hobby'), label_format)
        sheet.merge_range('B9:C9', lines.hobby)
        sheet.write('A10', _('Address'), label_format)
        sheet.merge_range('B10:C10', lines.address)
        sheet.write('A11', _('Permanent Address'), label_format)
        sheet.merge_range('B11:C11', lines.permanent_address)

        sheet.write('A12', _('Email'), label_format)
        sheet.merge_range('B12:C12', lines.email)
        sheet.write('A13', _('Facebook'), label_format)
        sheet.merge_range('B13:C13', lines.facebook)
        sheet.write('A14', _('Phone'), label_format)
        sheet.merge_range('B14:C14', lines.phone)
        sheet.write('A15', _('Field of Interest'), label_format)
        sheet.merge_range('B15:C15', lines.field_of_interest)
        sheet.write('A11', _('Working Experience'), label_format)
        sheet.merge_range('B15:C15', lines.working_experience)
