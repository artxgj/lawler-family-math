from luaparser import ast, astnodes
from typing import Optional, Tuple, Any, Union


class LuaAstToPy:
    @staticmethod
    def table(tb: astnodes.Table) -> dict:
        pydict = {}

        for f in tb.fields:
            key, value = LuaAstToPy.field(f)
            if key is None and value is None:
                # f.key and f.value are not yet supported
                continue

            pydict[key] = value

        return pydict

    @staticmethod
    def field(f: astnodes.Field) -> Tuple[Any, Any]:
        """
        returns a key/value pair
        :return:
        """
        try:
            k = f.key
            v = f.value
            key = _luapy_dispatch[k.display_name](k)
            value = _luapy_dispatch[v.display_name](v)
            return key, value
        except KeyError as err:
            print(f"{err}: {k} {v}")

        return None, None

    @staticmethod
    def call(stmt: astnodes.Call):
        """
        returns a Lua string that shows a Lua function call statement

        :param stmt:
        :return:
        """
        fname = _luapy_dispatch[stmt.func.display_name](stmt.func)
        args = ','.join(map(str, (_luapy_dispatch[arg.display_name](arg) for arg in stmt.args)))
        return f"{fname}({args})"

    @staticmethod
    def name(nombre: astnodes.Name):
        return nombre.id

    @staticmethod
    def number(numero: astnodes.Number) -> Union[int, float]:
        return numero.n

    @staticmethod
    def string(s: astnodes.String) -> str:
        return s.s

    @staticmethod
    def nil(node: astnodes.Nil):
        return None

    @staticmethod
    def true_expr(node: astnodes.TrueExpr) -> bool:
        return True

    @staticmethod
    def false_expr(node: astnodes.FalseExpr) -> bool:
        return False


_luapy_dispatch = {
    'Table': LuaAstToPy.table,
    'Field': LuaAstToPy.field,
    'Call':  LuaAstToPy.call,
    'Name': LuaAstToPy.name,
    'Number': LuaAstToPy.number,
    'String': LuaAstToPy.string,
    'Nil': LuaAstToPy.nil,
    'True': LuaAstToPy.true_expr,
    'False': LuaAstToPy.false_expr,
}


class LuaSimpleRhs:
    def __init__(self, chunk: str):
        self._ast = ast.parse(chunk)

    def assign_name(self, var_name: str):
        # for now, deal only with single variables and ignore varlist
        for node in ast.walk(self._ast):
            if isinstance(node, ast.Assign):
                for index, lua_var in enumerate(node.targets):
                    if isinstance(lua_var, ast.Name) and _luapy_dispatch[lua_var.display_name](lua_var) == var_name:
                        return _luapy_dispatch[node.values[index].display_name](node.values[index])

        return None

    def assign_index(self, idx_name, value_name):
        # for now, deal only with single variables and ignore varlist
        for node in ast.walk(self._ast):
            if isinstance(node, ast.Assign):
                for index, lua_var in enumerate(node.targets):
                    if isinstance(lua_var, ast.Index) and _luapy_dispatch[lua_var.idx.display_name](lua_var.idx) == idx_name \
                            and _luapy_dispatch[lua_var.value.display_name](lua_var.value) == value_name:
                        return _luapy_dispatch[node.values[index].display_name](node.values[index])
        return None

    def return_exp(self):
        # for now, assume there is only one return statement and a single expression
        for node in ast.walk(self._ast):
            if isinstance(node, ast.Return):
                ret_expr = node.values[0]
                return _luapy_dispatch[ret_expr.display_name](ret_expr)

        return None
