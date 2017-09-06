#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2017 Ganggao Zhu- Grupo de Sistemas Inteligentes
# gzhu[at]dit.upm.es
# DIT, UPM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

def test_matcher():
    from sematch.application import Matcher
    matcher = Matcher(result_limit=2, expansion=False, show_query=True)
    assert matcher.match_type('singer') is not None
    assert matcher.match_concepts(['http://dbpedia.org/class/yago/Singer110599806']) is not None
    assert matcher.match_entity_type('singer Spain') is not None

def test_sparql():
    from sematch.semantic.sparql import EntityFeatures, NameSPARQL
    ef = EntityFeatures()
    name = NameSPARQL()
    feature = EntityFeatures()
    x = name.name2entities('Michael Jordan')[0]
    y = name.name2entities('Michael I. Jordan')[0]
    assert x is not None
    assert y is not None
    assert feature.features(x) is not None
    assert feature.features(y) is not None
    assert ef.type('http://dbpedia.org/resource/Star_Wars') is not None