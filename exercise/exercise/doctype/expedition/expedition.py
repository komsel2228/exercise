# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ridhosribumi and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Expedition(Document):
	def on_submit(self):
		employee = frappe.get_doc("Expedition",self.name)
		new_employee = frappe.copy_doc(employee)
		# new_employee.nama_expedition = 'SICEPAT'
		new_employee.company = 'BUANA MEGA BAHAGIA'

		# test = frappe.get_all('Expedition Item',)
		# new_employee.update.
		new_employee.set('items',[])

		new_employee.append("items",{
			'lokasi' : 'Jakarta',
			'quantity': 1,
			'rate': 1000,
			'warehouse': 'Stores - BMB'
		})

		new_employee.append("items",{
			'lokasi' : 'Surabaya',
			'quantity': 1,
			'rate': 1000,
			'warehouse': 'Stores - BMB'
		})


		# new_employee.get("items").update({
		# 	'warehouse': 'Finished Goods - BMB'
		# })

		new_employee.flags.ignore_permissions = True
		new_employee.insert()
		new_employee.reload()
