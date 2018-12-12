# -*- coding: utf-8 -*-
"""
    step4.data.version1.BeaconV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconV1 class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class BeaconV1(dict):
    def __init__(self, id, site_id, type, udi, label, center, radius):
        self['id'] = id
        self['site_id'] = site_id
        self['type'] = type
        self['udi'] = udi
        self['label'] = label
        self['center'] = center
        self['radius'] = radius

    # _id = None
    # _siteId = None
    # _type = None
    # _udi = None
    # _label = None
    # _center = None
    # _radius = 0.0
    #
    # def __init__(self, id, siteId, type, udi, label, center, radius):
    #     self._id = id
    #     self._siteId = siteId
    #     self._type = type
    #     self._udi = udi
    #     self._label = label
    #     self._center = center
    #     self._radius = radius

