import gy_listtools


class GyList:
    def __init__(self, a_list: list):
        self.a_list = a_list

    def remove_by_index(self, index: int) -> list:
        return gy_listtools.remove_element_by_index(self.a_list, index)

    def remove_by_value(self, value: str) -> list:
        return gy_listtools.remove_element_by_value(self.a_list, value)

    def dedup(self) -> list:
        return gy_listtools.remove_duplicates(self.a_list)
