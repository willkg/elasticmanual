
=====================
 Geo Distance Filter 
=====================




—-
layout: guide
title: Geo Distance Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents that include only hits that exists within a specific
distance from a geo point. Assuming the following indexed json:

::

    {
        “pin” : {
            “location” : {
                “lat” : 40.12,
                “lon” : -71.34
            }
        }
    }

Then the following simple query can be executed with a ``geo_distance``
filter:

::

    {
        “filtered” : {
            “query” : {
                “match_all” : {}
            },
            “filter” : {
                “geo_distance” : {
                    “distance” : “200km”,
                    “pin.location” : {
                        “lat” : 40,
                        “lon” : -70
                    }
                }
            }
        }
    }    

Accepted Formats
================

In much the same way the ``geo_point`` type can accept different
representation of the geo point, the filter can accept it as well:

Lat Lon As Properties
---------------------

::

    {
        “filtered” : {
            “query” : {
                “match_all” : {}
            },
            “filter” : {
                “geo_distance” : {
                    “distance” : “12km”,
                    “pin.location” : {
                        “lat” : 40,
                        “lon” : -70
                    }
                }
            }
        }
    }

Lat Lon As Array
----------------

Format in ``[lon, lat]``, note, the order of lon/lat here in order to
conform with `GeoJSON <http://geojson.org/>`_.

::

    {
        “filtered” : {
            “query” : {
                “match_all” : {}
            },
            “filter” : {
                “geo_distance” : {
                    “distance” : “12km”,
                    “pin.location” : [40, -70]
                }
            }
        }
    }

Lat Lon As String
-----------------

Format in ``lat,lon``.

::

    {
        “filtered” : {
            “query” : {
                “match_all” : {}
            },
            “filter” : {
                “geo_distance” : {
                    “distance” : “12km”,
                    “pin.location” : “40,-70”
                }
            }
        }
    }

Geohash
-------

::

    {
        “filtered” : {
            “query” : {
                “match_all” : {}
            },
            “filter” : {
                “geo_distance” : {
                    “distance” : “12km”,
                    “pin.location” : “drm3btev3e86”
                }
            }
        }
    }

Options
=======

The following are options allowed on the filter:

Option
Description
``distance``
The distance to include hits in the filter. The distance can be a
numeric value, and then the ``distance_unit`` (either ``mi``/@miles@ or
``km`` can be set) controlling the unit. Or a single string with the
unit as well.
``distance_type``
How to compute the distance. Can either be ``arc`` (better precision) or
``plane`` (faster). Defaults to ``arc``.
``optimize_bbox``
Will an optimization of using first a bounding box check will be used.
Defaults to ``memory`` which will do in memory checks. Can also have
values of ``indexed`` to use indexed value check (make sure the
``geo_point`` type index lat lon in this case), or ``none`` which
disables bounding box optimization.
geo\_point Type
===============

The filter **requires** the ``geo_point`` type to be set on the relevant
field.

Multi Location Per Document
===========================

The ``geo_distance`` filter can work with multiple locations / points
per document. Once a single location / point matches the filter, the
document will be included in the filter.

Caching
=======

The result of the filter is not cached by default. The \`\_cache\` can
be set to \`true\` to cache the **result** of the filter. This is handy
when the same point and distance parameters are used on several (many)
other queries. Note, the process of caching the first execution is
higher when caching (since it needs to satisfy different queries).



