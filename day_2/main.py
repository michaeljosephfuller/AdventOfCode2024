'''Advent of Code Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2

The solution class below takes a text file ("day_2/unusual_data.txt"), which contains lines of
"reports", and finds (i) the total number of "safe" reports, i.e. where a line is

- strictly increasing/decreasing
- any two adjacent levels (numbers) in a report differ by 1, 2, or 3

and (ii) the total number of safe "dampened" reports: as in the above, but it is permitted to
remove any one element of the report.'''


class Solution:
    def __init__(self, filepath: str = "day_2/unusual_data.txt", separator: str = " "):
        self.filepath: str = filepath
        self.separator: str = separator
        self.list_of_reports: list[list[int]] = self._convert_text_file_lines_to_list()
        

    def _convert_text_file_lines_to_list(self) -> list[list[int]]:
        '''Creates a list of reports of each line in self.filepath. Each report is a list of integers.'''
        with open(self.filepath, "r") as file:
            data = file.read()
            list_of_reports_str = [report.split(self.separator) for report in data.split("\n")] # e.g. [['1', '3', '4', '5', '2'], ['5', '7', '5', '3', '1'], ...]
        return [[int(level) for level in report] for report in list_of_reports_str] # e.g. [[1, 3, 4, 5, 2], [5, 7, 5, 3, 1], ...]


    def _report_is_safe(self, report: list[int]) -> bool:
        '''Return True if a report is safe'''

        # Initial check if report level variance too large 
        if self._level_variance_too_large(report[0], report[1]):
            # print(f"UNSAFE: report {report} has large variance")
            return False
        
        # Should the sequence be increasing or decreasing?
        increasing: bool = (report[1] > report[0])
        is_correctly_monotone: function = self._is_increasing if increasing else self._is_decreasing
    
        # Iterate through report, returning False at the first instance of a breach if necessary 
        for i in range(1, len(report) - 1):
            # Level variance check
            if self._level_variance_too_large(report[i], report[i+1]):
                # print(f"UNSAFE: report {report} has large variance")
                return False
            # Monotonicity check
            if not is_correctly_monotone(report[i], report[i+1]):
                # print(f"UNSAFE: report {report} fails monotonicity check")
                return False
        
        # print(f"SAFE: report {report} passes")
        return True
    

    def _dampened_report_is_safe(self, report: list[int]) -> bool:
        '''Return True if the report is is safe with '''
        for i in range(len(report)):
            dampened_report = report[:i] + report[i+1:]
            if self._report_is_safe(dampened_report):
                return True
        return False
    

    def _is_increasing(self, level_1: int, level_2: int) -> bool:
        return level_2 > level_1
    

    def _is_decreasing(self, level_1: int, level_2: int) -> bool:
        return level_2 < level_1

        
    def _level_variance_too_large(self, level_1: int, level_2: int) -> bool:
        '''Return True if the variance between two levels in a report is not 1, 2, or 3'''
        return abs(level_1 - level_2) not in [1, 2, 3]
    
    
    def _is_monotone(self, report: list[int]) -> bool:
        '''Return true if the input list is monotone.
        We ignore strictly monotone here as the function _correct_level_diffs() implicitly checks for this'''
        return (tuple(report.sort()) == tuple(report)) or (tuple(report.sort(reverse=True)) == tuple(report))
    

    def _correct_level_diffs(self, report: list[int]) -> bool:
        '''Return true if each level in a report differs by 1, 2, or 3'''
        diffs = [abs(report[i+1] - report[i]) for i in range(len(report) - 1)]
        incorrect_level_diffs = any(map(lambda x: x not in [1, 2, 3], diffs))
        return not incorrect_level_diffs
    
    
    def num_safe_reports(self) -> int:
        '''Returns the number of safe reports in self.list_of_reports'''
        return sum(self._report_is_safe(report) for report in self.list_of_reports)


    def num_safe_dampened_reports(self) -> int:
        '''Returns the number of safe dampened reports in self.list_of_reports'''
        return sum(self._dampened_report_is_safe(report) for report in self.list_of_reports)


if __name__ == "__main__":
    solution = Solution()
    print(f"Number of safe reports: {solution.num_safe_reports()}")
    print(f"Number of safe reports with Problem Dampener: {solution.num_safe_dampened_reports()}")
