# -*- coding: utf-8 -*-
from apps.core.tests import BaseTestCase


class CrmFinanceTestCase(BaseTestCase):

    def test_1_list_page_without_login(self):
        self.go_reverse_without_check('crm:finance:list')
        self.check_url_reverse('crm:login')

    def test_2_login_to_crm(self):
        self.go_reverse('crm:login')
        self.fill_inputs({
            'id_username': 'deploy',
            'id_password': 'deploy'
        })

        self.submit()

    def test_3_list_page_after_login(self):
        self.go_reverse('crm:finance:list')

    def test_4_create_from_crm(self):
        self.find_and_click('create')
