Context Extension
-----------------

This library supports interacting with the attributes of the `Context Object
<https://github.com/radiantearth/stac-api-spec/tree/master/fragments/context#context-object>`__ in an `Item Collection
<https://github.com/radiantearth/stac-api-spec/blob/master/fragments/itemcollection/README.md>`__ for services that
implement the Context Extension. The implementation extends :class:`~pystac_api.API`, :class:`~pystac_api.ItemSearch`, and
:class:`pystac_api.ItemCollection` instances.

``API`` Instances
+++++++++++++++++

The :class:`~pystac_api.extensions.context.ContextAPIExtension` class extends :class:`~pystac_api.API` instances to
enable checking conformance with this extension:

.. code-block:: python

    >>> from pystac_api import API, APIExtensions
    >>> api = API.from_file('https://eod-catalog-svc-prod.astraea.earth')
    >>> api.api_ext.implements(APIExtensions.CONTEXT)
    True

No other functionality is added to :class:`~pystac_api.API` instances as part of this extension.

``ItemSearch`` Instances
++++++++++++++++++++++++

The :class:`~pystac_api.extensions.context.ContextItemSearchFragment` class extends :class:`~pystac_api.ItemSearch`
instances to enable checking conformance with this extension:

.. code-block:: python

    >>> results = api.search(
    ...     bbox=(-73.21, 43.99, -73.12, 44.05),
    ...     collections='naip',
    ... )
    >>> results.api_ext.implements(APIExtensions.CONTEXT)
    True

No other functionality is added to :class:`~pystac_api.ItemSearch` instances as part of this extension.

``ItemCollection`` Instances
++++++++++++++++++++++++++++

The :class:`~pystac_api.extensions.context.ContextItemCollectionFragment` class extends
:class:`~pystac_api.ItemCollection` instances to enable checking conformance with this extension and access to the
``limit``, ``matched``, and ``returned`` elements of a `Context Object
<https://github.com/radiantearth/stac-api-spec/tree/master/fragments/context#context-object>`__:

.. code-block:: python

    >>> first_page = next(results.item_collections())
    >>> first_page.api_ext.implements(APIExtensions.CONTEXT)
    True
    >>> first_page.api_ext.context.returned
    10
    >>> first_page.api_ext.context.limit
    10
    >>> first_page.api_ext.context.matched
    30
