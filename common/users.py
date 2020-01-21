# -*- coding:utf-8 -*-
from common.idCardandphone import get_user_info

owner_dependents=get_user_info('业主转家属')
owner_be_deleted=get_user_info('业主被删除')
owner_not_pass=get_user_info('业主未通过')
owner_have_dep=get_user_info('业主有家属')
owner_del_dep=get_user_info('业主无家属')
dependents_pass=get_user_info('通过的家属')
dependents_notpass=get_user_info('不通过的家属')
tenant_pass=get_user_info('通过的租户')