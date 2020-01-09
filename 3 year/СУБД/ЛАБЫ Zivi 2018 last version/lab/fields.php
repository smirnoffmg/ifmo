<?
/*
	Скрипт с функциями по работе с полями таблиц и данными, переданными через них
*/
 
// Функция формирования HTML-тега для поля ввода в зависимости от типа поля таблицы
function show_field($field_data_local)
	{
	// Глобальные переменные
	global $mysqli, $old_datas;
	// Данные, уже имеющиеся в поле
	$old_data=isset($old_datas[$field_data_local['name']]) ? $old_datas[$field_data_local['name']] : NULL;
	$body_local = '';
	// Если у поля указана таблица для связи
	if(isset($field_data_local['f_table']))
		{// Формируется запрос к БД для выбора всех возможных значений поля
		$query = 'SELECT `'.$field_data_local['f_table'].'`.`'.$field_data_local['f_field'].'`, '.$field_data_local['f_select'].' FROM `'.$field_data_local['f_table'].'`';
		// Запрос отправляется в БД
		$result = $mysqli->query($query);
 
		// Формируется HTML-тег для вывода списка возможных значений
		$body_local.='<select name="fields['.$field_data_local['name'].']">';
		// Цикл по всем возможным значениям
		while($row = $result->fetch_row())
			{// Если идентификатор записи (0-столбец) равен уже введенным ранее данным, пункт помечается как выбранный
			$body_local.='<option value="'.$row[0].'"'.(($row[0]==$old_data) ? " selected" : "").">".$row[1]."</option>";
			}
		$body_local.='</select>';
		}
	// Если у поля указано количество элементов массива, тип поля - массив данных
	else if (isset($field_data_local['array_count']))
		{
		// Если нет ранее введенных данных, в качестве них формируется массив из соответствующего количества элементов
		$old_data = is_null($old_data) ? array_fill(1, $field_data_local['array_count'], '') : unserialize($old_data);
		// Цикл вывода полей в количестве, соответствующем количеству элементов массива
		for($i=1;$i<=$field_data_local['array_count'];$i++)
			{
			$body_local.=' '.$i.': <input class="array_input" type="text" name="fields['.$field_data_local['name'].']['.$i.']" value="'.$old_data[$i].'">;';
			}
		}
	// Во всех остальных случаях формируется HTML-тег поля input
	else
		{// Если не указан тип поля, используется тип text, иначе - указанный тип (text, password, date, datetime-local, ...)
		$body_local.='<input type="'.(isset($field_data_local['type']) ? $field_data_local['type'] : 'text').'" name="fields['.$field_data_local['name'].']" value="'.$old_data.'">';
		}
	// Функция возвращает сформированный HTML-тег поля ввода
	return $body_local;
	}
 
 
// Функция для предварительной обработки данных, полученных от пользователя
function format_insertion_fields($field_data_local)
	{
	// Глобальные переменные 
	global $tables_action, $old_datas;
 
	// Если тип поля, для которого переданы данные - password и данные в поле были изменены
	if(isset($field_data_local['type']) && $field_data_local['type']=='password' && ($tables_action=='insert' || $_GET['fields'][$field_data_local['name']]!=$old_datas[$field_data_local['name']]))
		{// Функция возвращает данные поля, хэшированные алгоритмом md5
		return md5($_GET['fields'][$field_data_local['name']]);
		}
	// Если тип поля, для которого переданы данные - массив
	else if (isset($field_data_local['array_count']))
		{
		//В цикле все данные, если это числа, приводятся к целочисленному типу
		foreach($_GET['fields'][$field_data_local['name']] as $key => $val) 
			if(is_numeric($val))
				{$_GET['fields'][$field_data_local['name']][$key]=(int)$val;}
		// Функция возвращает сериализованный массив, пригодный для хранения в БД (в виде строки)
		return serialize($_GET['fields'][$field_data_local['name']]);
		}
	// Если поле - обычное текстовое поле ввода
	else
		{// Функция возвращает данные в неизменном виде
		return $_GET['fields'][$field_data_local['name']];
		}
	}
?>
