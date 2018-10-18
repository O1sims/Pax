from unittest import TestCase
from analytics import Criticality

import json

class TestCalculateAssetImpact(TestCase):

    def test_correct_input_output1(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "3",
                 "id" : "POWER-STATION-BIL1",
                 "integrity" : "4",
                 "availability" : "5"
            },
            "otherdata2": "something2"
        }

        self.assertEqual(Criticality.calculate_asset_impact(asset), 80)

    def test_correct_input_output2(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "2",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "2"
            },
            "otherdata2": "something2"
        }

        self.assertEqual(Criticality.calculate_asset_impact(asset), 46)

    def test_exception_is_raised1(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "-1",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "2"
            },
            "otherdata2": "something2"
        }

        self.assertRaises(Criticality.AssetImpactValueOutOfRange, Criticality.calculate_asset_impact, asset)

    def test_exception_is_raised2(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "1",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "20"
            },
            "otherdata2": "something2"
        }

        self.assertRaises(Criticality.AssetImpactValueOutOfRange, Criticality.calculate_asset_impact, asset)


class TestCalculateAssetCriticality(TestCase):

    def test_correct_input_output1(self):
        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "3",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "4",
                "availability" : "5"
            },
            "otherdata2": "something2",
            "sensitivity" : 3
        }

        self.assertEqual(Criticality.calculate_asset_criticality(asset), 48)


    def test_correct_input_output2(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "2",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "2"
            },
            "otherdata2": "something2",
            "sensitivity" : 2
        }

        self.assertEqual(Criticality.calculate_asset_criticality(asset), 18)

    def test_sensitivity_missing(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "2",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "2"
            },
            "otherdata2": "something2",
        }

        self.assertEqual(Criticality.calculate_asset_criticality(asset), 36)

    def test_exception_is_raised1(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "1",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "2"
            },
            "otherdata2": "something2",
            "sensitivity" : -1
        }

        self.assertRaises(Criticality.AssetImpactValueOutOfRange,
                          Criticality.calculate_asset_criticality, asset)


    def test_exception_is_raised2(self):

        asset = {
            "otherdata1": "something",
            "impact" : {
                "confidentiality" : "1",
                "id" : "POWER-STATION-BIL1",
                "integrity" : "3",
                "availability" : "1"
            },
            "otherdata2": "something2",
            "sensitivity" : 6
        }

        self.assertRaises(Criticality.AssetImpactValueOutOfRange,
                          Criticality.calculate_asset_criticality, asset)


class TestHighestCriticalityAsset(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestHighestCriticalityAsset, self).__init__(*args, **kwargs)
        self.filename = "./tests/data/assets.json"

    def test_correct_input_output1(self):

        data = json.load(open(self.filename))

        data[2]["sensitivity"] = 4

        self.assertEqual(Criticality.highest_criticality_asset(data), data[2])

    def test_correct_input_output2(self):

        data = json.load(open(self.filename))

        data[0]["sensitivity"] = 4

        self.assertEqual(Criticality.highest_criticality_asset(data), data[0])

    def test_correct_input_output3(self):

        data = json.load(open(self.filename))

        data[1]["sensitivity"] = 4

        self.assertEqual(Criticality.highest_criticality_asset(data), data[1])



