# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name", header="test header", footer="test footer"))
    app.group.modify_first_group(Group(name="New test group"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name", header="test header", footer="test footer"))
    app.group.modify_first_group(Group(header="New header"))