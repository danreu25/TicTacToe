<?php
if (isset($_GET['script'])) {
    $script = $_GET['script'];
    // Execute the appropriate Python script based on the button pressed
    $output = shell_exec("python $script");
    echo $output;
} else {
    echo "No script specified.";
}
?>
