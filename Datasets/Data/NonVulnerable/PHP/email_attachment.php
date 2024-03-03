<?php
  $to = 'recipient@example.com';
  $subject = 'Attachment Test';
  $message = 'Check out the attachment.';
  $attachment = 'file.pdf';

  $headers = 'From: sender@example.com' . "\r\n" .
    'Reply-To: sender@example.com' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

  mail($to, $subject, $message, $headers, $attachment);
?>
