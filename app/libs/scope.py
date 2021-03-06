# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午11:41
# @Author  : iGolden
# @Software: PyCharm


class Scope:
    allow_api = set()
    allow_module = set()
    forbidden = set()

    def __add__(self, other):
        self.allow_module = self.allow_module | other.allow_module
        self.allow_api = self.allow_api | other.allow_api
        self.forbidden = self.forbidden | other.forbidden
        return self


class AdminScope(Scope):
    allow_module = {'v1.user', 'v1.posts', 'v1.reports', 'v1.likes', 'v1.collections', 'v1.followers', 'v1.comments',
                    'v1.upload'}


class UserScope(Scope):
    forbidden = {'v1.user+super_get_user', 'v1.user+super_delete_user', 'v1.user+super_user_list',
                 'v1.user+super_user_active', 'v1.posts+super_posts_list', 'v1.posts+super_delete_posts',
                 'v1.posts+super_reports_list'}

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    return (endpoint in scope.allow_api) or (red_name in scope.allow_module)
