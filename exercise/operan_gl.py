# # -*- coding: utf-8 -*-
# # Copyright (c) 2019, Ridhosribumi and contributors
# # For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_fullname, flt, cstr, formatdate
from frappe.model.document import Document
from erpnext.accounts.general_ledger import make_gl_entries
from frappe.utils import nowdate, cstr, flt, now, getdate, add_months
from datetime import datetime

def copydataitem(doc, method) :
    pass

def copydatajv(doc, method):
    employee = frappe.get_doc("Journal Entry",doc.name)
    new_employee = frappe.copy_doc(employee)
    new_employee.company = 'BUANA MEGA BAHAGIA'
    new_employee.set('accounts',[])

    new_employee.append("accounts",{
        'account' : '1111.001 - Kas Kecil - BMB',
        'debit_in_account_currency': 500,
        # 'credit_in_account_currency': 0,
        'cost_center': 'Main - BMB'
    })

    new_employee.append("accounts",{
        'account' : '5510.001 - Beban Adm Bank - BMB',
        'credit_in_account_currency': 500,
        # 'credit_in_account_currency': 0,
        'cost_center': 'Main - BMB'
    })

    new_employee.flags.ignore_permissions = True
    new_employee.insert()
    new_employee.reload()



def copydatapo(doc, method):
    employee = frappe.get_doc("Purchase Order",doc.name)
    new_employee = frappe.copy_doc(employee)
    new_employee.company = 'BUANA MEGA BAHAGIA'
    new_employee.set('items',[])

    new_employee.append("items",{
        'item_code' : 'item1',
        'item_name' : 'item1',
        'qty': 1,
        'uom': 'Unit',
        'stock_uom': 'Unit',
        'conversion_factor': 1,
        'cost_center': 'Main - BMB',
        'warehouse': 'Stores - BMB',
        'expense_account': '4210.000 - HPP Pembelian - BMB'
    })

    new_employee.flags.ignore_permissions = True
    new_employee.insert()
    new_employee.reload()


def copydatasinv(doc, method):
    employee = frappe.get_doc("Sales Invoice",doc.name)
    new_employee = frappe.copy_doc(employee)
    new_employee.company = 'BUANA MEGA BAHAGIA'
    new_employee.debit_to = '1131.0010 - Piutang Dagang - BMB'
    new_employee.set('items',[])

    new_employee.append("items",{
        'item_code' : 'item1',
        'item_name' : 'item1',
        'qty': 1,
        'uom': 'Unit',
        'stock_uom': 'Unit',
        'conversion_factor': 1,
        'rate': 60000,
        'cost_center': 'Main - BMB',
        'warehouse': 'Stores - BMB',
        'expense_account': '4210.000 - HPP Pembelian - BMB',
        'income_account': '4110.000 - Penjualan - BMB'
    })

    new_employee.flags.ignore_permissions = True
    new_employee.insert()
    new_employee.reload()

def copydataprec(doc, method):
    employee = frappe.get_doc("Purchase Receipt",doc.name)
    new_employee = frappe.copy_doc(employee)
    new_employee.company = 'BUANA MEGA BAHAGIA'
    new_employee.set_warehouse = 'Stores - BMB'
    new_employee.set('items',[])

    new_employee.append("items",{
        'item_code' : 'item1',
        'item_name' : 'item1',
        'qty': 500,
        'received_qty': 500,
        'uom': 'Unit',
        'stock_uom': 'Unit',
        'conversion_factor': 1,
        'rate': 15000,
        'cost_center': 'Main - BMB',
        'warehouse': 'Stores - BMB'
        # 'expense_account': '4210.000 - HPP Pembelian - BMB',
        # 'income_account': '4110.000 - Penjualan - BMB'
    })

    new_employee.flags.ignore_permissions = True
    new_employee.insert()
    new_employee.reload()


def copydatapinv(doc, method):
    employee = frappe.get_doc("Purchase Invoice",doc.name)
    new_employee = frappe.copy_doc(employee)
    new_employee.company = 'BUANA MEGA BAHAGIA'
    new_employee.credit_to = '2111.001 - Hutang Dagang Dalam Negeri - BMB'
    new_employee.set('items',[])

    new_employee.append("items",{
        'item_code' : 'item1',
        'item_name' : 'item1',
        'qty': 500,
        'uom': 'Unit',
        'stock_uom': 'Unit',
        'conversion_factor': 1,
        'rate': 30000,
        'cost_center': 'Main - BMB',
        'warehouse': 'Stores - BMB',
        'expense_account': '4210.000 - HPP Pembelian - BMB'
    })

    new_employee.flags.ignore_permissions = True
    new_employee.insert()
    new_employee.reload()
