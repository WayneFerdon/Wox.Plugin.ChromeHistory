# ----------------------------------------------------------------
# Author: WayneFerdon wayneferdon@hotmail.com
# Date: 2023-03-04 12:45:56
# LastEditors: WayneFerdon wayneferdon@hotmail.com
# LastEditTime: 2023-03-04 13:23:44
# FilePath: \Flow.Launcher.Plugin.ChromeHistory\RegexList.py
# ----------------------------------------------------------------
# Copyright (c) 2023 by Wayne Ferdon Studio. All rights reserved.
# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.
# ----------------------------------------------------------------

import re

class RegexList:
    def __init__(self, queryString: str):
        self.queryString = queryString
        queryList = RegexList.__replaceBrackets__(queryString).lower().split()
        self.__regexs__ = [ re.compile(x) for x in queryList ]

    def __replaceBrackets__(string:str):
        return string.replace('[', '\[') \
            .replace(']', '\]') \
            .replace('(', '\(') \
            .replace(')', '\)')

    def match(self, item: str):
        for regex in self.__regexs__:
            if not regex.search(item.lower()):
                return False
        return True