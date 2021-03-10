"""Implementation of the `STAC API Sort Extension
<https://github.com/radiantearth/stac-api-spec/tree/master/fragments/sort>`__"""
from typing import Iterator, List, Optional, Tuple, Union

from pystac.extensions.base import ExtensionDefinition

from pystac_api import APIExtensions, ConformanceClasses, ItemSearch
from pystac_api.extensions import base

SortBy = Tuple[str, ...]
SortByLike = Union[SortBy, List[str], Iterator[str], str]


class SortItemSearchFragment(base.ItemSearchFragment):
    """Implements the `STAC API Sort Extension
    <https://github.com/radiantearth/stac-api-spec/tree/master/fragments/sort>`__ for :class:`~pystac_api.ItemSearch`
    instances.

    This extension class enables checking for implementation of the Sort Extension on :class:`~pystac_api.ItemSearch`
    objects as show below and adds a ``sortby`` search parameter to search queries.
    """
    conformance = ConformanceClasses.STAC_API_ITEM_SEARCH_SORT_EXT

    def __init__(self, item_search):
        self.item_search = item_search

    @classmethod
    def from_item_search(cls, item_search):
        return cls(item_search)

    @classmethod
    def _object_links(cls):
        return []

    def _format_sortby(self, sortby: Optional[SortByLike]) -> Optional[SortBy]:
        if sortby is None:
            return None
        if type(sortby) is str:
            return tuple(sortby.split(','))
        return tuple(sortby)

    def search_parameters(self, sortby: Optional[SortByLike] = None, **_):
        return {'sortby': self._format_sortby(sortby)}


SORT_EXTENSION_DEFINITION = ExtensionDefinition(
    APIExtensions.SORT,
    [
        base.ExtendedObject(ItemSearch, SortItemSearchFragment),
    ]
)
