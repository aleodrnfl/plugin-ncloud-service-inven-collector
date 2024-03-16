import logging
from spaceone.inventory.libs.connector import NaverCloudConnector
import json

__all__ = ['MetricConnector']

_LOGGER = logging.getLogger("cloudforet")


class MetricConnector(NaverCloudConnector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_metric_list(self):

        response = self.metric_client.json()
        return response
