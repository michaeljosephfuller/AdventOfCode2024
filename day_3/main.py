'''Advent of Code Day 3: Mull It Over

https://adventofcode.com/2024/day/3

The solution class below takes a text file ("day_3/corrupted_data.txt"), which contains substrings
of the form "mul(x,y)" where x, y are integers, and finds:

(i) the sum of all multiplications of x and y in instances of "mul(x,y)"
(ii) the same sum but only counting "enabled" multiplications. 

Multiplications are "enabled" and "disabled" by the substrings "do()" and "don't()" rescpectively:
any instance of "mul(x,y)" found after a "don't()" substring won't count, until a "do()" substring
appears.

My solution leverages the RegEx Python package, re.'''


import re


class Solution:
    def __init__(self, 
                 filepath: str = "day_3/corrupted_data.txt", 
                 text: str = None
                 ):
        self.filepath = filepath
        self.text = text or self._read_file()
    

    def _read_file(self) -> str:
        '''Convert the text file at self.filepath to a string object'''
        with open(self.filepath, "r") as file:
            data = file.read()
        return data.replace("\n","")
    

    def _list_of_muls(self) -> list[str]:
        '''Use RegEx to return a list of tuples of all pairs of numbers found inside mul() in self.text'''
        list = re.findall("mul\((\d+),(\d+)\)", self.text)
        return [(int(item[0]), int(item[1])) for item in list]
    

    def sum_of_multiplications(self):
        '''Return the sum of all multiplications'''
        list = self._list_of_muls()
        return sum(tuple[0] * tuple[1] for tuple in list)
    

    def remove_disabled_multiplications(self):
        '''Update self.text with all disabled multiplications removed'''
        # Fully sandwiched don't() ... do()
        disabled_substrings_full = re.findall("don't\(\).*?do\(\)", self.text)
        self._remove_substrings(disabled_substrings_full)

        # Edge case: don't()... at the end
        disabled_substrings_end = re.findall("don't\(\).*", self.text)
        self._remove_substrings(disabled_substrings_end)


    def _remove_substrings(self, substrings: list[str]):
        '''Update self.text with substrings removed'''
        for substring in substrings:
            # print(substring, "\n")
            self.text = self.text.replace(substring, "") 


if __name__ == "__main__":
    solution = Solution()
    print(f"Part 1 solution: {solution.sum_of_multiplications()}")
    solution.remove_disabled_multiplications()
    print(f"Part 2 solution: {solution.sum_of_multiplications()}")
    