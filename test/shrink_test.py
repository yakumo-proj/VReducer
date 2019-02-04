#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

from vrm.reducer import shrink_gltf_materials, shrink_vrm_materials, shrink_materials


@pytest.mark.parametrize(
    "src, dst", [
        (
                [
                    {
                        'name': 'mat1',
                        'emissiveTexture': {'index': 0, 'texCoord': 1},
                        'normalTexture': {'index': 2, 'texCoord': 3}
                    },
                    {
                        'name': 'mat2',
                        'emissiveTexture': {'index': 4, 'texCoord': 5}
                    }
                ],
                [
                    {'name': 'mat1'},
                    {'name': 'mat2'}
                ]
        ),
        (
                [{'name': 'mat1'}, {'name': 'mat2'}],
                [{'name': 'mat1'}, {'name': 'mat2'}]
        ),
        ([], [])
    ]
)
def test_shrink_gltf_materials(src, dst):
    shrink_gltf_materials(src)
    assert src == dst


@pytest.mark.parametrize(
    "src, dst", [
        (
                [
                    {
                        'name': 'mat1',
                        'textureProperties': {
                            '_MainTex': 0, '_ShadeTexture': 0, '_BumpMap': 1, '_SphereAdd': 2, '_EmissionMap': 3,
                            '_OutlineWidthTexture': 3
                        },
                        'keywordMap': {'_ALPHABLEND_ON': True, '_NORMALMAP': True}
                    },
                    {
                        'name': 'mat2',
                        'textureProperties': {
                            '_MainTex': 0, '_ShadeTexture': 0, '_BumpMap': 1, '_SphereAdd': 2, '_EmissionMap': 3,
                            '_OutlineWidthTexture': 3
                        },
                        'keywordMap': {'_ALPHABLEND_ON': True, '_NORMALMAP': True}
                    },
                ],
                [
                    {
                        'name': 'mat1',
                        'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                        'keywordMap': {'_ALPHABLEND_ON': True}
                    },
                    {
                        'name': 'mat2',
                        'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                        'keywordMap': {'_ALPHABLEND_ON': True}
                    },
                ]
        ),
        (
                [
                    {
                        'name': 'mat1',
                        'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                        'keywordMap': {'_ALPHABLEND_ON': True}
                    }
                ],
                [
                    {
                        'name': 'mat1',
                        'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                        'keywordMap': {'_ALPHABLEND_ON': True}
                    }
                ]
        ),
        (
                [{'name': 'mat1', 'textureProperties': {}, 'keywordMap': {}}],
                [{'name': 'mat1', 'textureProperties': {}, 'keywordMap': {}}]
        ),
        ([], [])
    ]
)
def test_shrink_vrm_materials(src, dst):
    shrink_vrm_materials(src)
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
                                    'textureProperties': {
                                        '_MainTex': 0, '_ShadeTexture': 0, '_BumpMap': 1, '_SphereAdd': 2,
                                        '_EmissionMap': 3,
                                        '_OutlineWidthTexture': 3
                                    },
                                    'keywordMap': {'_ALPHABLEND_ON': True, '_NORMALMAP': True}
                                }
                            ]
                        }
                    },
                    'materials': [
                        {
                            'name': 'mat1',
                            'emissiveTexture': {'index': 0, 'texCoord': 1},
                            'normalTexture': {'index': 2, 'texCoord': 3}
                        }
                    ],
                },
                {
                    'extensions': {
                        'VRM': {
                            'materialProperties': [
                                {
                                    'name': 'mat1',
                                    'textureProperties': {'_MainTex': 0, '_ShadeTexture': 0, '_EmissionMap': 3},
                                    'keywordMap': {'_ALPHABLEND_ON': True}
                                }
                            ]
                        }
                    },
                    'materials': [{'name': 'mat1'}],
                }
        ),
        (
                {'extensions': {'VRM': {'materialProperties': []}}, 'materials': []},
                {'extensions': {'VRM': {'materialProperties': []}}, 'materials': []}
        )
    ]
)
def test_shrink_materials(src, dst):
    assert shrink_materials(src) == dst
