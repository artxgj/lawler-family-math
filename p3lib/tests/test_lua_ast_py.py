import sys
sys.path.append('../')

import unittest
from lua_ast_py import LuaSimpleRhs


class TestLuaSimpleRhs(unittest.TestCase):
    def setUp(self) -> None:
        self.intnum = 10
        self.floatnum = 19
        self.s = '算法'
        self.table = {'f(1)': 'g', 1: 'x', 2: 'y', 'x': 1, 3: 'f(x)', 30: 23, 4: 45, 'kj': True, 5: None, 6: False, 'ksl': {1: 'intelligence', 2: 'beauty'}}
        self.noun_python = {1: 'snake', 2: 'language'}

        chunk = """
            intvar = %s
            floatvar = %s
            strvar = '%s'
            truevar = true
            falsevar = false
            nilvar = nil
            tablevar = { [f(1)] = g; "x", "y"; x = 1, f(x),  [30] = 23; 45; [kj] = true; nil; false; ["ksl"] = {"intelligence", "beauty"} }
            noun["python"] = {"snake", "language"}
        """ % (self.intnum, self.floatnum, self.s)
        self.rhs = LuaSimpleRhs(chunk)

    def test_nil(self):
        expr = self.rhs.assign_name('nilvar')
        self.assertIsNone(expr)

    def test_str(self):
        self.assertEqual(self.rhs.assign_name('strvar'), self.s)

    def test_int(self):
        self.assertEqual(self.rhs.assign_name('intvar'), self.intnum)

    def test_float(self):
        self.assertEqual(self.rhs.assign_name('floatvar'), self.floatnum)

    def test_true(self):
        self.assertTrue(self.rhs.assign_name('truevar'))

    def test_false(self):
        self.assertFalse(self.rhs.assign_name('falsevar'))

    def test_table(self):
        self.assertEqual(self.rhs.assign_name('tablevar'), self.table)

    def test_assign_index(self):
        self.assertEqual(self.rhs.assign_index('python', 'noun'), self.noun_python)

    def test_return_int(self):
        rhs = LuaSimpleRhs('return 10')
        self.assertEqual(rhs.return_exp(), 10)

    def test_return_table(self):
        rhs = LuaSimpleRhs('return {["ksl"] = 17}')
        self.assertEqual(rhs.return_exp(), {'ksl': 17})
