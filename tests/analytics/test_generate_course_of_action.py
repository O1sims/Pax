from analytics import CourseOfActionGeneration as COAG
from unittest import TestCase
import json


class TestGenerateCourseOfActon(TestCase):

    def test_process_task_list_breadth_1(self):

        data = json.load(open("tests/data/course_of_action_generation_data_1.json"))

        result = COAG.generate_course_action_breadth(data[5], data)

        expected_result = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']

        self.assertEqual(result, expected_result)


    def test_process_task_list_breadth_2(self):

        data = json.load(open("tests/data/course_of_action_generation_data_2.json"))

        result = COAG.generate_course_action_breadth(data[7], data)

        expected_result = ['A6', 'A5', 'A4', 'A2', 'A3', 'D2', 'A1', 'S1', 'D1']

        self.assertEqual(result, expected_result)

    def test_process_task_list_depth_1(self):

        data = json.load(open("tests/data/course_of_action_generation_data_1.json"))

        result = COAG.generate_course_action_depth(data[5], data)

        expected_result = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']

        self.assertEqual(result, expected_result)

    def test_process_task_list_depth_2(self):

        data = json.load(open("tests/data/course_of_action_generation_data_2.json"))

        result = COAG.generate_course_action_depth(data[7], data)

        expected_result = ['A6', 'A4', 'A3', 'A1', 'A5', 'A2', 'D2', 'S1', 'D1']

        self.assertEqual(result, expected_result)

    def test_remove_replicated_task_1(self):

        expected_result = ["D1", "S1", "D2", "A2", "A5", "A1", "A3", "A4", "A6"]

        data = ["D1", "S1", "D2", "A2", "A5", "A6", "A1", "A3", "A4", "A6"]
        
        result = COAG.remove_replicated_task(data)

        self.assertEqual(result, expected_result)

    def test_remove_replicated_task_2(self):

        data = ["D1", "S1", "D2", "A2", "D2", "A6", "A1", "A3", "A4", "A6"]

        expected_result = ["D1", "S1", "A2", "D2", "A1", "A3", "A4", "A6"]

        result = COAG.remove_replicated_task(data)

        self.assertEqual(result, expected_result)

    def test_extract_tasks_1(self):

        task_list = ["D1", "D2"]
        tasks = json.load(open("tests/data/course_of_action_generation_data_2.json"))

        expected_result = [
            {
                "taskId": "D1",
                "effect": "DISRUPT",
                "objective": "POWER-STATION-PROCESSING-NODE-C2",
                "actor": "JV3",
                "timeFrame": 2,
                "dependencies": [
                    "S1", "A1"
                ]
            },
            {
                "taskId": "D2",
                "effect": "DISRUPT",
                "objective": "POWER-STATION-FIREWALL-C1",
                "actor": "JV3",
                "timeFrame": 2,
                "dependencies": [
                    "A2"
                ]
            }
        ]

        result = COAG.extract_tasks(task_list, tasks)

        self.assertEqual(result, expected_result)

    def test_extract_tasks_2(self):

        task_list = ["A1", "D2"]
        tasks = json.load(open("tests/data/course_of_action_generation_data_2.json"))

        expected_result = [
            {
                "taskId": "A1",
                "effect": "ACCESS",
                "objective": "POWER-STATION-LOGIN-NODE-C1",
                "actor": "JV3",
                "timeFrame": 2,
                "dependencies": [
                    "A3"
                ]
            },
            {
                "taskId": "D2",
                "effect": "DISRUPT",
                "objective": "POWER-STATION-FIREWALL-C1",
                "actor": "JV3",
                "timeFrame": 2,
                "dependencies": [
                    "A2"
                ]
            }
        ]

        result = COAG.extract_tasks(task_list, tasks)

        self.assertEqual(result, expected_result)




