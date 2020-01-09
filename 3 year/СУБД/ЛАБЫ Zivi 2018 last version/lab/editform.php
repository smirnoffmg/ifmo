<?
/*	Редактирование записей БД*/
 
$body.='Модификация таблицы: '.$tables[$menu_id]['label'].'<br>';
$body.='<a href="'.$main_directory.'?tables_action=select&menu_id='.$menu_id.'">Назад</a><br>';
// Форма редактирования
$body.='<form method="get" action="'.$main_directory.'">';
	// Скрытые поля для передачи данных о таблице и действии в обрабатывающий скрипт
	$body.='<input type="hidden" name="menu_id" value="'.$menu_id.'">';
	$body.='<input type="hidden" name="tables_action" value="'.$tables_action.'">';
	// Скрытое поле для хранения идентификатора модифицируемой записи таблицы
	$body.='<input type="hidden" name="key_value" value="'.$_GET['key_value'].'">';
 
	$body.='<table>';
	foreach($tables[$menu_id]['fields'] as $field_key => $field_data)
		{
		$body.='<tr>';
			$body.='<td>'.$field_data['label'].'</td>';
			// Формирование поля в соответствии с его типом (текстовое, поля выбора, ...)
			$body.='<td>'.show_field($field_data).'</td>';
		$body.='</tr>';
		}
	$body.='</table>';
 
	$body.='<input type="submit" value="Сохранить">';
$body.='</form>';
?>
