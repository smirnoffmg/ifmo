<?
/*
	Скрипт для вставки данных в БД
*/
 
$title_text .= '. Добавление данных.';
$old_datas = $_GET['fields'];
 
// Подключается скрипт с функциями для работы с полями таблиц БД
require_once 'fields.php';
 
//	Если имеются данные, введенные пользователем
if(isset($_GET['fields']))
	{
	// Переменная для хранения списка использованных полей (для SQL-запроса)
	$query_fields = '';
	// Переменная для хранения введенных пользователем данных (для SQL-запроса)
	$query_data = '';
	// В цикле по всем столбцам таблицы
	foreach ($tables[$menu_id]['fields'] as $field_key => $field_data)
		{
		//Если для текущего столбца заданы данные
		if (isset($_GET['fields'][$field_data['name']]) && $_GET['fields'][$field_data['name']]!='')
			{
			// Если обрабатывается не первая пара "столбец-данные", проставляются разделители - запятые
			$query_fields .= ($query_fields=='') ? '' : ', ';
			$query_data .= ($query_data=='') ? '' : ', ';
			// Записываются название поля и данные в нем
			$query_fields .= "`".$field_data['name']."`";
			$query_data .= "'".format_insertion_fields($field_data)."'";				
			}
		}
	// Формируется SQL-запрос к БД
	$query = "INSERT INTO ".$tables[$menu_id]['name']." ($query_fields) VALUES ($query_data)";
	$result = $mysqli->query($query);
	if($mysqli->errno)
		{
		$msg = 'Ошибка вставки данных.';
		}
	else
		{
		$msg = 'Данные успешно добавлены.';
		//header('Refresh: 0; url='.$main_directory.'?tables_action=select&menu_id='.$menu_id.'&msg='.urlencode($msg));
		}
	}
 
// Подключается скрипт, формирующий форму для ввода данных в БД
include 'editform.php';
?>
