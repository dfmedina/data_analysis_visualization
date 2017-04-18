import unittest

from mock import Mock, create_autospec
from django.utils.timezone import utc
from datetime import datetime
import json
import os
from elasticsearch import Elasticsearch


class TestLandingDAO(unittest.TestCase):

    def setUp(self):
        elastic_client = create_autospec(Elasticsearch)
        self.dao = LandingDAO(elastic_client)

        self.config_message = self.load_fixture('configuration.json')
        self.events_message = self.load_fixture('events.json')

        self.now = datetime.now(tz=utc)
        self.dao.now_isoformat = Mock(return_value='{:%Y-%m-%dT%H:%M:%S%z}'.format(self.now))