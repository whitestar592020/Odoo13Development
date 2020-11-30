{
    'name': "Curriculum Vitae",
    'author': "White Star",

    'website': "www.whitestart.com.mm",
    'category': "CV From",
    'summary': """
        Odoo ERP Development Tutorial for Myanmar
    """,

    'description': """
        Odoo ERP Development Tutorial for Mynamr
            - To learn the Odoo ERP Development by creating the curriculum_vitae module.
    """,

    'depends': [
        'base',
        'mail',
        'report_xlsx'
    ],

    'data': [
        'security/ir.model.access.csv',
        'security/curriculum_vitae_security.xml',

        'reports/curriculum_vitae_simple_report.xml',
        'reports/curriculum_vitae_simple_excel_report.xml',

        'reports/curriculum_vitae_report.xml',
        'reports/curriculum_vitae_excel_report.xml',

        'views/curriculum_vitae_simple.xml',
        'views/curriculum_vitae_simple_form_view.xml',

        'views/curriculum_vitae.xml',
        'views/curriculum_vitae_tree_view.xml',
        'views/curriculum_vitae_search_view.xml',
        'views/curriculum_vitae_form_view.xml',
        'views/curriculum_vitae_kanban_view.xml',

        'views/education_background.xml',
        'views/education_background_tree_view.xml',
        'views/education_background_form_view.xml',

        'views/employment_history.xml',
        'views/employment_history_tree_view.xml',
        'views/employment_history_form_view.xml',

        'views/project_experiences.xml',
        'views/project_experiences_tree_view.xml',
        'views/project_experiences_form_view.xml',

        'views/language_skills.xml',
        'views/language_skills_tree_view.xml',
        'views/language_skills_form_view.xml',

        'wizard/reporting_wizard.xml',
        'wizard/reporting_cv_simple_pdf.xml',
        'wizard/reporting_cv_standard_pdf.xml',
        'wizard/reporting_cv_excel_report.xml',

        'views/language_selection.xml',
    ],

    'qweb': [
        'static/src/xml/base.xml',
    ],
}
