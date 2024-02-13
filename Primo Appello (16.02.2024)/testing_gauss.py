import unittest
from esame import CSVTimeSeriesFile, compute_increments, ExamException

score = 0

class TestComputeIncrements(unittest.TestCase):
    
    def test_get_data(self):
        file = CSVTimeSeriesFile('data/data.csv')
        data = file.get_data()
        self.assertEqual(len(data), 3) 
        self.assertEqual(data[0], ['1949-01', 90])
        self.assertEqual(data[-1], ['1950-11', 100])
        
        global score
        score += 4
    
    def test_get_data_missing_file(self):
        with self.assertRaises(ExamException):
            CSVTimeSeriesFile('data/missing.csv')
        
        global score
        score += 1
        
    def test_get_data_empty_file(self):
        with self.assertRaises(ExamException):
            CSVTimeSeriesFile('data/empty.csv')
        
        global score
        score += 1
        
    def test_get_data_incorrect_header(self):
        file = CSVTimeSeriesFile('data/incorrect_header.csv')
        with self.assertRaises(ExamException):
            file.get_data()
        
        global score
        score += 1
    
    def test_get_data_invalid_rows(self):
        file = CSVTimeSeriesFile('data/invalid_rows.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_out_of_order(self):
        file = CSVTimeSeriesFile('data/dates_out_of_order.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_dates_incorrect_format(self):
        file = CSVTimeSeriesFile('data/dates_incorrect_format.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_months_range(self):
        file = CSVTimeSeriesFile('data/months_range.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_duplicate_dates(self):
        file = CSVTimeSeriesFile('data/duplicate_dates.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
    
    def test_get_data_months_out_of_order(self):
        file = CSVTimeSeriesFile('data/months_out_of_order.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_passengers_string(self):
        file = CSVTimeSeriesFile('data/passengers_string.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
        
    def test_get_data_passengers_float(self):
        file = CSVTimeSeriesFile('data/passengers_float.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
    
    def test_get_data_passengers_negative(self):
        file = CSVTimeSeriesFile('data/passengers_negative.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
    
    def test_get_data_passengers_zero(self):
        file = CSVTimeSeriesFile('data/passengers_zero.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1

    def test_normal(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2020' 
        last_year = '2021'
        expected = {'2020-2021': 25.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 4
        
    def test_fist_end_four_digits(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2020' 
        last_year = '921'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1
        
    def test_firs_end_not_digits(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2020' 
        last_year = 'test'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1

    def test_missing_year(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2022-01', 140], ['2022-02', 150]] 
        first_year = '2020'
        last_year = '2022'
        expected = {'2020-2022': 35.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1

    def test_empty_result(self):
        time_series = [['2020-01', 100], ['2022-01', 120]]
        first_year = '2020'
        last_year = '2021' 
        expected = {}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1

    def test_invalid_years(self):
        time_series = [['2020-01', 100], ['2020-02', 120]]
        first_year = '202'
        last_year = '2021'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1

    def test_years_not_in_order(self):
        time_series = [['2020-01', 100], ['2021-02', 120]]
        first_year = '2021'
        last_year = '2020'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)

        global score
        score += 1

    def test_years_not_in_data(self):
        time_series = [['2020-01', 100], ['2020-02', 120]]
        first_year = '2018'
        last_year = '2020'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
            
        global score
        score += 1
        
    def test_missing_first_year(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2019'
        last_year = '2021'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)

        global score
        score += 1
    
    def test_holes(self):
        time_series = [['2020-01', 100], ['2022-02', 120], ['2024-01', 130], ['2026-02', 140]]
        first_year = '2020'
        last_year = '2026'
        expected = {'2020-2022': 20.0, '2022-2024': 10.0, '2024-2026': 10.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1

    @classmethod
    def tearDownClass(cls):
        global score
        print('\n\n-------------')
        print('| Voto: {}  |'.format(score))
        print('-------------\n')


# Run the tests
if __name__ == "__main__":
    unittest.main()