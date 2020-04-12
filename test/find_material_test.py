#!/usr/bin/env python


import pytest

from vrm.reducer import find_near_vrm_material


@pytest.mark.parametrize(
    "gltf, name, material, dst", [
        (
                {
                    'extensions': {
                        'VRM': {
                            'materialProperties': [
                                {'name': 'hair1', 'vectorProperties': {'_Color': [0, 0, 0, 1]}},
                                {'name': 'hair2', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 1]}},
                                {'name': 'hair3', 'vectorProperties': {'_Color': [0.5, 0.5, 0.51, 1]}},
                                {'name': 'hair4', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 0]}},
                                {'name': 'hair5', 'vectorProperties': {'_Color': [1, 1, 1, 1]}},
                                {'name': 'hairBack', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 1]}},
                                {'name': 'other', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 1]}}
                            ]
                        }
                    }
                },
                'hair',
                {'name': 'hairBack', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 1]}},
                {'name': 'hair2', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 1]}},
        ),
        (
                {'extensions': {'VRM': {'materialProperties': []}}},
                'hair',
                {'name': 'hair2', 'vectorProperties': {'_Color': [0.5, 0.5, 0.5, 1]}},
                None
        )
    ]
)
def test_find_near_vrm_material(gltf, name, material, dst):
    assert find_near_vrm_material(gltf, name, material) == dst
