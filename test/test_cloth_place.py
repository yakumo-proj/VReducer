#!/usr/bin/env python

import pytest

from vrm import placer


@pytest.mark.parametrize(
    "src, dst", [
        ({'materials': []}, {}),
        (  # 服上のみ
                {'materials': [
                    {'name': 'F00_002_01_Tops_01_CLOTH-10'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (2048, 2048)}
                    }
                }
        ),
        (  # スカートのみ
                {'materials': [
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'}
                ]},
                {
                    'main': '_Bottoms_',
                    'place': {
                        '_Bottoms_': {'pos': (0, 0), 'size': (1024, 512)}
                    }
                }
        ),
        (  # 靴のみ
                {'materials': [
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'}
                ]},
                {
                    'main': '_Shoes_',
                    'place': {
                        '_Shoes_': {'pos': (0, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # アクセサリのみ
                {'materials': [
                    {'name': 'F00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Accessory_',
                    'place': {
                        '_Accessory_': {'pos': (0, 0), 'size': (256, 256)}
                    }
                }
        ),
        (  # 服上、靴
                {'materials': [
                    {'name': 'F00_001_01_Tops_01_CLOTH-01'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # 服上、アクセサリ
                {'materials': [
                    {'name': 'F00_001_01_Tops_01_CLOTH-01'},
                    {'name': 'F00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Accessory_': {'pos': (1024, 0), 'size': (256, 256)}
                    }
                }
        ),
        (  # スカート、靴
                {'materials': [
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'}
                ]},
                {
                    'main': '_Bottoms_',
                    'place': {
                        '_Bottoms_': {'pos': (0, 0), 'size': (1024, 512)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # ペンシルスカート、靴
                {'materials': [
                    {'name': '00_004_01_Bottoms_01_CLOTH-11'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'}
                ]},
                {
                    'main': '_Bottoms_',
                    'place': {
                        '_Bottoms_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # 靴、アクセサリ
                {'materials': [
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'},
                    {'name': 'F00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Shoes_',
                    'place': {
                        '_Shoes_': {'pos': (0, 0), 'size': (512, 512)},
                        '_Accessory_': {'pos': (0, 512), 'size': (256, 256)}
                    }
                }
        ),
        (  # 靴、アクセサリ
                {'materials': [
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'F00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Bottoms_',
                    'place': {
                        '_Bottoms_': {'pos': (0, 0), 'size': (1024, 512)},
                        '_Accessory_': {'pos': (1024, 0), 'size': (256, 256)}
                    }
                }
        ),
        (  # 学生服スカート
                {'materials': [
                    {'name': 'F00_001_01_Tops_01_CLOTH-01'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 512)}
                    }
                }
        ),
        (  # 学生服スカート靴
                {'materials': [
                    {'name': 'F00_001_01_Tops_01_CLOTH-01'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 512)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # 学生服スカート靴リボン
                {'materials': [
                    {'name': 'F00_001_01_Tops_01_CLOTH-01'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-13'},
                    {'name': 'F00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 512)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)},
                        '_Accessory_': {'pos': (1024, 512), 'size': (256, 256)}
                    }
                }
        ),
        (  # スカートリボン
                {'materials': [
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'F00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Bottoms_',
                    'place': {
                        '_Bottoms_': {'pos': (0, 0), 'size': (1024, 512)},
                        '_Accessory_': {'pos': (1024, 0), 'size': (256, 256)}
                    }
                }
        ),
        (  # 学生服ズボン靴ネクタイ
                {'materials': [
                    {'name': 'M00_001_01_Tops_01_CLOTH-10'},
                    {'name': 'M00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'M00_001_01_Shoes_01_CLOTH-13'},
                    {'name': 'M00_001_01_Accessory_Tie_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 1024)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)},
                        '_Accessory_': {'pos': (1024, 512), 'size': (256, 256)}
                    }
                }
        ),
        (  # Tシャツのみ
                {'materials': [
                    {'name': 'F00_005_01_Tops_01_CLOTH-12'},
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (2048, 2048)}
                    }
                }
        ),
        (  # Tシャツスカート靴
                {'materials': [
                    {'name': 'F00_005_01_Tops_01_CLOTH-12'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-11'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-10'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 512)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # パーカーのみ
                {'materials': [
                    {'name': 'F00_006_01_Tops_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (2048, 2048)}
                    }
                }
        ),
        (  # パーカースカート靴
                {'materials': [
                    {'name': 'F00_006_01_Tops_01_CLOTH-11'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-10'},
                    {'name': 'F00_001_01_Bottoms_01_CLOTH-12'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 512)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        ),
        (  # ロングコート
                {'materials': [
                    {'name': 'F00_008_01_Tops_01_CLOTH-10'},
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (2048, 2048)},
                    }
                }
        ),
        (  # ロングコート、ペンシルスカート
                {'materials': [
                    {'name': 'F00_008_01_Tops_01_CLOTH-10'},
                    {'name': 'F00_004_01_Bottoms_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 1024)},
                    }
                }
        ),
        (  # ロングコートズボン靴
                {'materials': [
                    {'name': 'F00_008_01_Tops_01_CLOTH-10'},
                    {'name': 'F00_008_01_Bottoms_01_CLOTH-11'},
                    {'name': 'F00_001_01_Shoes_01_CLOTH-12'},
                    {'name': 'F00_008_01_Bottoms_01_CLOTH-11'}
                ]},
                {
                    'main': '_Tops_',
                    'place': {
                        '_Tops_': {'pos': (0, 0), 'size': (1024, 1024)},
                        '_Bottoms_': {'pos': (0, 1024), 'size': (1024, 1024)},
                        '_Shoes_': {'pos': (1024, 0), 'size': (512, 512)}
                    }
                }
        )
    ]
)
def test_get_cloth_place(src, dst):
    assert placer.get_cloth_place(src) == dst
