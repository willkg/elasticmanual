
================
 Geo Shape Type 
================




—-
layout: guide
title: Geo Shape Type
cat: guide
sidebar: reference\_mapping
—-

The ``geo_shape`` mapping type facilitates the indexing of and searching
with arbitrary geo shapes such as rectangles and polygons. It should be
used when either the data being indexed or the queries being executed
contain shapes other than just points.

Note, the ``geo_shape`` type uses
`Spatial4J <https://github.com/spatial4j/spatial4j>`_ and
`JTS <http://www.vividsolutions.com/jts/jtshome.htm>`_, both of which
are optional dependencies. Consequently you must add Spatial4J v0.3 and
JTS v1.12 to your classpath in order to use this type.

Shape Representation
====================

To efficiently represent shapes in the index, Shapes are converted into
a series of hashes representing grid squares using implementations of a
PrefixTree. The tree notion comes from the fact that the PrefixTree uses
multiple grid layers, each with a different level of precision, to
represent the Earth. For example, the QuadPrefixTree implementation uses
four grid squares, labelled A, B, C and D, to represent its first layer.
Move one level of precision further and there are now 16 grid squares,
AA, AB, AC, AD, BA… and so on. By having the multiple layers of
precision, shapes can be indexed in an efficient representation which
balances the number of terms vs. the precision of searches.

Multiple PrefixTree implementations are provided:

-  GeohashPrefixTree – Uses
   `geohashes <http://en.wikipedia.org/wiki/Geohash>`_ for grid squares
   which means more squares per layer
-  QuadPrefixTree – Represents Earth using a
   `quadtree <http://en.wikipedia.org/wiki/Quadtree>`_

Mapping Options
===============

+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .\_ Option               | .\_ Description                                                                                                                                                                                                                              |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tree``                 | Name of the PrefixTree implementation to be used. ``geohash`` for GeohashPrefixTree and ``quadtree`` for QuadPrefixTree. Defaults to ``geohash``.                                                                                            |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tree_levels``          | Maximum number of layers to be used by the PrefixTree. This can be used to control the precision of shape representations and therefore how many terms are indexed. Defaults the the default value of the chosen PrefixTree implementation   |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``distance_error_pct``   | Used as a hint to the PrefixTree about how precise it should be. Defaults to 0.025 (2.5%) with 0.5 as the maximum supported value.                                                                                                           |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Input Structure
===============

The `GeoJSON <http://www.geojson.org>`_ format is used to represent
Shapes as input as follows:

::

    {
        “location” : {
            “type” : “point”,
            “coordinates” : [45.0, -45.0]
        }
    }

Note, both the ``type`` and ``coordinates`` fields are required.

The supported ``types`` are ``point``, ``linestring``, ``polygon``,
``multipoint`` and ``multipolygon``. Additionally, ElasticSearch
supports an ``envelope`` type which consists of coordinates for upper
left and lower right points of the shape. The following is an example of
a ``envelope``:

::

    {
        “location” : {
            “type” : “envelope”,
            “coordinates” : [[-45.0, 45.0], [45.0, -45.0]]
        }
    }

Sorting and Retrieving index Shapes
===================================

Due to the complex input structure and index representation of shapes,
it is not currently possible to sort shapes or retrieve their field
specifically. They are only retrieveable through the ``_source`` field.



