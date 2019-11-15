
from abc import ABC, abstractmethod
from lua_ast_py import LuaSimpleRhs


class ZhDataModLuaChunk(ABC):
    def __init__(self, chunk: str):
        self._rhs = LuaSimpleRhs(chunk)

    @abstractmethod
    def content(self, lua_varname: str):
        pass

    def _associate_array_to_list(self, contents: dict):
        """
        Lua does not support arrays and uses associative arrays. This method
        converts the python-version of the associative array to a list
        :return:
        """
        new_contents = {}
        for key, value in contents.items():
            if type(value) == dict:
                new_contents[key] = [value[index] for index in range(1, len(value)+1) if value[index] != ""]
            else:
                new_contents[key] = contents[key]
        return new_contents


class ZhDataModTableAssignName(ZhDataModLuaChunk):
    def __init__(self, chunk: str):
        super().__init__(chunk)

    def content(self, lua_var: str):
        return self._associate_array_to_list(self._rhs.assign_name(lua_var))


class ZhDataModTableAssignIndex(ZhDataModLuaChunk):
    def __init__(self, chunk: str):
        super().__init__(chunk)

    def content(self, lua_var: str):
        table_name, index = lua_var.split('.')
        return self._associate_array_to_list(self._rhs.assign_index(index, table_name))


class ZhDataModTableReturn(ZhDataModLuaChunk):
    def __init__(self, chunk: str):
        super().__init__(chunk)

    def content(self, lua_var: str = None):
        return self._associate_array_to_list(self._rhs.return_exp())
