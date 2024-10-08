
========
 Mapper 
========




—-
layout: guide
title: Mapper
cat: guide
sidebar: reference\_index\_modules
—-

The mapper module acts as a registry for the type mapping definitions
added to an index either when creating it or by using the put mapping
api. It also handles the dynamic mapping support for types that have no
explicit mappings pre defined. For more information about mapping
definitions, check out the `mapping
section </guide/reference/mapping>`_.

Dynamic / Default Mappings
--------------------------

Dynamic mappings allow to automatically apply generic mapping definition
to types that do not have mapping pre defined or applied to new mapping
definitions (overridden). This is mainly done thanks to the fact that
the ``object`` type and namely the root ``object`` type allow for schema
less dynamic addition of unmapped fields.

The default mapping definition is plain mapping definition that is
embedded within ElasticSearch:

::

    {
        default : {
        }
    }

Pretty short, no? Basically, everything is defaulted, especially the
dynamic nature of the root object mapping. The default mapping
definition can be overridden in several manners. The simplest manner is
to simply define a file called ``default-mapping.json`` and placed it
under the ``config`` directory (which can be configured to exist in a
different location). It can also be explicitly set using the
``index.mapper.default_mapping_location`` setting.

Dynamic creation of mappings for unmapped types can be completely
disabled by setting ``index.mapper.dynamic`` to ``false``.



