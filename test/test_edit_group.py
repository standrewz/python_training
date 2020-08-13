# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import allure

def test_edit_some_group_name(app, db, check_ui):
    with allure.step('When no groups presented in list'):
        if app.group.count() == 0:
            app.group.create(Group(name="test name", header="test header", footer="test footer"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('Random group selected'):
        random_index = randrange(len(old_groups))
        group = old_groups[random_index]
    with allure.step('Given a new data for group'):
        updated_group = Group(name="New test group")
        updated_group.id = group.id
    with allure.step('When I edit a group to new one %s' %updated_group):
        app.group.modify_group_by_id(group.id, updated_group)
        new_groups = db.get_group_list()
    with allure.step('Then the new group list is equal to the old list without modified group'):
        assert len(old_groups) == len(new_groups)
        old_groups[random_index] = updated_group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
