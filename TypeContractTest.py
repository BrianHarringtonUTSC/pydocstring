import unittest
import pydocstring as pydoc


class AcceptableTypeContractTest(unittest.TestCase):
    def test_TypeContract_Empty(self):
        theirs_tc = pydoc.DocString(func_none).get_type_contract()
        ours_tc = pydoc.TypeContract([], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Standard(self):
        theirs_tc = pydoc.DocString(func_standard).get_type_contract()
        ours_tc = pydoc.TypeContract(["int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Standard_Union(self):
        theirs_tc = pydoc.DocString(func_standard_union).get_type_contract()
        ours_tc = pydoc.TypeContract(["int or str"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_List_1(self):
        theirs_tc = pydoc.DocString(func_list1).get_type_contract()
        ours_tc = pydoc.TypeContract(["list"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_List_2(self):
        theirs_tc = pydoc.DocString(func_list2).get_type_contract()
        ours_tc = pydoc.TypeContract(["list of int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_List_Recursive(self):
        theirs_tc = pydoc.DocString(func_list_recursive).get_type_contract()
        ours_tc = pydoc.TypeContract(["list of list of list of list of int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_List_Union(self):
        theirs_tc = pydoc.DocString(func_list_union).get_type_contract()
        ours_tc = pydoc.TypeContract(["list of int or str"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Set_1(self):
        theirs_tc = pydoc.DocString(func_set1).get_type_contract()
        ours_tc = pydoc.TypeContract(["set"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Set_2(self):
        theirs_tc = pydoc.DocString(func_set2).get_type_contract()
        ours_tc = pydoc.TypeContract(["set of int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Set_Recursive(self):
        theirs_tc = pydoc.DocString(func_set_recursive).get_type_contract()
        ours_tc = pydoc.TypeContract(["set of set of set of set of int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Set_Union(self):
        theirs_tc = pydoc.DocString(func_set_union).get_type_contract()
        ours_tc = pydoc.TypeContract(["set of int or str"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Tuple_1(self):
        theirs_tc = pydoc.DocString(func_tuple1).get_type_contract()
        ours_tc = pydoc.TypeContract(["tuple"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Tuple_2(self):
        theirs_tc = pydoc.DocString(func_tuple2).get_type_contract()
        ours_tc = pydoc.TypeContract(["tuple of int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Tuple_Recursive(self):
        theirs_tc = pydoc.DocString(func_tuple_recursive).get_type_contract()
        ours_tc = pydoc.TypeContract(["tuple of tuple of tuple of tuple of int"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Tuple_Union(self):
        theirs_tc = pydoc.DocString(func_tuple_union).get_type_contract()
        ours_tc = pydoc.TypeContract(["tuple of int or str"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Dict_1(self):
        theirs_tc = pydoc.DocString(func_dict1).get_type_contract()
        ours_tc = pydoc.TypeContract(["dict"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Dict_2(self):
        theirs_tc = pydoc.DocString(func_dict2).get_type_contract()
        ours_tc = pydoc.TypeContract(["dict of {int:str}"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Dict_Recursive(self):
        theirs_tc = pydoc.DocString(func_dict_recursive).get_type_contract()
        ours_tc = pydoc.TypeContract(["dict of {dict of {dict: dict of {int:str}}:str}"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Dict_Union(self):
        theirs_tc = pydoc.DocString(func_dict_union).get_type_contract()
        ours_tc = pydoc.TypeContract(["dict of {int or str: int or str}"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Standard_Subclass(self):
        theirs_tc = pydoc.DocString(func_standard_subclass).get_type_contract()
        ours_tc = pydoc.TypeContract(["io.TextIOWrapper"], ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Mixed1(self):
        theirs_tc = pydoc.DocString(func_mixed1).get_type_contract()
        ours_tc = pydoc.TypeContract(["int", "io.TextIOWrapper", "dict", "set", "tuple"],
                                     ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Mixed2(self):
        theirs_tc = pydoc.DocString(func_mixed2).get_type_contract()
        ours_tc = pydoc.TypeContract(["int", "io.TextIOWrapper", "dict of {int:str}", "set of int", "tuple of int"],
                                     ["NoneType"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))

    def test_TypeContract_Mixed3(self):
        theirs_tc = pydoc.DocString(func_mixed3).get_type_contract()
        ours_tc = pydoc.TypeContract(["int", "io.TextIOWrapper", "dict of {int:str}", "set of int", "tuple of int"],
                                     ["int", "io.TextIOWrapper", "dict of {int:str}", "set of int", "tuple of int"])
        self.assertEqual(theirs_tc, ours_tc, "Type contract does not match. \"{}\" != \"{}\""
                         .format(theirs_tc, ours_tc))


def func_none():
    """() -> NoneType
    """


def func_standard():
    """(int) -> NoneType
    """


def func_standard_union():
    """(int or str) -> NoneType
    """


def func_list1():
    """(list) -> NoneType
    """


def func_list2():
    """(list of int) -> NoneType
    """


def func_list_union():
    """(list of int or str) -> NoneType
    """


def func_list_recursive():
    """(list of list of list of list of int) -> NoneType
    """


def func_set1():
    """(set) -> NoneType
    """


def func_set2():
    """(set of int) -> NoneType
    """


def func_set_union():
    """(set of int or str) -> NoneType
    """


def func_set_recursive():
    """(set of set of set of set of int) -> NoneType
    """


def func_tuple1():
    """(tuple) -> NoneType
    """


def func_tuple2():
    """(tuple of int) -> NoneType
    """


def func_tuple_union():
    """(tuple of int or str) -> NoneType
    """


def func_tuple_recursive():
    """(tuple of tuple of tuple of tuple of int) -> NoneType
    """


def func_dict1():
    """(dict) -> NoneType
    """


def func_dict2():
    """(dict of {int:str}) -> NoneType
    """


def func_dict_union():
    """(dict of {int or str: int or str}) -> NoneType
    """


def func_dict_recursive():
    """(dict of {dict of {dict: dict of {int:str}}:str}) -> NoneType
    """


def func_standard_subclass():
    """(io.TextIOWrapper) -> NoneType
    """


def func_mixed1():
    """(int, io.TextIOWrapper, dict, set, tuple) -> NoneType
    """


def func_mixed2():
    """(int, io.TextIOWrapper, dict of {int:str}, set of int, tuple of int) -> NoneType
    """


def func_mixed3():
    """(int, io.TextIOWrapper, dict of {int:str}, set of int, tuple of int)
    ->
    int, io.TextIOWrapper, dict of {int:str}, set of int, tuple of int
    """


# TODO test wrong/bad contracts
if __name__ == '__main__':
    unittest.main()
