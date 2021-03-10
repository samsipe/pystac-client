Item Search
-----------

STAC API services may optionally implement a ``/search`` endpoint as describe in the  `STAC API - Item Search spec
<https://github.com/radiantearth/stac-api-spec/tree/master/item-search>`__. This endpoint allows clients to query
STAC Items across the entire service using a variety of filter parameters. See the `Query Parameter Table
<https://github.com/radiantearth/stac-api-spec/tree/master/item-search#query-parameter-table>`__ from that spec for
details on the meaning of each parameter.

The :meth:`pystac_api.API.search` method provides an interface for making requests to a service's
"search" endpoint. This method returns a :class:`pystac_api.ItemSearch` instance.

.. code-block:: python

    >>> from pystac_api import API
    >>> api = API.from_file('https://eod-catalog-svc-prod.astraea.earth')
    >>> results = api.search(
    ...     bbox=[-73.21, 43.99, -73.12, 44.05],
    ...     datetime=['2019-01-01T00:00:00Z', '2019-01-02T00:00:00Z'],
    ...     max_items=5
    ... )

.. note::

    The :meth:`~pystac_api.API.search` method takes arbitrary keyword arguments that may be used by API extensions to
    add search parameters to a query. However, it *does not validate that these keyword arguments are actually used.*
    this means that if you, for instance, use ``sort_by`` instead of ``sortby``, the request will be sent without this
    parameter and no exception will be raised. To ensure that your parameter is being sent correctly, you may want to
    check that it appears in the :class:`~pystac_api.ItemSearch.search_parameters_get` and/or
    :class:`~pystac_api.ItemSearch.search_parameters_post` dictionaries.

Instances of :class:`~pystac_api.ItemSearch` have 2 methods for iterating over results:

* :meth:`ItemSearch.item_collections() <pystac_api.ItemSearch.item_collections>`: iterates over *pages* of results,
  yielding an :class:`~pystac_api.ItemCollection` for each page of results.
* :meth:`ItemSearch.items() <pystac_api.ItemSearch.items>`: iterate over individual results, yielding a
  :class:`pystac.Item` instance for all items that match the search criteria.

.. code-block:: python

    >>> for item in results.items():
    ...     print(item.id)
    S2B_OPER_MSI_L2A_TL_SGS__20190101T200120_A009518_T18TXP_N02.11
    MCD43A4.A2019010.h12v04.006.2019022234410
    MCD43A4.A2019009.h12v04.006.2019022222645
    MYD11A1.A2019002.h12v04.006.2019003174703
    MYD11A1.A2019001.h12v04.006.2019002165238

Unless you need to access attributes of the :class:`~pystac_api.ItemCollection` fragment, you will most likely want to
loop over individual items using the :meth:`~pystac_api.ItemSearch.items` method . This method handles retrieval of
successive pages of results by finding any links with a ``"rel"`` type of ``"next"`` and parsing them to construct the
next request. The default implementation of this ``"next"`` link parsing assumes that the link follows the spec for an
extended STAC link as described in the `STAC API - Item Search: Paging
<https://github.com/radiantearth/stac-api-spec/tree/master/item-search#paging>`__ section. See the :mod:`Paging
<pystac_api.paging>` docs for details on how to customize this behavior.
