# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group("Test group", "Test header", "Test footer"))

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))

