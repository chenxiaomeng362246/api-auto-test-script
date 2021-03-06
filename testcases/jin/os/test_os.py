# coding=utf-8
import testcases.account.xq_glb as glb
from config.gbl import *
import unittest
import api_call.jin.os.api_os as api_os




class OsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lesson_object = api_os.LessonPlan(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

# ============================================公共部分========================================
    def test_get_org_details(self):
        """
            [POST]获取某个组织的组织详情
        """
        prn = "prn:Organization::ApiTest"
        # 获取组织详情  //ApiTest
        err_message = '获取组织详情失败'
        response = self.lesson_object.api_getOrgDetails(prn)
        glb.rest_o.parse_response(response, glb.CODE200, err_message)

    def test_orgRequestsList(self):
        """
            [POST]获取org request列表
        """
        # 获取组织详情  //ApiTest
        err_message = '获取列表失败'
        response = self.lesson_object.api_orgRequestsList()
        glb.rest_o.parse_response(response, glb.CODE200, err_message)

    def test_getIntegrationsList(self):
        """
            [POST]获取Integrations列表
        """
        # 获取组织详情  //ApiTest
        err_message = '获取列表失败'
        response = self.lesson_object.api_getIntegrationsList()
        glb.rest_o.parse_response(response, glb.CODE200, err_message)

    def test_getActivityLogList(self):
        """
            [POST]获取activity log列表
        """
        # 获取组织详情  //ApiTest
        err_message = '获取列表失败'
        response = self.lesson_object.api_getActivityLogList()
        glb.rest_o.parse_response(response, glb.CODE200, err_message)
