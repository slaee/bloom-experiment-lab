<?php
  libxml_use_internal_errors(true);
  $xml = new DOMDocument;
  $xml->load('data.xml');
  $xsd = new DOMDocument;
  $xsd->load('schema.xsd');
  if ($xml->schemaValidate($xsd)) {
    echo "XML is valid against the XSD schema.";
  } else {
    echo "XML is not valid against the XSD schema.";
  }
?>
