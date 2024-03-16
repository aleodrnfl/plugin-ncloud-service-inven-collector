import logging
import unittest
import os
from spaceone.core import config
import json

from spaceone.inventory.connector.management.metric_connector import MetricConnector

_LOGGER = logging.getLogger(__name__)
AKI = os.environ.get('NCLOUD_ACCESS_KEY_ID', None)
SK = os.environ.get('NCLOUD_SECRET_KEY', None)

class TestMetricConnector(unittest.TestCase):
    secret_data = {
        'ncloud_access_key_id': AKI,
        'ncloud_secret_key': SK,
        'domain_id': 'default',
        'project_id': '25cd875760ea45fdbe6e0198a3e212cc',
        'ncloud_prod_key': '460438474722512896'
    }

    @classmethod
    def setUpClass(cls):
        config.init_conf(package='spaceone.inventory')
        cls.schema = 'naver_client_secret'
        cls.metric_connector = MetricConnector(secret_data=cls.secret_data)
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_get_metric_list(self):
        metric_instances = self.metric_connector.get_metric_list()
        print(metric_instances)

if __name__ == '__main__':
    unittest.main()

    ##