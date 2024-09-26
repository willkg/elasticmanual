
=======================
 Truncate Token Filter 
=======================




—-
layout: guide
title: Truncate Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

The ``truncate`` token filter can be used to truncate tokens into a
specific length. This can come in handy with keyword (single token)
based mapped fields that are used for sorting in order to reduce memory
usage.

It accepts a ``length`` parameter which control the number of characters
to truncate to, defaults to ``10``.



