<?php
require_once __DIR__ . '/vendor/autoload.php';

use PhpParser\{Error, NodeDumper, ParserFactory};

$code = file_get_contents($argv[1]);

$parser = (new ParserFactory())->createForNewestSupportedVersion();

function walk($node, &$variables) {
    if ($node instanceof PhpParser\Node\Expr\ArrayDimFetch) {
        $variables[] = '$'.$node->var->name."['".$node->dim->value."']";
    }

    if ($node instanceof PhpParser\Node\Expr\Variable) {
        $variables[] = '$'.$node->name;
    }

    foreach ($node->getSubNodeNames() as $subNodeName) {
        $subNode = $node->$subNodeName;
        if ($subNode instanceof PhpParser\Node) {
            walk($subNode, $variables);
        }
    }
}

try {
    $stmts = $parser->parse($code);
    $variables = array();

    foreach ($stmts as $stmt) {
        walk($stmt, $variables);
    }

    // Remove all duplicates
    $variables = array_unique($variables);

    // Remove all $_GET, $_POST, $_SERVER, $_COOKIE, $_SESSION, $_FILES, $_ENV with no array shim '[]'
    $variables = array_filter($variables, function($var) {
        if (preg_match('/\$_(GET|POST|SERVER|COOKIE|SESSION|FILES|ENV)\b/', $var)
        && strpos($var, '[') === false) {
            return false;
        }

        return true;
    });

    print_r($variables);

} catch (PhpParser\Error $e) {
    echo 'Parse Error: ', $e->getMessage();
    exit(1);
}
?>
