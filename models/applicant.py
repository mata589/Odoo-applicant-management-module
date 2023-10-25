# applicant_management/models/applicant.py

from odoo import models, fields

class Applicant(models.Model):
    _name = 'applicant.management.applicant'
    _description = 'Applicant'

    name = fields.Char(string='Full Name', required=True)
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    program = fields.Char(string='Program of Study/Course')
    intake = fields.Char(string='Intake')
    course_units = fields.Selection([
        ('unit1', 'Unit 1'),
        ('unit2', 'Unit 2'),
        ('unit3', 'Unit 3'),
        # Add more choices as needed
    ], string='Course Units of Choice')