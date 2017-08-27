--DESCRIPTION--

Test simplest matching

--GIVEN--

$x match {
    42 => "bazinga"
}

--EXPECT--

(function($declaredVars·cfcd208495d565ef66e7dff9f98764da) use ($x) {
    extract($declaredVars·cfcd208495d565ef66e7dff9f98764da);
    $on·cfcd208495d565ef66e7dff9f98764da = match($x); switch(true) {
        case $on·cfcd208495d565ef66e7dff9f98764da(42): "bazinga"; break;

    }
})(get_defined_vars())