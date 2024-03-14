<?php include("../common/header.php"); ?>

<?php hint("not everything you need to play with is in a text field"); ?>

<form action="/LFI-11/index.php" method="POST">
    <input type="text" name="file">
    <input type="hidden" name="style" name="stylepath">
</form>

<?php include($_POST['stylepath']); ?>