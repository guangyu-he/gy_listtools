import gy_listtools
import ast


class GyList:
    def __init__(self, a_list: list, dtype: str = None):
        self.a_list: list[str] = list(map(str, a_list))
        self.dtype: str = dtype

    def return_its_own_type(self, str_list: list[str]) -> list:

        if self.dtype is None or self.dtype == "fast" or self.dtype == "str":
            # do not process the type of elements in the list or elements are already string type
            return str_list
        elif self.dtype == "int" or self.dtype == "d":
            for index, each_item in enumerate(str_list):
                try:
                    # try to convert to int
                    int_item = int(each_item)
                    str_list[index] = int_item
                except ValueError:
                    raise ValueError(
                        f"Can not convert '{each_item}' into int type, please considering using dtype='force'")
        elif self.dtype == "float" or self.dtype == "f":
            for index, each_item in enumerate(str_list):
                try:
                    # try to convert to float
                    float_item = float(each_item)
                    str_list[index] = float_item
                except ValueError:
                    raise ValueError(
                        f"Can not convert '{each_item}' into float type, please considering using dtype='force'")
        elif self.dtype == "dict":
            for index, each_item in enumerate(str_list):
                try:
                    # try to convert to dict
                    dict_item = ast.literal_eval(each_item)
                    str_list[index] = dict_item
                except:
                    raise ValueError(
                        f"Can not convert '{each_item}' into dict type, please considering using dtype='force'")
        elif self.dtype == "force":
            # try to convert as it could be, could take some time
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
        else:
            raise ValueError(f"{self.dtype} is an invalid dtype argument")

        return str_list

    def remove_by_index(self, index: int) -> list:

        return self.return_its_own_type(gy_listtools.remove_element_by_index(self.a_list, index))

    def remove_by_value(self, value: str) -> list:
        return self.return_its_own_type(gy_listtools.remove_element_by_value(self.a_list, value))

    def dedup(self) -> list:
        return self.return_its_own_type(gy_listtools.remove_duplicates(self.a_list))
