--DESCRIPTION--

Test simplest matching

--GIVEN--

$x match {
    42 => "bazinga"
}

--EXPECT--

(function () use ($x) {
    $on·cfcd208495d565ef66e7dff9f98764da = match($x);
    $mdPatternMatchingReturnValue·cfcd208495d565ef66e7dff9f98764da = null;
    switch (true) {
    case $on·cfcd208495d565ef66e7dff9f98764da(42): $mdPatternMatchingReturnValue·cfcd208495d565ef66e7dff9f98764da = "bazinga"
;
    break;
}
    return $mdPatternMatchingReturnValue·cfcd208495d565ef66e7dff9f98764da;
})();

