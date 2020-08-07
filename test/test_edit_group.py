# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_edit_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test name", header="test header", footer="test footer"))
    old_groups = db.get_group_list()
    random_index = randrange(len(old_groups))
    group = old_groups[random_index]
    updated_group = Group(name="New test group")
    updated_group.id = group.id
    app.group.modify_group_by_id(group.id, updated_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[random_index] = updated_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test name", header="test header", footer="test footer"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)