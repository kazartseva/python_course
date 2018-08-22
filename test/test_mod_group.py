# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify_first_group(Group(name="Name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify_first_group(Group(header="Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


