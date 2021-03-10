import pytest

from pystac_api import API, APIExtensions, ConformanceClasses, ItemSearch

from ..helpers import ASTRAEA_API_PATH, ASTRAEA_URL

SEARCH_URL = f'{ASTRAEA_URL}/search'


class TestItemSearchSortExtension:

    def test_implements(self):
        results = ItemSearch(
            url=SEARCH_URL,
            conformance=[
                ConformanceClasses.STAC_API_CORE,
                ConformanceClasses.STAC_API_ITEM_SEARCH,
                ConformanceClasses.STAC_API_ITEM_SEARCH_SORT_EXT
            ],
        )

        assert results.api_ext.implements(APIExtensions.SORT)

    def test_search_params(self):
        results = ItemSearch(
            url=SEARCH_URL,
            bbox=[-73.3, 43.9, -73.1, 44.1],
            collections='naip',
            conformance=[
                ConformanceClasses.STAC_API_CORE,
                ConformanceClasses.STAC_API_ITEM_SEARCH,
                ConformanceClasses.STAC_API_ITEM_SEARCH_SORT_EXT
            ],
            sortby='id'
        )

        assert results.search_parameters_post.get('sortby') == ('id',)

    @pytest.mark.vcr
    def test_sorting(self):
        results = ItemSearch(
            url=SEARCH_URL,
            bbox=[-73.3, 43.9, -73.1, 44.1],
            collections='naip',
            conformance=[
                ConformanceClasses.STAC_API_CORE,
                ConformanceClasses.STAC_API_ITEM_SEARCH,
                ConformanceClasses.STAC_API_ITEM_SEARCH_SORT_EXT
            ],
            sortby='id'
        )

        items = list(results.items())
        assert items == sorted(items, key=lambda item: item.id)

    @pytest.mark.vcr
    def test_reverse_sorting(self):
        results = ItemSearch(
            url=SEARCH_URL,
            bbox=[-73.3, 43.9, -73.1, 44.1],
            collections='naip',
            conformance=[
                ConformanceClasses.STAC_API_CORE,
                ConformanceClasses.STAC_API_ITEM_SEARCH,
                ConformanceClasses.STAC_API_ITEM_SEARCH_SORT_EXT
            ],
            sortby='-id'
        )

        items = list(results.items())
        assert items == sorted(items, key=lambda item: item.id, reverse=True)


class TestAPISortExtension:
    @pytest.mark.vcr
    def test_search(self):
        api = API.from_file(ASTRAEA_API_PATH)
        results = api.search(
            bbox=[-73.3, 43.9, -73.1, 44.1],
            collections='naip',
            sortby='id'
        )
        assert results.search_parameters_post.get('sortby') == ('id',)

        items = list(results.items())
        assert items == sorted(items, key=lambda item: item.id)
