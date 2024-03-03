<?php
  $xmlString = '<user><name>John</name><age>25</age></user>';
  $xml = simplexml_load_string($xmlString);
  echo $xml->name;
?>
