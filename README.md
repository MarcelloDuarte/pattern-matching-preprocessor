Pattern Matching pre-processor
==============================

Pattern matching is a mechanism for checking a value against a pattern. A successful match can also deconstruct a value into its constituent parts. It is a more powerful version of the switch statement in PHP and it can likewise be used in place of a series of if/else statements.

This pre-processor will translate the operations using the pattern matching syntax below into pure PHP. This does not happen at runtime, so there is no hit on perfomance. The pre-processor works on top of the [pre](https://github.com/preprocess/pre-plugin) plugin and the [yay macro library](https://github.com/marcioAlmada/yay). 

TODO
----

 - [x] Simplest pattern matching syntax example
 - [ ] Catch all using a `case _` syntax
 - [ ] Case classes support
 - [ ] Guards support
 - [ ] Check for exhausting clauses error (sealed number of cases)
 - [ ] List deconstruction
 - [ ] Case class deconstruction

A simpler `switch` statement
----------------------------

```php
$y = $x match {
    1 => "one",
    2 => "two"
}
```

Catch all using a `case _` syntax
---------------------------------

```php
$y = $x match {
    1 => "one",
    2 => "two",
    _ => "many"
}
```

Case classes support
--------------------

Guards support
--------------

Check for exhausting clauses error (sealed number of cases)
-----------------------------------------------------------

List deconstruction
-------------------

Case class deconstruction
-------------------------


Final Notes
-----------
 - This pre-processor is alpha software. Do not use it in production.