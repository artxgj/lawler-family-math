
from abc import ABC, abstractmethod
from lua_ast_py import LuaSimpleRhs


class ZhDataModLuaChunk(ABC):
    def __init__(self, chunk: str):
        self._rhs = LuaSimpleRhs(chunk)

    @abstractmethod
    def content(self, lua_varname: str):
        pass


class ZhDataModTableAssignName(ZhDataModLuaChunk):
    def __init__(self, chunk: str):
        super().__init__(chunk)

    def content(self, lua_var: str):
        return self._rhs.assign_name(lua_var)


class ZhDataModTableAssignIndex(ZhDataModLuaChunk):
    def __init__(self, chunk: str):
        super().__init__(chunk)

    def content(self, lua_var: str):
        table_name, index = lua_var.split('.')
        return self._rhs.assign_index(index, table_name)


class ZhDataModTableReturn(ZhDataModLuaChunk):
    def __init__(self, chunk: str):
        super().__init__(chunk)

    def content(self, lua_var: str = None):
        return self._rhs.return_exp()
