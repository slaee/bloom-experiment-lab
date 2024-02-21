<?php

$finder = (new PhpCsFixer\Finder())
    ->in(__DIR__)
;

return (new PhpCsFixer\Config())
    ->setRules([
        'strict_param' => false,
        'control_structure_braces' => true,
    ])
    ->setFinder($finder)
;