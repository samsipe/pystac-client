Sort Extension
--------------

This library supports requests with a ``sortby`` search parameter as describe in the Sort Extension. The implementation
extends :class:`~pystac_api.API` and :class:`~pystac_api.ItemSearch` instances.

``API`` Instances
+++++++++++++++++

The :class:`~pystac_api.extensions.sort.SortAPIExtension` class extends :class:`~pystac_api.API` instances to
enable checking conformance with this extension:

.. code-block:: python

    >>> from pystac_api import API, APIExtensions
    >>> api = API.from_file('https://eod-catalog-svc-prod.astraea.earth')
    >>> api.api_ext.implements(APIExtensions.SORT)
    True

No other functionality is added to :class:`~pystac_api.API` instances as part of this extension.

``ItemSearch`` Instances
++++++++++++++++++++++++

The :class:`~pystac_api.extensions.sort.SortItemSearchFragment` class extends :class:`~pystac_api.ItemSearch`
instances to enable checking conformance with this extension and to accept a ``sortby`` keyword argument. This argument
is passed to the ``sortby`` parameter of the ``/search`` request.

.. code-block:: python

    >>> results = api.search(
    ...     collections='naip',
    ...     sortby=['collection', '-id']
    ... )
    >>> results.search_parameters_get
    {'collections': 'naip', 'sortby': 'collection,-id'}

