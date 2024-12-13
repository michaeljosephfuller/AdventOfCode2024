'''Advent of Code Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1

The solution class below takes a text file ("day_1/lists.txt"), which contains two vertical 
lists of numbers, and finds (i) the total distance of the lists, and (ii) the similarity score
of the lists, as defined in the problem above.'''


class Solution:
    def __init__(self, filepath: str = "day_1/lists.txt", separator: str = "   "):
        self.filepath: str = filepath
        self.separator: str = separator
        
        list_of_lines: list[str] = self._convert_text_file_lines_to_list() # e.g. ['100 261', '153 200', ...]
        self.left_list, self.right_list = self._convert_list_to_two_sorted_lists(list_of_lines) # e.g. [100, 153, ...], [200, 261, ...]
        assert len(self.left_list) == len(self.right_list)
        

    def _convert_text_file_lines_to_list(self) -> list[str]:
        '''Creates a list of strings of each line in self.filepath'''
        with open(self.filepath, "r") as file:
            data = file.read()
        return data.split("\n") 


    def _convert_list_to_two_sorted_lists(self, list: list[str]):
        '''Returns two lists, where elements of the input list are strings of numbers separated by self.separator'''
        left_list, right_list = [], []
        for item in list:
            sub_items = item.split(self.separator)
            assert len(sub_items) == 2
            left_list.append(int(sub_items[0]))
            right_list.append(int(sub_items[1]))
        left_list.sort()
        right_list.sort()
        return left_list, right_list
    

    def total_distance(self) -> int:
        '''Calculates the total distance of the left and right lists'''
        return sum(abs(self.left_list[i] - self.right_list[i]) for i in range(len(self.left_list)))


    def similarity_score(self) -> int:
        '''Calculates the similarity score of the left and right lists'''
        return sum(num * self.right_list.count(num) for num in self.left_list)


if __name__ == "__main__":
    solution = Solution()
    print(f"Total distance: {solution.total_distance()}")
    print(f"Similarity score: {solution.similarity_score()}")
