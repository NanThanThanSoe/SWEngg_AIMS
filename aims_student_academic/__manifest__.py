# -*- coding: utf-8 -*-
{
	'name': 'TGGS - AIMS',
	'version': '12.0.1.0.0',
	'summary': 'TGGS Academic Information Management System',
	'category': 'Tools',
	'author': 'Lianne Visperas',
	'maintainer': 'TGGS',
	'company': 'TGGS',
	'website': 'TGGS',
	'depends': ['board', 'document', 'hr', 'web', 'website', 'mail'],
	'images': ['static/description/icon.png'],
	'data': [
		'security/tggs_security.xml',
		'security/ir.model.access.csv',
		'reports/report_menu.xml',
		'reports/report_tggs_certificate.xml',
		'views/student_view.xml',
		'views/course_view.xml',
		'views/batch_view.xml',
		'views/subject_view.xml',
		'views/category_view.xml',
		'views/faculty_view.xml',
		'views/academic_affairs_view.xml',
		'views/aims_tggs_template.xml',
		'menu/tggs_menu.xml',
	],
	'license': 'AGPL-3',
	'installable': True,
	'application': True,
	'auto_install': False,
}