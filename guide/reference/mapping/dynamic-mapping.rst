
=================
 Dynamic Mapping 
=================




—-
layout: guide
title: Dynamic Mapping
cat: guide
sidebar: reference\_mapping
—-

Default mappings allow to automatically apply generic mapping definition
to types that do not have mapping pre defined. This is mainly done
thanks to the fact that the `object mapping <object-type.html>`_ and
namely the `root object mapping <root-object-type.html>`_ allow for
schema-less dynamic addition of unmapped fields.

The default mapping definition is plain mapping definition that is
embedded within the distribution:

::

    {
        “default“ : {
        }
    }

Pretty short, no? Basically, everything is defaulted, especially the
dynamic nature of the root object mapping. The default mapping
definition can be overridden in several manners. The simplest manner is
to simply define a file called ``default-mapping.json`` and placed it
under the ``config`` directory (which can be configured to exist in a
different location). It can also be explicitly set using the
``index.mapper.default_mapping_location`` setting.

The dynamic creation of mappings for unmapped types can be completely
disabled by setting ``index.mapper.dynamic`` to ``false``.

As an example, here is how we can change the default
`date\_formats <date-format.html>`_ used in the root and inner object
types:

::

    {
        “default“ : {
            “date_formats” : [“yyyy-MM-dd”, “dd-MM-yyyy”, “date_optional_time”],
        }
    }




