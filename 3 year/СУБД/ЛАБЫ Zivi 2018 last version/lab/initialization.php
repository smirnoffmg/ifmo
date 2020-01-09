<?
/*
	Скрипт с начальными установками приложения
*/
 
// Главная директория
$main_directory='/lab1/';
 
/*
	Переменная для хранения данных о БД.
 
	В данных о таблице:
 
		name	- название таблицы в БД;
		label	- название таблицы для пользователя;
		fields	- данные о полях (столбцах) таблицы:
 
					name		- название поля (столбца) в БД;
					label		- название поля (столбца) для пользователя;
					f_table		- название главной (связываемой) таблицы в БД;
					f_field		- название связываемого столбца в БД (из главной таблицы);					
					f_select	- название столбца в БД, из главной таблицы, выводимого пользователю вместо ключевого.

В случае, если в таблице присутствуют столбцы с одинаковыми названиями (такое бывает при соединении таблиц), вы можете добавить таким столбцам псевдонимы через конструкцию AS, как это показано в 4 таблице примера.
*/
 
$tables=array
	(
	1=>array
		(
		'name'=>'clientDB', 'label'=>'БД Клиентов', 'fields'=>array
			(
			array('name'=>'ID Client', 'label'=>'ID Клиента'),
			array('name'=>'Family', 'label'=>'Фамилия'),
			array('name'=>'Name', 'label'=>'Имя'),
			array('name'=>'Othestvo', 'label'=>'Отчество'),
            array('name'=>'Address', 'label'=>'Адрес'),
            array('name'=>'Telephon', 'label'=>'Телефон')
            )
        ),

    2=>array
		(
		'name'=>'Supply', 'label'=>'Поставщики и производители', 'fields'=>array
			(
			array('name'=>'IDMaterial', 'label'=>'ID Товара'),
			array('name'=>'Name', 'label'=>'Название товара'),
			array('name'=>'price', 'label'=>'Цена'), 
            array('name'=>'SupplyName', 'label'=>'Поставщик'),
            array('name'=>'Production','label'=>'Производитель'),
			)
		),
	3=>array
		(
		'name'=>'employeePD', 'label'=>'ПД Сотрудников', 'fields'=>array
			(
			array('name'=>'employeeID', 'label'=>'ID Сотрудника'),
			array('name'=>'Family', 'label'=>'Фамилия'),
			array('name'=>'Name', 'label'=>'Имя'),
			array('name'=>'Othestvo', 'label'=>'Отчество'),
			array('name'=>'Telephon', 'label'=>'Телефон'),
			array('name'=>'Position', 'label'=>'Должность'),
			)
		),
	4=>array
		(
		'name'=>'Pricelist', 'label'=>'Оказываемые услуги', 'fields'=>array
			( 
			array('name'=>'serviceID', 'label'=>'ID Услуги'),
			array('name'=>'price', 'label'=>'Цена'),
			array('name'=>'description', 'label'=>'Описание'),
			)
		),
	5=>array
		(
		'name'=>'PriceMaterial', 'label'=>'ПрейскурантМатериалы', 'fields'=>array
			(
			array('name'=>'serviceID', 'label'=>'ID Услуги','f_table'=>'Pricelist', 'f_field'=>'serviceID', 'f_select'=>'`Pricelist`.`description`'),
			array('name'=>'IDMaterial', 'label'=>'ID Товара','f_table'=>'Supply', 'f_field'=>'IDMaterial', 'f_select'=>'`Supply`.`Name`'),
			)
		),

6=>array
		(
		'name'=>'PriceClientLog', 'label'=>'УслугиЛоги', 'fields'=>array
			(
			array('name'=>'serviceID', 'label'=>'ID услуги','f_table'=>'Pricelist', 'f_field'=>'serviceID', 'f_select'=>'`Pricelist`.`description`'),
			array('name'=>'LogID', 'label'=>'ID лога','f_table'=>'ClientLog', 'f_field'=>'LogID', 'f_select'=>'`ClientLog`.`Date`'),
			)
		),
		
7=>array
		(
		'name'=>'ClientLog', 'label'=>'ЖурналУслуг',
 'fields'=>array
			(
			array('name'=>'LogID', 'label'=>'ID Запись'),
			array('name'=>'employeeID', 'label'=>'ID Сотрудника', 'f_table'=>'employeePD', 'f_field'=>'employeeID', 'f_select'=>'`employeePD`.`Family` AS sotrudnic_fio'),
            array('name'=>'ID Client', 'label'=>'ID Клиент', 'f_table'=>'clientDB', 'f_field'=>'ID Client', 'f_select'=>'`clientDB`.`Family`'),
            array('name'=>'Date', 'label'=>'Дата'),
            array('name'=>'Time', 'label'=>'Время'),
			)
		),
8=>array
		(
		'name'=>'security_user', 'label'=>'Пользователи', 'fields'=>array
			(
			array('name'=>'id', 'label'=>'№'),
			array('name'=>'login', 'label'=>'Логин'),
			array('name'=>'password', 'label'=>'Пароль', 'type'=>'password'),
			array('name'=>'rights', 'label'=>'Права на таблицы', 'array_count'=>8)
			)
		)
);
 
// Если передан идентификатор таблицы, он присваивается переменной menu_id, иначе - присваивается 0
$menu_id=isset($_GET['menu_id']) ? $_GET['menu_id'] : 0;
// Переменная для хранения HTML-кода страницы
$body='';
// Переменная для хранения требуемого действия (отображение таблицы, модификация данных, ...)
$tables_action=isset($_GET['tables_action']) ? $_GET['tables_action'] : '';
// Переменная для хранения текста системного сообщения
$msg=isset($_GET['msg']) ? urldecode($_GET['msg']) : '';
// Переменная для хранения заголовка страницы
$title_text=$menu_id > 0 ? $tables[$menu_id]['label'] : 'Главная страница';
// Переменная для хранения идентификатора ключевого поля таблицы
$key_id=isset($tables[$menu_id]['key_id']) ? $tables[$menu_id]['key_id'] : 0;
 
// Производится подключение к БД
$mysqli=new mysqli('localhost', 'q921756a_user', '5SzGyT*W', 'q921756a_user');
if($mysqli->connect_errno)
	{
	$msg='Не удалось подключиться к БД.';
	}
else
	{
	// Задается UTF8 в качестве набора символов по умолчанию
	$mysqli->set_charset('utf8');
	}
?>