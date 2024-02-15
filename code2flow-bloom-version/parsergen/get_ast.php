<?php
require_once __DIR__ . '/vendor/autoload.php';

use PhpParser\Error;
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

$code = file_get_contents($argv[1]);

$parser = (new ParserFactory())->createForNewestSupportedVersion();

function walk($node) {
    global $variables;

    if ($node instanceof PhpParser\Node\Expr\ArrayDimFetch) {
        $variables[] = '$'.$node->var->name."['".$node->dim->value."']";
    }

    if ($node instanceof PhpParser\Node\Expr\Variable) {
        $variables[] = '$'.$node->name;
    }

    foreach ($node->getSubNodeNames() as $subNodeName) {
        $subNode = $node->$subNodeName;
        if ($subNode instanceof PhpParser\Node) {
            walk($subNode);
        }
    }
}

try {
    $stmts = $parser->parse($code);
    $variables = array();

    foreach ($stmts as $stmt) {
        walk($stmt);
    }

    // remove all duplicates
    $variables = array_unique($variables);

    // remove all $_GET, $_POST, $_SERVER, $_COOKIE, $_SESSION, $_FILES, $_ENV with no array shim '[]'
    $variables = array_filter($variables, function($var) {
        if (preg_match('/\$_(GET|POST|SERVER|COOKIE|SESSION|FILES|ENV)\b/', $var)
        && strpos($var, '[') === false) {
            return false;
        }

        return true;
    });

    print_r($variables);
    // echo json_encode($stmts, JSON_PRETTY_PRINT), "\n";

} catch (PhpParser\Error $e) {
    echo 'Parse Error: ', $e->getMessage();
    exit(1);
}

?>