# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group_name(app):
    app.group.modify_first_group(Group(name="New test group"))

def test_edit_group_header(app):
    app.group.modify_first_group(Group(header="New header"))