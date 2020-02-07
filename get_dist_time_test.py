import unittest
import get_dist_time

class MainTest(unittest.TestCase):
	
	def test_time_to_min(self):
		test_case = ["0 hours 0 mins", "24 mins", "3 hours 3 mins", "80 hours"]
		expected_results = ['0', '24', '183', '4800']

		results = [get_dist_time.time_to_min(test) for test in test_case]
		self.assertEqual(results, expected_results)

	def test_get_estimated_time_and_distance(self):
		origin = 'MERIDIAN DIALYSIS CTR 1525 MERIDIAN AVE. SAN JOSE'
		destination = 'SCVMC 751 S. BASCOM AVE. SAN JOSE'

		status, result = get_dist_time.get_estimated_time_and_distance(origin, destination)
		self.assertEqual(len(result), 2)
		self.assertEqual(status, True)
		self.assertEqual(result[0], '2.7')
		self.assertEqual(result[1], '10')

	def test_get_number_of_route(self):
		line = '10,43,FRESNIUS KIDNEY CARE,2163 COUNTRY HILLS DRIVE,ANTIOCH,94509,17:22,,'
		expected = '10'
		self.assertEqual(expected, get_dist_time.get_number_of_route(line))

	def test_get_origin_and_destination(self):
		origin_line = '6,32,INVITAE,1400 16TH STREET,SAN FRANCISCO,94103,9:02,,'
		destination_line = '6,32,DR. TOIG,801 BREWSTER AVE.,REDWOOD CITY,94063,15:38,,'

		expected = ['INVITAE 1400 16TH STREET SAN FRANCISCO', 'DR. TOIG 801 BREWSTER AVE. REDWOOD CITY']
		origin, destination = get_dist_time.get_origin_and_destination(origin_line, destination_line)
		self.assertEqual(origin, expected[0])
		self.assertEqual(destination, expected[1])
