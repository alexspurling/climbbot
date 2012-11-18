import unittest
import gradeconvert

class GradeConvertTest(unittest.TestCase):

#    def test_get_yos_grade(self):
#        for key in gradeconvert.yos_map.keys():
#            print "Expected yos grade: " + str(key)
#            self.assertTrue(gradeconvert.get_yos_grade(key))
#
#    def test_get_french_grade(self):
#        for key in gradeconvert.french_map.keys():
#            print "Expected french grade: " + str(key)
#            self.assertTrue(gradeconvert.get_french_grade(key))
#
#    def test_get_font_grade(self):
#        for key in gradeconvert.font_map.keys():
#            print "Expected font grade: " + str(key)
#            self.assertTrue(gradeconvert.get_font_grade(key))
#
#    def test_get_v_grade(self):
#        for key in gradeconvert.v_map.keys():
#            print "Expected v grade: " + str(key)
#            self.assertTrue(gradeconvert.get_v_grade(key))

    def test_contains_grade(self):
        self.assertTrue(gradeconvert.contains_grade("One v grade v9"))
        self.assertTrue(gradeconvert.contains_grade("Two v grades V10 v9"))
        self.assertTrue(gradeconvert.contains_grade("One yos grade 5.12d"))
        self.assertTrue(gradeconvert.contains_grade("Two yos grades 5.9 5.15c"))
        self.assertTrue(gradeconvert.contains_grade("One font grade 6A"))
        self.assertTrue(gradeconvert.contains_grade("Two font grades 8C+ 4+"))
        self.assertTrue(gradeconvert.contains_grade("One french grade 5 a"))
        self.assertTrue(gradeconvert.contains_grade("Two french grades F6c+ 4+"))

        self.assertTrue(gradeconvert.contains_grade("Two mixed grades 5.12d 3"))
        self.assertTrue(gradeconvert.contains_grade("Two mixed grades V12 5C"))

        self.assertFalse(gradeconvert.contains_grade("No valid grade VB+"))
        self.assertFalse(gradeconvert.contains_grade("FJ+"))


    def test_convert(self):
        self.assertEquals([('5.14c',), ('7C',)], gradeconvert.convert("What is F8c+? and V9"))
        self.assertEquals([('5.14c', 'V16'), ('7C',)], gradeconvert.convert("What is 8c+? and v9?"))
        self.assertEquals([('8A+',), ('V11',)], gradeconvert.convert("Why is SSD V12 but PI font 8A?"))



