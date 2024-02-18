// index.php

<?php
session_start();
require_once("fs.php");

$userspace = md5(session_id());
$fs = new GuestFS("../root/$userspace/");

$mode = !empty($_POST['mode']) ? (string)$_POST['mode'] : "*";
$name = !empty($_POST['name']) ? (string)$_POST['name'] : "*";

$error = null;
try {
    switch($mode) {
        case "create":
            $type = isset($_POST['type']) ? 1 : 0;
            $target = !empty($_POST['target']) ? (string)$_POST['target'] : "*";
            $fs->create($name, $type, $target);
            break;

        case "read":
            $size = !empty($_POST['size']) ? (int)$_POST['size'] : -1;
            $offset = !empty($_POST['offset']) ? (int)$_POST['offset'] : 0;
            $contents = $fs->read($name, $size, $offset);
            break;

        case "write":
            $data = !empty($_POST['data']) ? (string)$_POST['data'] : "";
            $offset = !empty($_POST['offset']) ? (int)$_POST['offset'] : 0;
            $fs->write($name, $data, $offset);
            break;

        case "delete":
            $fs->delete($name);
            break;
    }
} catch(Exception $e) {
    $error = $e->getMessage();
}

$listdir = $fs->listup();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
              integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"
                integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg=="
                crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
                integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
                crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
                integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
                crossorigin="anonymous"></script>

        <title>Your Workspace</title>
    </head>

    <body>
        <div class="container">
            <h2 class="mt-5">Your Workspace</h2>
            <?php if (!empty($error)) { ?>
                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>ERROR </strong><?= htmlspecialchars($error) ?>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            <?php } ?>
            <?php if (isset($contents)) { ?>
                <div class="card">
                    <div class="card-header">Contents of <?= htmlspecialchars($name) ?></div>
                    <div class="card-body">
                        <p class="card-text"><?= nl2br(htmlspecialchars($contents)) ?></p>
                    </div>
                </div>
            <?php } ?>

            <!-- Create -->
            <hr>
            <h4 class="mt-1">Create a File</h4>
            <form method="POST" action="/">
                <div class="form-group">
                    <label for="new-name">Filename</label>
                    <input id="new-name" type="text" class="form-control" placeholder="filename" name="name" required>
                </div>
                <div class="form-group">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="type" value="" id="new-type">
                        <label class="form-check-label" for="new-type">Symbolic Link</label>
                    </div>
                </div>
                <div class="form-group" id="new-target-group">
                    <label for="new-target">Target</label>
                    <input id="new-target" type="text" class="form-control" placeholder="target path" name="target">
                </div>
                <input type="hidden" name="mode" value="create">
                <button type="submit" class="btn btn-primary">Create File</button>
                <script>
                 $(function() {
                     $('[id=new-target-group]').hide();
                     $('[name="type"]:checkbox').change(function() {
                         $('[id=new-target-group]').fadeToggle();
                     });
                 });
                </script>
            </form>

            <!-- File List -->
            <hr>
            <h4 class="mt-1">Your Files</h4>
            <div id="workspace">
                <?php $id = 0; ?>
                <?php foreach($listdir as $filename => $attribute) { ?>
                    <div class="card">
                        <div class="card-header" id="file-<?= $id ?>-head">
                            <h5 class="mb-0">
                                <button class="btn btn-link" data-toggle="collapse" aria-expanded="false" 
                                        data-target="#file-<?= $id ?>-body" aria-controls="file-<?= $id ?>-body">
                                    <?= htmlspecialchars($filename) ?>
                                </button>
                            </h5>
                        </div>
                    </div>
                    <div id="file-<?= $id ?>-body" class="collapse" aria-labelledby="file-<?= $id ?>-head" data-parent="#workspace">
                        <div class="card-body">
                            <p>Type: <?= htmlspecialchars($attribute) ?></p>
                            <form method="POST" action="/">
                                <input type="hidden" name="name" value="<?= htmlspecialchars($filename); ?>">
                                <input type="hidden" name="mode" value="read">
                                <input type="submit" class="btn btn-success" value="Read">
                            </form>
                            <hr>
                            <form method="POST" action="/">
                                <div class="form-group">
                                    <label for="edit-<?= $id ?>">Contents</label>
                                    <textarea class="form-control" id="edit-<?= $id ?>" name="data" rows="3"></textarea>
                                </div>
                                <input type="hidden" name="name" value="<?= htmlspecialchars($filename); ?>">
                                <input type="hidden" name="mode" value="write">
                                <input type="submit" class="btn btn-success" value="Write">
                            </form>
                            <hr>
                            <form method="POST" action="/">
                                <input type="hidden" name="name" value="<?= htmlspecialchars($filename); ?>">
                                <input type="hidden" name="mode" value="delete">
                                <input type="submit" class="btn btn-danger" value="Delete">
                            </form>
                        </div>
                    </div>
                    <?php $id++; ?>
                <?php } ?>
            </div>
        </div>
    </body>
</html>

// fs.php

<?php
/**
 * GuestFS is a simple file server.
 *
 *  - Every user has a root directory (user-space)
 *  - Users can put files in their user-space
 */
class GuestFS {
    function __construct($root)
    {
        if (!is_dir($root)) {
            mkdir($root, 0755);
        }
        $this->root = $root;
    }

    /**
     * Create a new file
     *
     * @param string $name Filename to create
     * @param int $type File type (0:normal/1:symlink)
     * @param string $link Path to the real file (when $type=1)
     */
    function create($name, $type=0, $target="")
    {
        $this->validate_filename($name);

        if ($type === 0) {

            /* Create an empty file */
            $fp = @fopen($this->root.$name, "w");
            @fwrite($fp, '');
            @fclose($fp);

        } else {

            /* Target file must exist */
            $this->assert_file_exists($this->root.$target);

            /* Create a symbolic link */
            @symlink($target, $this->root.$name);

            /* This check ensures $target points to inside user-space */
            try {
                $this->validate_filepath(@readlink($this->root.$name));
            } catch(Exception $e) {
                /* Revert changes */
                @unlink($this->root.$name);
                throw $e;
            }

        }
    }

    /**
     * Read a file
     *
     * @param string $name Filename to read
     * @param int $offset Offset to read
     */
    function read($name, $size=-1, $offset=0)
    {
        /* Check filename, size and offset */
        $this->validate_filename($name);
        $this->assert_file_exists($this->root.$name);
        $size = $this->validate_bounds($this->root.$name, $size, $offset);

        /* This may alleviate heavy disk load. */
        usleep(500000);

        /* Read contents */
        $fp = @fopen($this->root.$name, "r");
        @fseek($fp, $offset, SEEK_SET);
        $buf = @fread($fp, $size);
        @fclose($fp);

        return $buf;
    }

    /**
     * Write to a file
     *
     * @param string $name Filename to write
     * @param string $data Contents to write
     * @param int $offset Offset to write
     */
    function write($name, $data, $offset=0)
    {
        /* We don't call validate_bounds to allow appending data */
        $this->validate_filename($name);
        $this->assert_file_exists($this->root.$name);

        /* This may alleviate heavy disk load. */
        usleep(500000);

        /* Write contents */
        $fp = @fopen($this->root.$name, "w");
        @fseek($fp, $offset, SEEK_SET);
        @fwrite($fp, $data);
        @fclose($fp);
    }

    /**
     * Delete a file
     *
     * @param string $name Filename to delete
     */
    function delete($name)
    {
        $this->validate_filename($name);
        $this->assert_file_exists($this->root.$name);

        @unlink($this->root.$name);        
    }

    /**
     * List files in the user space
     */
    function listup()
    {
        $result = array();

        $list = array_diff(scandir($this->root), array('..', '.'));
        foreach($list as $key => $value) {
            if (is_link($this->root.$value)) {
                $result[$value] = "Symlink to ".@readlink($this->root.$value);
            } else {
                $result[$value] = "Regular file";
            }
        }

        return $result;
    }

    /* Security Functions */
    function validate_filepath($path)
    {
        if (strpos($path, "/") === 0) {
            throw new Exception('invalid filepath (absolute path)');
        } else if (strpos($path, "..") !== false) {
            throw new Exception('invalid filepath (outside user-space)');
        }
    }

    function validate_filename($name)
    {
        if (preg_match('/[^a-z0-9]/i', $name)) {
            throw new Exception('invalid filename');
        }
    }

    function assert_file_exists($name)
    {
        if (file_exists($name) === false
            && is_link($name) === false) {
            throw new Exception('file not found');
        }
    }

    function validate_bounds($path, $size, $offset)
    {
        $st = @stat($path);
        if ($offset < 0) {
            throw new Exception('offset must be positive');
        }
        if ($size < 0) {
            $size = $st['size'] - $offset;
            if ($size < 0) {
                throw new Exception('offset is larger than file size');
            }
        }
        if ($size + $offset > $st['size']) {
            throw new Exception('trying to read out of bound');
        }
        return $size;
    }
}
?>
