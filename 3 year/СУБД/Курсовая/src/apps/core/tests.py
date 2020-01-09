# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from unittest import SkipTest
from urlparse import urljoin

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.webdriver.phantomjs.webdriver import WebDriver


class BaseTestCase(StaticLiveServerTestCase):
    screenshots_dir = 'coverage/screenshots/phantomjs'
    fixtures = ['fixtures.json']

    def screenshot(self, screenshot_name=None):
        screenshot_name = self.selenium.current_url or screenshot_name
        self.selenium.get_screenshot_as_file(
            os.path.join(self.screenshots_dir, screenshot_name)
        )

    def go_reverse(self, url, *args, **kwargs):
        self.selenium.get(urljoin(
            self.live_server_url,
            reverse(
                url,
                *args,
                **kwargs
            ))
        )

        self.check_url_reverse(
            url,
            *args,
            **kwargs
        )

    def go(self, url):
        self.selenium.get(urljoin(self.live_server_url, url))
        self.check_url(url)

    def go_without_check(self, url):
        self.selenium.get(urljoin(self.live_server_url, url))

    def go_reverse_without_check(self, url):
        self.selenium.get(urljoin(self.live_server_url, reverse(url)))

    def fill_input(self, el, data):
        self.selenium.find_element_by_id(el).send_keys(data)

    def fill_inputs(self, data_dict):
        for el, data in data_dict.items():
            self.fill_input(el, data)

    def find_and_click(self, el):
        self.selenium.find_element_by_id(el).click()

    def submit(self):
        self.find_and_click('submit')

    def check_url(self, url):
        self.assertIn(
            urljoin(self.live_server_url, url),
            self.selenium.current_url)

    def check_url_reverse(self, url, *args, **kwargs):
        self.assertIn(
            urljoin(self.live_server_url, reverse(url, *args, **kwargs)),
            self.selenium.current_url)

    @classmethod
    def setUpClass(cls):
        try:
            cls.selenium = WebDriver()
            cls.selenium.set_page_load_timeout(10)
            super(BaseTestCase, cls).setUpClass()
        except Exception:
            raise SkipTest('Selenium webdriver is not operational')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(BaseTestCase, cls).tearDownClass()
