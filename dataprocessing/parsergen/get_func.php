<?php
require_once __DIR__ . '/vendor/autoload.php';

use PhpParser\{Error, ParserFactory};

$filename = $argv[1];

if (!file_exists($filename)) {
    echo "File does not exist: $filename\n";
    exit(1);
}

$code = file_get_contents($filename);

$parser = (new ParserFactory())->createForNewestSupportedVersion();

function extractFunctions($node, &$functions) {
    if ($node instanceof PhpParser\Node\Stmt\Function_) {
        $functions[] = $node->name->name;
    }

    foreach ($node->getSubNodeNames() as $subNodeName) {
        $subNode = $node->$subNodeName;
        if ($subNode instanceof PhpParser\Node) {
            extractFunctions($subNode, $functions);
        }
    }
}

try {
    $stmts = $parser->parse($code);
    $functions = array();

    foreach ($stmts as $stmt) {
        extractFunctions($stmt, $functions);
    }

    // Remove duplicates from functions
    $functions = array_unique($functions);

    // Sort the functions based on their appearance in the code
    usort($functions, function ($a, $b) use ($code) {
        return strpos($code, $a) <=> strpos($code, $b);
    });

    // Output functions
    echo "Functions:\n";
    foreach ($functions as $function) {
        echo $function . "\n";
    }

} catch (PhpParser\Error $e) {
    echo 'Parse Error: ', $e->getMessage();
    exit(1);
}
?>
