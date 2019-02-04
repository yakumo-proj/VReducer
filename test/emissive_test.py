#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

from vrm.reducer import emissive_mtoon_material, emissive_mtoon_materials


@pytest.mark.parametrize(
    "src, dst", [
        (
                {
                    'name': 'mat1',
                    'floatProperties': {"_IndirectLightIntensity": 0.1},
                    'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                    "vectorProperties": {
                        "_Color": [1, 0.5, 0.9, 1],
                        "_ShadeColor": [1, 0.8, 0.8, 1],
                        "_EmissionColor": [0, 0, 0, 1],
                    }
                },
                {
                    'name': 'mat1',
                    'floatProperties': {"_IndirectLightIntensity": 0},
                    'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 0},
                    "vectorProperties": {
                        "_Color": [0, 0, 0, 1],
                        "_ShadeColor": [0, 0, 0, 1],
                        "_EmissionColor": [1, 0.5, 0.9, 1],
                    }
                }
        )
    ]
)
def test_emissive_mtoon_material(src, dst):
    emissive_mtoon_material(src)
    assert src == dst


@pytest.mark.parametrize(
    "src, dst", [
        (
                {
                    'extensions': {
                        'VRM': {
                            'materialProperties': [
                                {
                                    'name': 'mat1',
                                    'floatProperties': {"_IndirectLightIntensity": 0.1},
                                    'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                                    "vectorProperties": {
                                        "_Color": [1, 0.5, 0.9, 1],
                                        "_ShadeColor": [1, 0.8, 0.8, 1],
                                        "_EmissionColor": [0, 0, 0, 1],
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'extensions': {
                        'VRM': {
                            'materialProperties': [
                                {
                                    'name': 'mat1',
                                    'floatProperties': {"_IndirectLightIntensity": 0},
                                    'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 0},
                                    "vectorProperties": {
                                        "_Color": [0, 0, 0, 1],
                                        "_ShadeColor": [0, 0, 0, 1],
                                        "_EmissionColor": [1, 0.5, 0.9, 1],
                                    }
                                }
                            ]
                        }
                    }
                }
        ),
        ({'extensions': {'VRM': {'materialProperties': []}}}, {'extensions': {'VRM': {'materialProperties': []}}})
    ]
)
def test_emissive_mtoon_materials(src, dst):
    assert emissive_mtoon_materials(src) == dst
