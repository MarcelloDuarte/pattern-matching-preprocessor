--DESCRIPTION--

Test matching with a catch all _ clause

--GIVEN--

$y = $x match {
    1 => "one",
    2 => "two",
    _ => "many"
}

--EXPECT--

$y = (function($declaredVars·cfcd208495d565ef66e7dff9f98764da) use ($x) {
    extract($declaredVars·cfcd208495d565ef66e7dff9f98764da);
    $on·cfcd208495d565ef66e7dff9f98764da = match($x); switch(true) {
        case $on·cfcd208495d565ef66e7dff9f98764da(1): "one"; break;
        case $on·cfcd208495d565ef66e7dff9f98764da(2): "two"; break;
        case $on·cfcd208495d565ef66e7dff9f98764da(_): "many"; break;

    }
})(get_defined_vars())
