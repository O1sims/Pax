from unittest import TestCase
from mock import patch

from analytics import SystemAnalysis
from tests.mocks import mock_requests

class TestRiskLabel(TestCase):

    @patch("analytics.SystemAnalysis.config")
    def test_get_mission_data_from_system_id(self, c2_config):

        c2_config.C2_REST = "C2_REST/"


        with patch("analytics.SystemAnalysis.requests", mock_requests) as r_mock:

            missions = [{
                    "globalId": "id1"
                },
                {
                    "globalId": "id2"
                },
                {
                    "globalId": "id3"
                }]

            valid = {
                "systems": [
                    {"id": "sysid3"}
                ]
            }

            r_mock.replies = {
                "http://{}missions".format(c2_config.C2_REST): missions,
                "http://{}missions/{}".format(c2_config.C2_REST, "id1"):
                    {
                        "systems": [
                            {"id": "sysid1"}
                        ]
                    },
                "http://{}missions/{}".format(c2_config.C2_REST, "id2"):
                    {
                        "systems": [
                            {"id": "sysid2"}
                        ]
                    },
                "http://{}missions/{}".format(c2_config.C2_REST, "id3"): valid

            }


            self.assertEqual(SystemAnalysis.get_mission_data_from_system_id("sysid3"),
                             valid)

class TestSystemGeolocation(TestCase):

    @patch("analytics.SystemAnalysis.config")
    def test_system_geolocation(self, c2_config):

        c2_config.C2_REST = "C2_REST/"


        with patch("analytics.SystemAnalysis.requests", mock_requests) as r_mock:

            missions = [{
                "globalId": "id1"
            },
            {
                "globalId": "id2"
            },
            {
                "globalId": "id3"
            }]

            r_mock.replies = {
                "http://{}missions".format(c2_config.C2_REST): missions,
                "http://{}missions/{}".format(c2_config.C2_REST, "id1"):
                    {
                        "systems": [
                            {"id": "sysid1"}
                        ],
                        "bbox": "1,1,2,2"
                    },
                "http://{}missions/{}".format(c2_config.C2_REST, "id2"):
                    {
                        "systems": [
                            {"id": "sysid2"}
                        ],
                        "bbox": "3,3,4,4"
                    },
                "http://{}missions/{}".format(c2_config.C2_REST, "id3"):
                    {
                        "systems": [
                            {"id": "sysid3"}],
                        "bbox": "5,6,7,8"
                    }

            }

            mission_coordinates = {
                'longitude': (5.0 + 7.0) / 2,
                'latitude': (6.0 + 8.0) / 2
            }


            self.assertEqual(SystemAnalysis.system_geolocation("sysid3"),
                             mission_coordinates)


def mock_offensive_or_defensive(action):
    actions = {
        "SECURE": "offensive",
        "PROTECT": "defensive",
        "HOLD": "defensive",
        "DESTORY": "offensive"
    }

    return actions[action]

def mock_get_unit_data(unit_id):
    unitdata = {
        "actor1": {
            "name": "actor1_name"
        },
        "actor2": {
            "name": "actor2_name"
        }
    }

    return unitdata[unit_id]


class TestRemoveAssetVulnerabilities(TestCase):

    @patch("analytics.SystemAnalysis.offensive_or_defensive", mock_offensive_or_defensive)
    def test_remove_asset_vulnerabilities(self):

        action_data = [
            {
                "effect": "SECURE",
                "objective": "Object1"
            },
            {
                "effect": "MOVE"
            },
            {
                "effect": "PROTECT",
                "objective": "Object10"
            },
            {
                "effect": "MOVE",
            },
            {
                "effect": "DESTORY",
                "objective": "Object1"
            },
            {
                "effect": "MOVE"
            },
            {
                "effect": "HOLD",
                "objective": "Object3"
            }
        ]

        remaining = {
            "id": "idv2",
            "assets": ["Ojbect10", "Object11"]
        }

        system_data = {
            "vulnerabilities": [
                {
                    "id": "idv1",
                    "assets": ["Object2", "Object3"]
                },
                remaining,
                {
                    "id": "idv3",
                    "assets": ["Object1", "Object3"]
                }
            ]
        }

        result = {
            "vulnerabilities": [remaining]
        }
        # @todo Confirm that functions is suppose to remove the whole vulnerabilities map and not just the defensive assets
        self.assertEqual(SystemAnalysis.remove_asset_vulnerabilities(system_data, action_data), result)



class TestGetAssetCoordinates(TestCase):

    # @todo remove mock of offensive_or_defensive
    @patch("analytics.SystemAnalysis.offensive_or_defensive", mock_offensive_or_defensive)
    @patch("analytics.SystemAnalysis.get_unit_data", mock_get_unit_data)
    def test_add_asset_threats_with_threats(self):

        action_data = [
            {
                "effect": "SECURE",
                "objective": "Object1",
                "actor": "actor1"
            },
            {
                "effect": "MOVE"
            },
            {
                "effect": "PROTECT",
                "objective": "Object10",
                "actor": "actor2"
            },
            {
                "effect": "MOVE",
            },
            {
                "effect": "DESTORY",
                "objective": "Object5",
                "actor": "actor2"
            },
            {
                "effect": "MOVE"
            },
            {
                "effect": "HOLD",
                "objective": "Object3",
                "actor": "actor1"
            }
        ]

        system_data = {
            "threats": [
                {
                    "assetsThreatened": ["Object8"],
                    "name": "actor5_name",
                    "threatLevel": "CRITICAL"
                }
            ]
        }


        results = {
            "threats": [
                {
                    "assetsThreatened": ["Object8"],
                    "name": "actor5_name",
                    "threatLevel": "CRITICAL"
                },
                {
                    "assetsThreatened": ["Object1"],
                    "name": "actor1_name",
                    "threatLevel": "CRITICAL"
                },
                {
                    "assetsThreatened": ["Object5"],
                    "name": "actor2_name",
                    "threatLevel": "CRITICAL"
                }]
        }

        self.assertEquals(SystemAnalysis.add_asset_threats(system_data, action_data), results)

    # @todo remove mocks of get_unit_data and offensive_or_defensive
    @patch("analytics.SystemAnalysis.offensive_or_defensive", mock_offensive_or_defensive)
    @patch("analytics.SystemAnalysis.get_unit_data", mock_get_unit_data)
    def test_add_asset_threats_without_threats(self):

        action_data = [
            {
                "effect": "SECURE",
                "objective": "Object1",
                "actor": "actor1" # Cannot find reference to action["actor"] type but it is required by the function
            },
            {
                "effect": "MOVE"
            },
            {
                "effect": "PROTECT",
                "objective": "Object10",
                "actor": "actor2"
            },
            {
                "effect": "MOVE",
            },
            {
                "effect": "DESTORY",
                "objective": "Object5",
                "actor": "actor2"
            },
            {
                "effect": "MOVE"
            },
            {
                "effect": "HOLD",
                "objective": "Object3",
                "actor": "actor1"
            }
        ]

        system_data = {}

        results = {
            "threats": [
                {
                    "assetsThreatened": ["Object1"],
                    "name": "actor1_name",
                    "threatLevel": "CRITICAL"
                },
                {
                    "assetsThreatened": ["Object5"],
                    "name": "actor2_name",
                    "threatLevel": "CRITICAL"
                }]
        }

        self.assertEquals(SystemAnalysis.add_asset_threats(system_data, action_data), results)



