# -*- coding: utf-8 -*-
"""
    step7.test.TestBeaconMongoDbPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    TestBeaconMongoDbPersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
import os

from pip_services3_commons.config import ConfigParams

from step7.src.persistence.BeaconsMongoDbPersistence import BeaconsMongoDbPersistence
from .BeaconsPersistenceFixture import BeaconsPersistenceFixture


class TestBeaconMongoDbPersistence():
    persistence = None
    fixture = None

    mongoUri = os.getenv('MONGO_URI')
    mongoHost = os.getenv('MONGO_HOST') if os.getenv('MONGO_HOST') != None else 'localhost'
    mongoPort = os.getenv('MONGO_PORT') if os.getenv('MONGO_PORT') != None else 27017
    mongoDatabase = os.getenv('MONGO_DB') if os.getenv('MONGO_DB') != None else 'test'

    @classmethod
    def setup_class(cls):
        if cls.mongoUri == None and cls.mongoHost == None:
            return

        db_config = ConfigParams.from_tuples('connection.uri', cls.mongoUri,
                                             'connection.host', cls.mongoHost,
                                             'connection.port', cls.mongoPort,
                                             'connection.database', cls.mongoDatabase)
        cls.persistence = BeaconsMongoDbPersistence()
        cls.fixture = BeaconsPersistenceFixture(cls.persistence)

        cls.persistence.configure(db_config)
        cls.persistence.open(None)

    @classmethod
    def teardown_class(cls):
        cls.persistence.close(None)

    def setup_method(self, method):
        self.persistence.clear(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_get_with_filter(self):
        self.fixture.test_get_with_filter()