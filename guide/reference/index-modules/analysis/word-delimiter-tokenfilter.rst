
=============================
 Word Delimiter Token Filter 
=============================




—-
layout: guide
title: Word Delimiter Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

Named ``word_delimiter``, it Splits words into subwords and performs
optional transformations on subword groups. Words are split into
subwords with the following rules:

-  split on intra-word delimiters (by default, all non alpha-numeric
   characters).
-  “Wi-Fi” -> “Wi”, “Fi”
-  split on case transitions: “PowerShot” -> “Power”, “Shot”
-  split on letter-number transitions: “SD500” -> “SD”, “500”
-  leading and trailing intra-word delimiters on each subword are
   ignored: “//hello—-there, 'dude’” -> “hello”, “there”, “dude”
-  trailing “'s” are removed for each subword: “O’Neil’s” -> “O”, “Neil”

Parameters include:

-  ``generate_word_parts``: If ``true`` causes parts of words to be
   generated: “PowerShot” => “Power” “Shot”. Defaults to ``true``.
-  ``generate_number_parts``: If ``true`` causes number subwords to be
   generated: “500-42” => “500” “42”. Defaults to ``true``.
-  ``catenate_words``: If ``true`` causes maximum runs of word parts to
   be catenated: “wi-fi” => “wifi”. Defaults to ``false``.
-  ``catenate_numbers``: If ``true`` causes maximum runs of number parts
   to be catenated: “500-42” => “50042”. Defaults to ``false``.
-  ``catenate_all``: If ``true`` causes all subword parts to be
   catenated: “wi-fi-4000” => “wifi4000”. Defaults to ``false``.
-  ``split_on_case_change``: If ``true`` causes “PowerShot” to be two
   tokens; (“Power-Shot” remains two parts regards). Defaults to
   ``true``.
-  ``preserve_original``: If ``true`` includes original words in
   subwords: “500-42” => “500” “42” “500-42”. Defaults to ``false``.
-  ``split_on_numerics``: If ``true`` causes “j2se” to be three tokens;
   “j” “2” “se”. Defaults to ``true``.
-  ``stem_english_possessive``: If ``true`` causes trailing “'s” to be
   removed for each subword: “O’Neil’s” => “O”, “Neil”. Defaults to
   ``true``.

Advance settings include:

``protected_words``: A list of protected words from being delimiter.
Either an array, or also can set ``protected_words_path`` which resolved
to a file configured with protected words (one on each line).
Automatically resolves to ``config/`` based location if exists.

``type_table``: A custom type mapping table, for example (when
configured using ``type_table_path``):

::

        # Map the $, %, '.’, and ',’ characters to DIGIT 
        # This might be useful for financial data.
        $ => DIGIT
        % => DIGIT
        . => DIGIT
        \u002C => DIGIT

        # in some cases you might not want to split on ZWJ
        # this also tests the case where we need a bigger byte[]
        # see http://en.wikipedia.org/wiki/Zero-width_joiner
        \u200D => ALPHANUM




