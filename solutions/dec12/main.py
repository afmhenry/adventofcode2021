#!/usr/bin/env python3
import csv

queue = []


def findPath(filename, second_challenge_mode):
    nodes = []
    traveled = []
    alt_routes = []
    alt_routes2 = []

    mapping = {}
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter="-")):
            nodes.append(row[0])
            nodes.append(row[1])
            exists = True if row[0] in mapping else False
            if exists:
                set_values = mapping.get(row[0])
                set_values.append(row[1])
            else:
                set_values = [row[1]]
            mapping.update({row[0]: set_values})

            alt_routes2.append({row[1]: row[0]})
        f.close()

    for node in nodes:
        if node not in mapping:
            mapping.update({node: []})

    start_nodes = mapping.get("start")

    alt_routes = findAltRoutes(mapping)

    path = []
    paths = []

    visited = set()
    dfs("start", path, visited, mapping, paths)



    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter="-")):
            print("foo")
            exists = True if row[1] in mapping else False
            if exists:
                set_values = mapping.get(row[1])
                set_values.append(row[0])
            else:
                set_values = [row[0]]
            mapping.update({row[1]: set_values})
    print(mapping)

    paths_formatted = []

    for path in paths:
        paths_formatted.append(formatPath(path))
        print(path)

    for i in range(1):
        findAllPaths(alt_routes, paths_formatted, mapping)

    print(paths_formatted)
    print(len(paths_formatted))


def findAllPaths(alt_routes, paths_formatted, mapping):
    for path in paths_formatted:
        for i, route in enumerate(alt_routes):
            key = list(route.keys())[0]
            value = str(list(route.values())[0])
            # print(key, value, path)
            if key in path and value not in path:
                # print("replace", key, value, string_path)
                path = path.replace("start-", "").replace("-end", "")
                new_str_path = path.replace(key, value, 1)
                new_str_path = "start-" + new_str_path + "-end"

                lower_case_old = ''.join([c for c in path.split("-") if c.islower() and c != "end" and c != "start"])
                lower_case_new = ''.join([c for c in value.split("-") if c.islower() and c != "end" and c != "start"])
                allowed = True

                for char in new_str_path.split("-"):
                    if str.islower(char):
                        if new_str_path.count(char) > 1:
                            allowed = False

                if allowed and new_str_path not in paths_formatted:

                    str_split = new_str_path.split("-")
                    allowed = True
                    for j, node in enumerate(str_split):
                        if node != "end":
                            if str_split[j + 1] not in mapping[str_split[j]]:
                                if str_split[j] not in mapping[str_split[j + 1]]:
                                    allowed = False
                    if allowed:
                        paths_formatted.append(new_str_path)


def formatPath(path):
    resulting_string = ""
    dash = "-"
    for i, node in enumerate(path):
        if i == len(path) - 1:
            dash = ""
        resulting_string += (node + dash)
    return resulting_string


def findAltRoutes(mapping):
    alt_mappings = []
    for i, entry in enumerate(mapping):
        if entry != "start" and entry != "end":
            for node in mapping.get(entry):
                if node != "start" and node != "end":
                    if str.isupper(entry) and str.isupper(node):
                        print("dunno", entry, node)
                    elif str.isupper(entry) and str.islower(node):
                        alt_mappings.append({entry: entry + "-" + node + "-" + entry})
                        for sub_node in mapping.get(node):
                            if sub_node == "end" or str.isupper(sub_node):
                                alt_mappings.append({entry: entry + "-" + node})
                                alt_mappings.append({node: node + "-" + entry})
                    elif str.isupper(node) and str.islower(entry):
                        alt_mappings.append({node: node + "-" + entry + "-" + node})
                        for sub_node in mapping.get(entry):
                            if sub_node == "end" or str.isupper(sub_node):
                                alt_mappings.append({entry: entry + "-" + node})
                                alt_mappings.append({node: node + "-" + entry})
                    elif str.islower(entry) and str.islower(node):
                        alt_mappings.append({entry: node + "-" + entry})

    return alt_mappings


def dfs(curr_node, path, visited, mapping, paths):
    if curr_node not in visited:
        if str.islower(curr_node) and curr_node != "end":
            visited.add(curr_node)
        # print("curr_node", curr_node, len(path))
        path.append(curr_node)
        if curr_node == "end":
            paths.append(path.copy())
            path.clear()
            path.append("start")
        else:
            options = mapping.get(curr_node)
            if options:
                for option in mapping.get(curr_node):
                    if option not in visited:
                        dfs(option, path, visited, mapping, paths)
            else:
                # print(path[-2])
                dfs(path[-2], path, visited, mapping, paths)
    else:
        # print("already seen", curr_node, " in ", path)
        path.pop()

def placeholder(node, current_path, mapping, visited):
    if node in visited:
        print("reject traversal")
        mapping.get(current_path.pop)
    elif str.islower(node) and node != "end":
        visited.append(node)
    if node == "end":
        current_path.append(node)
        return
    else:
        current_path.append(node)
        paths = mapping.get(node)
        if paths:
            for path in paths:
                graphTraversal(path, current_path, mapping, visited)
        else:
            print("reject traversal")
            prev_node = current_path.pop()
            visited.append(node)
            graphTraversal(prev_node, current_path, mapping, visited)


print("result of func", findPath("dec12-mock.txt", False))
# print (findPath("dec15.txt", False) == 1591)

# print (findPath("dec15-mock.txt", True) == 195)
# print (findPath("dec15.txt", True) == 314)
