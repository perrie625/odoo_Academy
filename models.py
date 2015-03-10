# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

class Courses(models.Model):
    _name = 'academy.courses'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")

# class academy(models.Model):
#     _name = 'academy.academy'

#     name = fields.Char()