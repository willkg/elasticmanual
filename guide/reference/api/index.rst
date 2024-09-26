
=====
 API 
=====




—-
layout: guide
title: API
cat: guide
sidebar: reference\_api
—-

This section describes the REST APIs **elasticsearch** provides (mainly)
using JSON. The API is exposed using
`HTTP </guide/reference/modules/http.html>`_,
`thrift </guide/reference/modules/thrift.html>`_,
`memcached </guide/reference/modules/memcached.html>`_.

Nodes
=====

Most cluster level APIs allow to specify which nodes to execute on (for
example, getting the node stats for a node). Nodes can be identified in
the APIs either using their internal node id, the node name, address,
custom attributes, or just the ``_local`` node receiving the request.
For example, here are some sample executions of nodes info:

::

        
            Local    
        
    curl localhost:9200/_cluster/nodes/_local
        
            Address
        
    curl localhost:9200/_cluster/nodes/10.0.0.3,10.0.0.4
    curl localhost:9200/_cluster/nodes/10.0.0.*
        
            Names
        
    curl localhost:9200/_cluster/nodes/node_name_goes_here
    curl localhost:9200/_cluster/nodes/node_name_goes_*
        
            Attributes (set something like node.rack: 2 in the config)
        
    curl localhost:9200/_cluster/nodes/rack:2
    curl localhost:9200/_cluster/nodes/ra*:2
    curl localhost:9200/_cluster/nodes/ra*:2*

Options
=======

Pretty Results
--------------

When appending ``?pretty=true`` to any request made, the JSON returned
will be pretty formatted (use it for debugging only!).

Parameters
----------

Rest parameters (when using HTTP, map to HTTP URL parameters) follow the
convention of using underscore casing.

Boolean Values
--------------

All REST APIs parameters (both request parameters and JSON body) support
providing boolean “false” as the values: ``false``, ``0`` and ``off``.
All other values are considered “true”. Note, this is not related to
fields within a document indexed treated as boolean fields.

Number Values
-------------

All REST APIs support providing numbered parameters as ``string`` on top
of supporting the native JSON number types.

Result Casing
-------------

All REST APIs accept the ``case`` parameter. When set to ``camelCase``,
all field names in the result will be returned in camel casing,
otherwise, underscore casing will be used. Note, this does not apply to
the source document indexed.

JSONP
-----

All REST APIs accept a ``callback`` parameter resulting in a
`JSONP <http://en.wikipedia.org/wiki/JSONP>`_ result.
p. You can also use the ``source`` query string parameter to substitute
for the body of the request.



