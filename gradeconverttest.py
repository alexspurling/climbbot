import unittest
import gradeconvert

class GradeConvertTest(unittest.TestCase):

    def test_get_yos_grade(self):
        for key in gradeconvert.yos.keys():
            print "Expected yos grade: " + str(key)
            self.assertTrue(gradeconvert.get_yos_grade(key))

    def test_get_french_grade(self):
        for key in gradeconvert.french.keys():
            print "Expected french grade: " + str(key)
            self.assertTrue(gradeconvert.get_french_grade(key))

    def test_get_font_grade(self):
        for key in gradeconvert.font.keys():
            print "Expected font grade: " + str(key)
            self.assertTrue(gradeconvert.get_font_grade(key))

    def test_get_v_grade(self):
        for key in gradeconvert.v.keys():
            print "Expected v grade: " + str(key)
            self.assertTrue(gradeconvert.get_v_grade(key))


