<?php
require_once __DIR__ . '/vendor/autoload.php';

use PhpParser\{Error, NodeDumper, ParserFactory};

$filename = $argv[1];

if (!file_exists($filename)) {
    echo "File does not exist: $filename\n";
    exit(1);
}

$code = file_get_contents($filename);

$parser = (new ParserFactory())->createForNewestSupportedVersion();

function walk($node, &$variables, $code) {
    // Handle conditions
    if ($node instanceof PhpParser\Node\Expr\ArrayDimFetch) {
        $variables[] = '$'.$node->var->name."['".$node->dim->value."']";
    }

    if ($node instanceof PhpParser\Node\Expr\Variable) {
        $variables[] = '$'.$node->name;
    }

    if ($node instanceof PhpParser\Node\Stmt\If_
        || $node instanceof PhpParser\Node\Stmt\ElseIf_
        || $node instanceof PhpParser\Node\Stmt\Else_
    ) {
        // Handle condition expression
        $condition = $node->cond;
        if ($condition instanceof PhpParser\Node) {
            walk($condition, $variables, $code);
        }

        // Handle statements inside the if statement
        foreach ($node->stmts as $stmt) {
            if ($stmt instanceof PhpParser\Node) {
                walk($stmt, $variables, $code);
            }
        }
    }

    // Handle other statements
    foreach ($node->getSubNodeNames() as $subNodeName) {
        $subNode = $node->$subNodeName;
        if ($subNode instanceof PhpParser\Node) {
            walk($subNode, $variables, $code);
        }
    }
}

try {
    $stmts = $parser->parse($code);
    $variables = array();

    foreach ($stmts as $stmt) {
        walk($stmt, $variables, $code);
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

    // Sort the variables based on their appearance in the code
    usort($variables, function($a, $b) use ($code) {
        return strpos($code, $a) <=> strpos($code, $b);
    });

    print_r($variables);

} catch (PhpParser\Error $e) {
    echo 'Parse Error: ', $e->getMessage();
    exit(1);
}
?>
