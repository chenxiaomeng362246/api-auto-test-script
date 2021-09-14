# coding=utf-8
import json
from config.gbl import *
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp
from api_call.base.txt_opera import TxtOpera


class LessonPlan(BaseHttp):
    def __init__(self, env='env'):
        super(LessonPlan, self).__init__(env=env)
        self.tokenId = ''
        my_txt = TxtOpera()
        self.tokenId = my_txt.read_txt_authorizationToken()

        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "8k7m8b5d5fe4uainvosm1ph3aaw1kgvgh4toixcx",
                "x-auth-organization-id": "d4b70d67-9287-49de-4973-a143cf00f052"
            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "uvw9493jpylxyzoww77c6pdhzo445mu82b9h03ja",
                "x-auth-organization-id": "f0bca5c7-1945-1b97-d6ac-806d88e62ebe"
            }
        elif self.env == 'staging':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "lvs656pldskhp2b9ryxz00ng4yo8f3rajv4f8kd8",
                "x-auth-organization-id": "d2bcaa83-062d-af1d-e778-c796397f024d"
            }
        elif self.env == 'prod':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "d8e8wkdumnxcrx74htsfowj9bx5xqy5f1995xq62",
                "x-auth-organization-id": "d6bcaa82-23c4-53e7-d96b-563703ce543c"
            }

        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)

    # ============================================公共部分========================================

    def api_getOrgDetails(self, prn):
        url = '/org-support/graphql'
        body = {
          "operationName": "getOrgDetails",
          "variables": {
            "prn": prn
          },
          "query": "query getOrgDetails($prn: String!) {\n  getOrgDetails(prn: $prn) {\n    id\n    prn\n    name\n    description\n    address\n    address2\n    city\n    region\n    postalCode\n    country\n    domains {\n      name\n      userCount\n      __typename\n    }\n    admins {\n      firstName\n      lastName\n      email\n      disabled\n      __typename\n    }\n    userCount\n    adminCount\n    status\n    createdOn\n    lastUpdatedOn\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        body = json.dumps(body)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, body)
        return res

    def api_searchOrgRequests(self):
        url = '/org-support/graphql'
        body = {
          "operationName": "SearchOrgRequests",
          "variables": {
            "pageNumber": 0,
            "pageSize": 25,
            "sortDirection": "DESC",
            "sortField": "createdOn",
            "searchString": "",
            "filters": {
              "requestStatus": "null",
              "domainsMissing": False,
              "domainUnavailable": False,
              "duplicateName": False,
              "manualFlag": False
            }
          },
          "query": "query SearchOrgRequests($pageNumber: Int, $pageSize: Int, $sortDirection: SortDirection, $sortField: OrgRequestSearchSortField, $searchString: String, $filters: OrgRequestSearchFilter) {\n  searchOrgRequests(request: {pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchString: $searchString, filters: $filters}) {\n    orgRequests {\n      id\n      name\n      lastUpdatedOn\n      createdOn\n      notes\n      requestStatus\n      domains {\n        userCount\n        __typename\n      }\n      statusDetails {\n        domainUnavailable\n        duplicateName\n        domainsMissing\n        manualFlag\n        flagComments\n        invalidDomains\n        __typename\n      }\n      __typename\n    }\n    totalPages\n    totalElements\n    isLastPage\n    isFirstPage\n    currentPage\n    __typename\n  }\n}\n"
        }
        body = json.dumps(body)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, body)
        return res

    def api_get_activityLog_list(self):
        url = '/org-support/graphql'
        body = {
          "operationName": "SearchAudits",
          "variables": {
            "pageNumber": 0,
            "pageSize": 25,
            "sortDirection": "DESC",
            "sortField": "EVENT_TIME",
            "filter": {
              "eventSource": [
                "ORG_SUPPORT",
                "USER_MANAGEMENT",
                "IDENTITY",
                "MDM_PORTAL",
                "CONFIGURATION",
                "INTEGRATION"
              ]
            },
            "searchString": ""
          },
          "query": "query SearchAudits($pageNumber: Int, $pageSize: Int, $sortDirection: SortDirection, $sortField: AuditSortField, $filter: AuditSearchFilter, $searchString: String) {\n  searchAudits(auditSearchInput: {pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, filters: $filter, searchString: $searchString}) {\n    audits {\n      id\n      sessionId\n      successful\n      actor {\n        id\n        email\n        givenName\n        familyName\n        __typename\n      }\n      masquerader {\n        id\n        email\n        givenName\n        familyName\n        __typename\n      }\n      eventTime\n      eventName\n      eventSource\n      i18n\n      targets {\n        userId\n        email\n        givenName\n        familyName\n        orgId\n        orgName\n        panelId\n        panelName\n        siteId\n        siteName\n        ownerId\n        ownerName\n        orgRequestId\n        orgRequestName\n        bundleId\n        bundleName\n        details\n        __typename\n      }\n      __typename\n    }\n    totalPages\n    totalElements\n    isLastPage\n    isFirstPage\n    currentPage\n    __typename\n  }\n}\n"
        }
        body = json.dumps(body)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, body)
        return res
