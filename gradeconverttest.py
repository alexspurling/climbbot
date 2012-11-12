import unittest
import gradeconvert

class GradeConvertTest(unittest.TestCase):

    def test_is_yos(self):
        self.assertFalse(gradeconvert.is_yos("5.0"))
        self.assertTrue(gradeconvert.is_yos("5.1"))
        self.assertTrue(gradeconvert.is_yos("5.2"))
        self.assertTrue(gradeconvert.is_yos("5.3"))
        self.assertTrue(gradeconvert.is_yos("5.4"))
        self.assertTrue(gradeconvert.is_yos("5.5"))
        self.assertTrue(gradeconvert.is_yos("5.6"))
        self.assertTrue(gradeconvert.is_yos("5.7"))
        self.assertTrue(gradeconvert.is_yos("5.8"))
        self.assertTrue(gradeconvert.is_yos("5.9"))
        self.assertTrue(gradeconvert.is_yos("5.10"))
        self.assertTrue(gradeconvert.is_yos("5.11"))
        self.assertTrue(gradeconvert.is_yos("5.12"))
        self.assertTrue(gradeconvert.is_yos("5.13"))
        self.assertTrue(gradeconvert.is_yos("5.14"))
        self.assertTrue(gradeconvert.is_yos("5.15"))
        self.assertFalse(gradeconvert.is_yos("5.16"))

        self.assertTrue(gradeconvert.is_yos("5.10a"))
        self.assertTrue(gradeconvert.is_yos("5.10b"))
        self.assertTrue(gradeconvert.is_yos("5.10c"))
        self.assertTrue(gradeconvert.is_yos("5.10d"))
        self.assertFalse(gradeconvert.is_yos("5.10f"))

        self.assertTrue(gradeconvert.is_yos("5.15a"))
        self.assertTrue(gradeconvert.is_yos("5.15b"))
        self.assertTrue(gradeconvert.is_yos("5.15c"))
        self.assertTrue(gradeconvert.is_yos("5.15d"))
        self.assertFalse(gradeconvert.is_yos("5.15f"))

        self.assertFalse(gradeconvert.is_yos("5.9a"))
        self.assertFalse(gradeconvert.is_yos("5.9b"))
        self.assertFalse(gradeconvert.is_yos("5.9c"))
        self.assertFalse(gradeconvert.is_yos("5.9d"))

    def test_is_french(self):
        self.assertTrue(gradeconvert.is_french("1"))
        self.assertTrue(gradeconvert.is_french("2"))
        self.assertTrue(gradeconvert.is_french("3"))
        self.assertTrue(gradeconvert.is_french("4"))
        self.assertTrue(gradeconvert.is_french("5"))
        self.assertTrue(gradeconvert.is_french("6"))
        self.assertTrue(gradeconvert.is_french("7"))
        self.assertTrue(gradeconvert.is_french("8"))
        self.assertTrue(gradeconvert.is_french("9"))
        self.assertFalse(gradeconvert.is_french("10"))

        self.assertFalse(gradeconvert.is_french("1a"))
        self.assertFalse(gradeconvert.is_french("2a"))
        self.assertFalse(gradeconvert.is_french("3a"))

        self.assertTrue(gradeconvert.is_french("4a"))
        self.assertTrue(gradeconvert.is_french("4b"))
        self.assertTrue(gradeconvert.is_french("4c"))
        self.assertFalse(gradeconvert.is_french("4d"))

        self.assertTrue(gradeconvert.is_french("5a"))
        self.assertTrue(gradeconvert.is_french("5b"))
        self.assertTrue(gradeconvert.is_french("5c"))

        self.assertTrue(gradeconvert.is_french("4+"))
        self.assertTrue(gradeconvert.is_french("5+"))

        self.assertTrue(gradeconvert.is_french("6a+"))
        self.assertTrue(gradeconvert.is_french("6b+"))
        self.assertTrue(gradeconvert.is_french("6c+"))
        self.assertTrue(gradeconvert.is_french("9a+"))
        self.assertTrue(gradeconvert.is_french("9b+"))
        self.assertTrue(gradeconvert.is_french("9c+"))

        self.assertFalse(gradeconvert.is_french("9d"))

        #Actually these are font bouldering grades
        self.assertFalse(gradeconvert.is_french("1A"))
        self.assertFalse(gradeconvert.is_french("2A"))
        self.assertFalse(gradeconvert.is_french("3A"))

        self.assertTrue(gradeconvert.is_french("4A"))
        self.assertTrue(gradeconvert.is_french("4B"))
        self.assertTrue(gradeconvert.is_french("4C"))
        self.assertFalse(gradeconvert.is_french("4D"))

        self.assertTrue(gradeconvert.is_french("5A"))
        self.assertTrue(gradeconvert.is_french("5B"))
        self.assertTrue(gradeconvert.is_french("5C"))
        self.assertTrue(gradeconvert.is_french("6A+"))
        self.assertTrue(gradeconvert.is_french("6B+"))
        self.assertTrue(gradeconvert.is_french("6C+"))
        self.assertTrue(gradeconvert.is_french("9A+"))
        self.assertTrue(gradeconvert.is_french("9B+"))
        self.assertTrue(gradeconvert.is_french("9C+"))

        self.assertFalse(gradeconvert.is_french("9D"))


