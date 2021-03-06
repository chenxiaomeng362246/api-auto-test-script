# coding=utf-8


__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
import config.gbl as g
from api_call.base.txt_opera import TxtOpera


class LessonPlan(BaseHttp):
    def __init__(self, env='dev'):
        super(LessonPlan, self).__init__(env=env)
        self.ssl = True
        self.token = ''
        self.cookies = ''
        self.XSRF_TOKEN=''
        self.cookies_x=''
        self.cookies_p = ''
        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()
        self.cookies=my_txt.read_txt_cookies()
        self.XSRF_TOKEN = my_txt.read_txt_cookies_x()
        self.cookies_x=my_txt.read_txt_cookies_x()
        self.cookies_p = my_txt.read_txt_cookies_p()


        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json",
                # MyPromethean
                # "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                "Authorization":self.XSRF_TOKEN,
               "Cookie":"XSRF-TOKEN="+self.XSRF_TOKEN+";prom:sess="+self.cookies_p
            }
        elif self.env == 'sandbox':
            self.header = {
                # "Accept": "application/json",
                "Content-Type": "application/json",
                # MyPromethean
                # "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
                "Authorization":self.XSRF_TOKEN,
                 "Cookie":"XSRF-TOKEN="+self.XSRF_TOKEN+";prom:sess="+self.cookies_p
              }
        else:
            self.header = {
                "Content-Type": "application/json",
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                # Panel Management?
                # user Management?
                "Authorization":self.XSRF_TOKEN,
                # "XSRF-TOKEN" : self.XSRF_TOKEN,
                # "credentials": "include"
                 "Cookie":"XSRF-TOKEN="+self.XSRF_TOKEN+";prom:sess="+self.cookies_p
                # "Cookie":self.cookies
                # "Cookie": my_txt.read_txt_cookies()
            }
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=self.ssl)

    # ============================================????????????========================================


    def post_list_query(self):
        """
      4.1.2 [POST] /Filters and sort
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res



    def post_list_query_all_des(self):
        """
      4. [POST] /Filters and sort ????????????
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":100,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}],\"accountStatus\":[{\"prn\":\"prn:AccountStatus:System:Active\"},{\"prn\":\"prn:AccountStatus:System:Suspended\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_list_query_all(self):
        """
      4. [POST] /Filters and sort ????????????
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":100,\"sortDirection\":\"ASC\",\"sortField\":\"lastName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}],\"accountStatus\":[{\"prn\":\"prn:AccountStatus:System:Active\"},{\"prn\":\"prn:AccountStatus:System:Suspended\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def get_user_permissions(self):
        """
       get
        """
        url = "/identity/user/permissions"
        # payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def post_set_roles_for_user(self):
        """
        ???????????????????????????
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res


    def post_filter_list(self):
        """
         ????????????????????????????????????
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"email\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_filter_list_page(self):
        """
         ???????????????????????????????????? ???????????????????????????????????????100???
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":100,\"sortDirection\":\"DESC\",\"sortField\":\"email\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_search_users(self):
        """
         ???????????????????????????"Dan"
        """

        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"ASC\",\"sortField\":\"firstName\",\"filter\":{\"fullTextSearchString\":\"Dan\"}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_remove_a_role(self):
        """
         ??????????????????????????????
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"ASC\",\"sortField\":\"firstName\",\"filter\":{\"fullTextSearchString\":\"\"}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_a_role_suspended(self):
        """
         ??????lnz300005@nd.com.cn????????????suspended
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"disableUserInOrg\",\"variables\":{\"disableUserInput\":{\"orgPrn\":\"prn:Organization::Promethean\",\"userPrn\":\"prn:User::lnz300005@nd.com.cn\"}},\"query\":\"mutation disableUserInOrg($disableUserInput: EnableOrDisableUserInOrgInput!) {\\n  disableUserInOrg(disableUserInput: $disableUserInput)\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res