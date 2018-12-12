# -*- coding: utf-8 -*-
"""
    step7.test.TestBeaconsHttpServiceV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    TestBeaconsHttpServiceV1 class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
import json
import time

import requests
from pip_services3_commons.config import ConfigParams
from pip_services3_commons.errors import InvocationException
from pip_services3_commons.refer import References, Descriptor

from step7.src.data.version1 import BeaconV1, BeaconTypeV1
from step7.src.logic.BeaconsController import BeaconsController
from step7.src.persistence.BeaconsMemoryPersistence import BeaconsMemoryPersistence
from step7.src.services.version1.BeaconsHttpServiceV1 import BeaconsHttpServiceV1

BEACON1 = BeaconV1("1", "1", BeaconTypeV1.AltBeacon, "00001", "TestBeacon1", {"type": 'Point', "coordinates": [0, 0]}, 50)
BEACON2 = BeaconV1("2", "1", BeaconTypeV1.iBeacon, "00002", "TestBeacon2", {"type": 'Point', "coordinates": [2, 2]}, 70)
BEACON3 = BeaconV1("3", "2", BeaconTypeV1.AltBeacon, "00003", "TestBeacon3", {"type": 'Point', "coordinates": [10, 10]}, 50)

class TestBeaconsHttpServiceV1():
    @classmethod
    def setup_class(cls):
        cls._persistence = BeaconsMemoryPersistence()
        cls._controller = BeaconsController()
        cls._service = BeaconsHttpServiceV1()

        cls._service.configure(ConfigParams.from_tuples(
            'connection.protocol', 'http',
            'connection.port', 3000,
            'connection.host', 'localhost'))

        references = References.from_tuples(Descriptor('beacons', 'persistence', 'memory', 'default', '1.0'),
                                            cls._persistence,
                                            Descriptor('beacons', 'controller', 'default', 'default', '1.0'),
                                            cls._controller,
                                            Descriptor('beacons', 'service', 'http', 'default', '1.0'),
                                            cls._service)
        cls._controller.set_references(references)
        cls._service.set_references(references)

        cls._persistence.open(None)
        cls._service.open(None)

    @classmethod
    def teardown_class(cls):
        cls._persistence.close(None)
        cls._service.close(None)

    # def test_crud_operations(self):
        # Create the first beacon
        # url = 'http://localhost:3000'
        # response = None
        # try:
        #     response = requests.post(url=url+'/v1/beacons/create_beacon', data={'beacon': BEACON1}, timeout=30).json()
        #
        # except requests.ConnectionError as e:
        #     print(e)
            #time.sleep(0.01)

        # beacon1 = json.dumps(response)
        #
        # assert beacon1 != None
        # assert beacon1['id'] == BEACON1['id']
        # assert beacon1['site_id'] == BEACON1['site_id']
        # assert beacon1['udi'] == BEACON1['udi']
        # assert beacon1['type'] == BEACON1['type']
        # assert beacon1['label'] == BEACON1['label']
        # assert beacon1['center'] != None
