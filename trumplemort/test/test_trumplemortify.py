import unittest
from trumplemort import trumplemortify

class TestTrumplemortification(unittest.TestCase):

    def test_basic_mortification(self):
        terms = (("([Bb]arak )?Obama", "Dumbledore"), ("[Ii]slam", "Mudblood"))

        status = "Barak Obama is an Islam fan"
        expected = "Dumbledore is an Mudblood fan"

        mortified = trumplemortify.trumplemortify(status, terms)

        self.assertEqual(mortified, expected)

    def test_case_insensitive_mortification(self):
        terms = (("(Barak )?Obama", "Dumbledore"), ("Islam", "Mudblood"))

        status = "obama is an Islam fan"
        expected = "Dumbledore is an Mudblood fan"

        mortified = trumplemortify.trumplemortify(status, terms)

        self.assertEqual(mortified, expected)




if __name__ == '__main__':
    unittest.main()