
=================
 GeoShape Filter 
=================




—-
layout: guide
title: GeoShape Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Efficient filtering of documents containing shapes indexed using the
``geo_shape`` type.

Much like the ``geo_shape`` type, the ``geo_shape`` Filter uses a grid
square representation of the filter shape to find those documents which
have shapes that relate to the filter shape in a specified way. In order
to do this, the field being filtered **must** be of ``geo_shape`` type.
The Filter will use the same PrefixTree configuration as defined for the
field.

Filter Format
=============

The Filter supports two way of defining the Filter shape, either by
providing a whole shape defintion, or by referencing the name of a shape
pre-indexed in another index. Both formats are defined below with
examples.

In addition to the shape, the ``relation`` type must be defined, which
sets how the filter shape and indexed shapes must relate. The following
``relation`` types are currently supported:

-  ``intersects`` – Finds those indexed shapes which intersect with the
   filter shape. Intersection occurs when the two shapes have at least
   one shared grid hash. Because of current limitations of the
   algorithm, very large indexed shapes are not deemed to intersect with
   very small filter shapes. However, smaller index shapes will
   intersect with larger filter shapes.
-  ``disjoint`` – Finds those indexed shapes which do not intersect with
   the filter shape. This means the two shapes will not share any grid
   hashes.
-  ``within`` – Finds those indexed shapes which are fully contained
   within the filter shape. Unlike ``intersects``, this means the all of
   the indexed shape must be present inside the filter shape. Any shapes
   will additional area outside of the filter shape are excluded. This
   relationship is still experimental. Note. this relation type was
   previously named ``contains``. This is no longer supported

Provided Shape Definition
-------------------------

Again, like the ``geo_shape`` type, the ``geo_shape`` Filter uses
`GeoJSON <http://www.geojson.org>`_ to represent shapes. The following
is an example of using the Filter with a provided Shape definition which
also makes use of ElasticSearch’s ``envelope`` GeoJSON extension:

::

    {
        “filtered”: {
            “query”: {
                “match_all”: {}
            },
            “filter”: {
                “geo_shape”: {
                    “location”: {
                        “shape”: {
                            “type”: “envelope”,
                            “coordinates”:[[-45,45],[45,-45]]
                        },
                        “relation”: “within”
                    }
                }
            }
        }
    }

Pre-Indexed Shape
-----------------

The Filter also supports using a shape which has already been indexed in
another index and/or index type. This is particularly useful for when
you have a pre-defined list of shapes which are useful to your
application and you want to reference this using a logical name (for
example 'New Zealand’) rather than having to provide their coordinates
each time. In this situation it is only necessary to provide:

-  ``id`` – The ID of the document that containing the pre-indexed
   shape.
-  ``index`` – Name of the index where the pre-indexed shape is.
   Defaults to 'shapes’.
-  ``type`` – Index type where the pre-indexed shape is.
-  ``shape_field_name`` – Name of the field in the document containing
   the pre-indexed shape. Defaults to 'shape’.

The following is an example of using the Filter with a pre-indexed
shape:

::

    {
        “filtered”: {
            “query”: {
                “match_all”: {}
            },
            “filter”: {
                “geo_shape”: {
                    “location”: {
                        “indexed_shape”: {
                            “id”: “New Zealand”,
                            “type”: “countries”,
                            “index”: “shapes”,
                            “shape_field_name”: “shape”
                        },
                        “relation”: “within”
                    }
                }
            }
        }
    }

Caching
=======

The result of the Filter is not cached by default. Setting ``_cache`` to
``true`` will mean the results of the Filter will be cached. Since
shapes can contain 10s-100s of coordinates and any one differing means a
new shape, it may make sense to only using caching when you are sure
that the shapes will remain reasonably static.



