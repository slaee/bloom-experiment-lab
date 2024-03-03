<?php
  $xml = new SimpleXMLElement('<root></root>');
  $xml->addChild('element', 'Hello, XML!');
  $xml->asXML('output.xml');
?>
