<?php
  header('Content-Type: text/csv');
  header('Content-Disposition: attachment; filename="export.csv"');
  $output = fopen('php://output', 'w');
  fputcsv($output, array('Name', 'Age', 'City'));
  // Add data rows here
  fclose($output);
?>
