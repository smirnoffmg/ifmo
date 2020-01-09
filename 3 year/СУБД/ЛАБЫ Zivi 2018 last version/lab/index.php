<?
// Подключается скрипт с начальными установками
require_once 'initialization.php';
require_once 'security.php';

// Подключается скрипт формирующий меню
include 'menu.php';
// Подключается скрипт формирующий заголовок HTML-страницы
include 'header.php';
// Выводится системное сообщение и содержимое страницы
echo '<div class="error_msg">'.$msg.'</div>'.$body;
// Подключается скрипт с тегами завершающими HTML-страницу
include 'footer.php';
?>
