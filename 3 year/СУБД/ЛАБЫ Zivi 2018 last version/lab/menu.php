<?
/*
	Скрипт для формирования меню приложения
*/
if($user_data['id']>0)
{
	// Формируется внешний вид меню
	$body.='<table>';
	$body.='<tr>';
 
	// Вывод ссылки на главную страницу
	$body.='<th><a href="'.$main_directory.'">'.mark_menu('Главная', 0, $menu_id).'</a></th>';


		// Пользователю отображается пункт меню по сводному отчету
		// Если у пользователя есть права на просмотр данных из таблиц (3 и 4), используемых в сводном отчете
	if($user_data['rights'][3][0]=='1' && $user_data['rights'][4][0]=='1')
		$body.='<th><a href="'.$main_directory.'?tables_action=report&menu_id=-1">'.mark_menu('Данные по ЗП', -1, $menu_id).'</a></th>';



	// В цикле по всем пунктам меню (таблицам)
	
	foreach($tables as $key=>$value)
			{// В меню выводится ссылка на просмотр текущей таблицы
			if(isset($user_data['rights'][$key][0]) && $user_data['rights'][$key][0]=='1')
			    $body.='<th><a href="'.$main_directory.'?tables_action=select&menu_id='.$key.'">'.mark_menu($value['label'], $key, $menu_id).'</a></th>';
			}
 
    
    $body.='<th><a href="'.$main_directory.'?exit=1">ВЫХОД ('.$user_data['login'].')</a></th>';
 

 
	$body.='</tr>';
	$body.='</table>';
 
 
	// Проверяется, задано ли какое-либо действие над таблицей и указана ли обрабатываемая таблица
	if(($tables_action!='' && $menu_id != 0) || $tables_action=='error')
		{
		if($tables_action=='select')
			{// Подключается модуль вывода данных
			include 'selectdata.php';
			}
		else if($tables_action=='insert')
			{// Подключается модуль вставки данных
			include 'insertdata.php';
			}
		else if($tables_action=='update')
			{// Подключается модуль редактирования данных
			include 'updatedata.php';
			}
		else if($tables_action=='delete')
			{// Подключается модуль удаления данных
			include 'deletedata.php';
			}
		else if($tables_action=='report' && $user_data['rights'][3][0]=='1' && $user_data['rights'][4][0]=='1')
			{// Подключается модуль формирования сводного отчета
			include 'report.php';
			}
			
		else
			{// Подключается модуль вывода страницы с ошибкой сервера
			include 'error.php';
			}
		}
	else
		{// Подключается модуль вывода главной страницы приложения
		include 'main.php';
		}
}
 
 
// Функция "подсветки" (выделения) активного пункта меню
function mark_menu($text, $key, $id)
	{
	if($key==$id) return '<h3>'.$text.'<h3>';
	return $text;
	}
?>
