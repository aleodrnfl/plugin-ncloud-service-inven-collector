import logging
from spaceone.inventory.libs.connector import NaverCloudConnector
import json

__all__ = ['MetricConnector']

_LOGGER = logging.getLogger("cloudforet")


class MetricConnector(NaverCloudConnector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_metric_list(self):
        # print("metric client: ", self.metric_client)
        # print(self.metric_client.text)
        response = json.dumps(self.metric_client.json(), indent=4)
        # print("response", response)
        return response

