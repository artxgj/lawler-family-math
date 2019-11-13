from zhdatamod_lua import ZhDataModTableAssignName, ZhDataModTableAssignIndex, ZhDataModTableReturn
import argparse
import io
import json
import os


def lua_to_json(input_path, output_path, lua_var, lua_py_type):
    s = io.StringIO()
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            s.write(line)

    rhs = lua_py_type(s.getvalue())

    with open(output_path, 'w', encoding='utf-8') as ostream:
        json.dump(rhs.content(lua_var), ostream, ensure_ascii=False, indent=4)


def convert_to_json(input_folder: str, output_folder: str):
    data_modules = [
        {'relpath': 'st', 'lua_var': 'export.st', 'lua_py_type': ZhDataModTableAssignIndex, 'is_dir': False},
        {'relpath': 'ts', 'lua_var': 'export.ts', 'lua_py_type': ZhDataModTableAssignIndex, 'is_dir': False},
        {'relpath': 'yue-pron', 'lua_var': 'export.jyutping', 'lua_py_type': ZhDataModTableAssignIndex, 'is_dir': False},
        {'relpath': 'cmn-pron', 'lua_var': 'export.py', 'lua_py_type': ZhDataModTableAssignIndex, 'is_dir': False},
        {'relpath': 'dial-syn', 'lua_var': 'export.list', 'lua_py_type': ZhDataModTableAssignIndex, 'is_dir': True},
        {'relpath': 'yue-word', 'lua_var': None, 'lua_py_type': ZhDataModTableReturn, 'is_dir': True},
        {'relpath': 'hak-pron', 'lua_var': None, 'lua_py_type': ZhDataModTableReturn, 'is_dir': True},
        {'relpath': 'nan-pron', 'lua_var': None, 'lua_py_type': ZhDataModTableReturn, 'is_dir': True},
        {'relpath': 'wordlist', 'lua_var': 'list', 'lua_py_type': ZhDataModTableAssignName, 'is_dir': True}
    ]

    for dm in data_modules:
        input_path = f"{input_folder}/{dm['relpath']}"
        output_path = f"{output_folder}/{dm['relpath']}"

        if dm['is_dir']:
            if not os.path.exists(output_path):
                os.mkdir(output_path)

            for f in os.listdir(input_path):
                file_path = f"{input_path}/{f}"

                if not os.path.isfile(file_path):
                    continue

                lua_to_json(file_path, f"{output_path}/{f}", dm['lua_var'], dm['lua_py_type'])
        else:
            lua_to_json(input_path, output_path, dm['lua_var'], dm['lua_py_type'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-folder", help="input folder", required=True)
    parser.add_argument("-o", "--output-folder", help="output folder", required=True)
    args = parser.parse_args()
    convert_to_json(args.input_folder, args.output_folder)


