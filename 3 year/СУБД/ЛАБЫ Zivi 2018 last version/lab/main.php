<?
//НЕ имеет никакого отношения к php инъекции=)
if (isset($_GET['inf']))
    $data=$_GET["inf"];
else
    $data='./inf/information.php';

include($data);

?>
