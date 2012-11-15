import unittest
import gradeconvert

class GradeConvertTest(unittest.TestCase):

    def test_contains_yos_grade(self):
        for key in gradeconvert.yos.keys():
            print "Expected yos grade: " + str(key)
            self.assertTrue(gradeconvert.contains_yos_grade(key))

    def test_contains_french_grade(self):
        for key in gradeconvert.french.keys():
            print "Expected french grade: " + str(key)
            self.assertTrue(gradeconvert.contains_french_grade(key))

    def test_contains_font_grade(self):
        for key in gradeconvert.font.keys():
            print "Expected font grade: " + str(key)
            self.assertTrue(gradeconvert.contains_font_grade(key))

    def test_contains_v_grade(self):
        for key in gradeconvert.v.keys():
            print "Expected v grade: " + str(key)
            self.assertTrue(gradeconvert.contains_v_grade(key))


