import gy_listtools
import ast


def return_its_own_type(str_list: list[str]) -> list:
    for index, each_item in enumerate(str_list):
        try:
            # try to convert to dict
            dict_item = ast.literal_eval(each_item)
            str_list[index] = dict_item
        except:
            # not a dict item
            try:
                # try to convert to int
                int_item = int(each_item)
                str_list[index] = int_item
            except ValueError:
                # not an int item
                try:
                    # try to convert to float
                    float_item = float(each_item)
                    str_list[index] = float_item
                except ValueError:
                    pass

    return str_list


class GyList:
    def __init__(self, a_list: list):
        self.a_list: list[str] = list(map(str, a_list))

    def remove_by_index(self, index: int) -> list:
        return return_its_own_type(gy_listtools.remove_element_by_index(self.a_list, index))

    def remove_by_value(self, value: str) -> list:
        return return_its_own_type(gy_listtools.remove_element_by_value(self.a_list, value))

    def dedup(self) -> list:
        return return_its_own_type(gy_listtools.remove_duplicates(self.a_list))
