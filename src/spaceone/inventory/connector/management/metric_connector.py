import logging
from spaceone.inventory.libs.connector import NaverCloudConnector
import json

__all__ = ['MetricConnector']

_LOGGER = logging.getLogger("cloudforet")


class MetricConnector(NaverCloudConnector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_metric_list(self):
        # print("metric client: ", self.metric_client) #이 코드는 클라이언트 정보를 보여주는 코드 Response201
        # print(self.metric_client.text)
        # response = json.dumps(self.metric_client.json(), indent=4) #json으로 덤프해서 그런가??
        # print("response", response)
        response = self.metric_client.json()
        return response

## response = { 'metrics' : [~~~], 'prodKey': "22344" }