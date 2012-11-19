import unittest
import gradeconvert

class GradeConvertTest(unittest.TestCase):

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
        #Success cases
        self.assertEquals("F8c+ is 5.14c, V9 is font 7C", gradeconvert.convert("What is F8c+? and V9"))
        self.assertEquals("8c+ is 5.14c or V16, v9 is font 7C", gradeconvert.convert("What is 8c+? and v9?"))
        self.assertEquals("V12 is font 8A+, font 8A is V11", gradeconvert.convert("Why is SSD V12 but PI font 8A?"))
        self.assertEquals("8A is 5.13b or V11, 8b+ is 5.14a or V14", gradeconvert.convert("8A8b+"))

        #Weird cases
        self.assertEquals("F7 is 5.11d", gradeconvert.convert("F7"))



