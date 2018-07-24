from unittest import TestCase

from analytics import RiskAnalysis

class TestGetUnattainableStrategies(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestGetUnattainableStrategies, self).__init__(*args, **kwargs)
        self.coa = {}
        self.restrictions = {}

    def setUp(self):

        self.coa = [{
            "courseOfAction":"course1",
            "totalTime": 10,
            "unitsRequired": 10,
            "probabilityOfCompletion": 10
        },
        {
            "courseOfAction":"course2",
            "totalTime": 10,
            "unitsRequired": 10,
            "probabilityOfCompletion": 10
        }]

        self.restrictions = {
            "missionTime": 10,
            "personnel": 10,
            "probability": 10
        }

    def test_all_fine(self):

        self.restrictions["missionTime"] = 11
        self.restrictions["personnel"] = 11
        self.restrictions["probability"] = 9

        self.assertEqual(len(RiskAnalysis.get_unattainable_strategies(self.restrictions, self.coa)),
                         0)

    def test_get_unattainable_strategies_total_time(self):

        self.coa[1]["totalTime"] = 8
        self.restrictions["missionTime"] = 9

        self.run_message_test("time")

    def test_get_unattainable_strategies_personnel(self):

        self.coa[1]["unitsRequired"] = 8
        self.restrictions["personnel"] = 9

        self.run_message_test("personnel")

    def test_get_unattainable_strategies_probability(self):

        self.coa[0]["probabilityOfCompletion"] = 6
        self.restrictions["probability"] = 9

        self.run_message_test("probability")


    def run_message_test(self, message):

        result = RiskAnalysis.get_unattainable_strategies(self.restrictions, self.coa)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["courseOfAction"], self.coa[0]["courseOfAction"])
        self.assertEqual(len(result[0]["reason"]), 1)
        self.assertEqual(result[0]["reason"][0], RiskAnalysis.unattainable_strategies_messages[message])


    def test_get_unattainable_strategies_all(self):

        self.coa[1]["totalTime"] = 8
        self.restrictions["missionTime"] = 9
        self.coa[1]["unitsRequired"] = 8
        self.restrictions["personnel"] = 9

        self.coa[1]["probabilityOfCompletion"] = 6
        self.restrictions["probability"] = 9

        result = RiskAnalysis.get_unattainable_strategies(self.restrictions, self.coa)
        self.assertEqual(len(result), 2)

        for r in result:

            if r["courseOfAction"] == self.coa[1]["courseOfAction"]:
                self.assertEqual(len(result[1]["reason"]), 1)
                self.assertEqual(result[1]["reason"][0], RiskAnalysis.unattainable_strategies_messages["probability"])
            elif r["courseOfAction"] == self.coa[0]["courseOfAction"]:
                self.assertEqual(len(result[0]["reason"]), 2)
                for m in result[0]["reason"]:
                    self.assertTrue(
                        m == RiskAnalysis.unattainable_strategies_messages["time"] or
                        m == RiskAnalysis.unattainable_strategies_messages["personnel"],
                        "m is {}".format(m)
                    )
            else:
                self.assertTrue(False, "Unknown value {} in courseOfAction field".format(r["courseOfAction"]))

class TestRemoveUnattainableStrategies(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRemoveUnattainableStrategies, self).__init__(*args, **kwargs)
        self.coa = {}
        self.restrictions = {}

    def setUp(self):
        self.coa = [{
            "courseOfAction":"course1",
            "totalTime": 10,
            "unitsRequired": 10,
            "probabilityOfCompletion": 10
        },
            {
                "courseOfAction":"course2",
                "totalTime": 10,
                "unitsRequired": 10,
                "probabilityOfCompletion": 10
            }]

        self.restrictions = {
            "missionTime": 10,
            "personnel": 10,
            "probability": 10
        }


    def test_remove_course_of_action1(self):

        self.coa[1]["totalTime"] = 8
        self.restrictions["missionTime"] = 9

        coas_remove = RiskAnalysis.get_unattainable_strategies(self.restrictions, self.coa)
        result = RiskAnalysis.remove_unattainable_strategies(self.coa, coas_remove)

        test = [{
            "courseOfAction":"course2",
            "totalTime": 8,
            "unitsRequired": 10,
            "probabilityOfCompletion": 10
        }]

        self.assertEqual(result, test)

    def test_remove_course_of_action2(self):

        self.coa[1]["probabilityOfCompletion"] = 6
        self.restrictions["probability"] = 9

        coas_remove = RiskAnalysis.get_unattainable_strategies(self.restrictions, self.coa)
        result = RiskAnalysis.remove_unattainable_strategies(self.coa, coas_remove)

        test = [{
            "courseOfAction":"course1",
            "totalTime": 10,
            "unitsRequired": 10,
            "probabilityOfCompletion": 10
        }]

        self.assertEqual(result, test)

    def test_remove_coourse_of_action_empty_comparative_statics(self):

        self.coa[1]["probabilityOfCompletion"] = 6
        self.restrictions["probability"] = 9

        coas_remove = RiskAnalysis.get_unattainable_strategies(self.restrictions, self.coa)
        result = RiskAnalysis.remove_unattainable_strategies([], coas_remove)

        self.assertEqual(len(result), 0)




