<?
/*
	Скрипт для модификации данных в БД
*/
 
$title_text.='. Изменение данных.';
 
// Из БД извлекаются данные, которые должны быть изменены
$query="SELECT * FROM `".$tables[$menu_id]['name']."` WHERE `".$tables[$menu_id]['fields'][$key_id]['name']."`='".$_GET['key_value']."'";
$old_datas=$mysqli->query($query)->fetch_assoc();
 
// Подключается скрипт с функциями для работы с полями таблиц БД
require_once 'fields.php';
 
//	Если имеются данные, введенные пользователем
if(isset($_GET['fields']))
	{
	// Формируется SQL-запрос к БД
	$query="";
	// В цикле по всем столбцам таблицы
	foreach($tables[$menu_id]['fields'] as $field_key=>$field_data)
		{
		// Если для текущего столбца заданы данные
		if (isset($_GET['fields'][$field_data['name']]) && $_GET['fields'][$field_data['name']]!='')
			{
			// Если обрабатывается не первая пара "столбец-данные", проставляется разделитель - запятая
			$query.=( $query == '' ) ? '' : ', ';
			// Добавляются название столбца и данные, введенные пользователем и отформатированные в соответствии с типом поля
			$query.="`".$field_data['name']."`='".format_insertion_fields($field_data)."'";
			}
		}
	$query="UPDATE ".$tables[$menu_id]['name']." SET ".$query." WHERE `".$tables[$menu_id]['fields'][$key_id]['name']."`='".$_GET['key_value']."'";
	$result=$mysqli->query($query);
	if($mysqli->errno)
		{
		$msg='Ошибка обновления данных.';
		}
	else
		{
		$msg='Данные успешно обновлены.';
		//header('Refresh: 0; url='.$main_directory.'?tables_action=select&menu_id='.$menu_id.'&msg='.urlencode($msg));
		}
	}
 
// Подключается скрипт, формирующий форму для ввода данных в БД
include 'editform.php';
?>
