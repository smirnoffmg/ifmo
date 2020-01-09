<?
/*
	Скрипт для формирования сводного отчета
*/
 
$title_text='Фильтр по работникам';
 
// Формирование участка кода SQL-запроса, отвечающего за сортировку данных
$order_line='';
if(isset($_GET['order_col']) && $_GET['order_col']!='')
	{
	$order_line.=' ORDER BY ';
	if($_GET['order_col']=='1')
		{
		$order_line.='`employeePD`.`employeeID`';
		}
	else if ($_GET['order_col']=='2')
		{
		$order_line.='`employeePD`.`Family`';
		}
	else if ($_GET['order_col']=='3')
		{
		$order_line.='`employeePD`.`Position`';
		}
	

	//Если задано,к запросу добавляется направление сортировки
	$order_line.=isset($_GET['order_style']) && $_GET['order_style']=='2' ? ' DESC' : ''; 
	}
 
// Формирование участка кода SQL-запроса, отвечающего за фильтрацию и поиск данных
$where_filter='';
if(isset($_GET['sotrudnic_fio']) && $_GET['sotrudnic_fio']!='')
	{
	$where_filter=" AND `employeePD`.`Family` LIKE '%".($_GET['sotrudnic_fio'])."%'";
	}
 
// Формируется запрос к БД
$query="
SELECT
	`employeePD`.`employeeID`,
	`employeePD`.`Family`,
	`employeePD`.`Position`,
	GROUP_CONCAT(DISTINCT `Pricelist`.`description` ORDER BY `Pricelist`.`description` ASC SEPARATOR ', ') AS All_uslugi,
	COUNT(`Pricelist`.`serviceID`) AS Number_of_clients,
    SUM(`Pricelist`.`price`) AS Zarabotok,
    SUM(`Pricelist`.`price`)-0.13*SUM(`Pricelist`.`price`) AS bez_NDS
FROM `employeePD`, `Pricelist`, `ClientLog`,`PriceClientLog`
WHERE
	`employeePD`.`employeeID`= `ClientLog`.`employeeID` AND
	`ClientLog`.`LogID`=`PriceClientLog`.`LogID` AND
    `PriceClientLog`.`serviceID`= `Pricelist`.`serviceID`
    $where_filter 
GROUP BY `employeePD`.`employeeID`

$order_line";
$result=$mysqli->query($query);
//var_dump($query);print('{----------}');
//var_dump($mysqli->error);print('{----------}');
$body.='Информация о заработке сотрудников:';
 
// Формирование формы для ввода условий запроса к БД
$body.='<form action="'.$main_directory.'" method="get">';
 
$body.='<input type="hidden" name="tables_action" value="'.$tables_action.'">';
$body.='<input type="hidden" name="menu_id" value="'.$menu_id.'">';
 
$body.='<br>Сортировка по столбцу ';
$body.='<select name="order_col">';
	$body.='<option value=""></option>';
	$body.='<option value="1"'.($_GET['order_col']==1 ? ' selected' : '').'>ID сотрудника</option>';
	$body.='<option value="2"'.($_GET['order_col']==2 ? ' selected' : '').'>Фамилия</option>';
	$body.='<option value="3"'.($_GET['order_col']==3 ? ' selected' : '').'>Должность</option>';

$body.='</select>';
 
$body.='. Направление сортировки ';
$body.='<select name="order_style">';
	$body.='<option value="1"'.($_GET['order_style']==1 ? ' selected' : '').'>Возрастание</option>';
	$body.='<option value="2"'.($_GET['order_style']==2 ? ' selected' : '').'>Убывание</option>';
$body.='</select>.';
 
$body.=' Фильтр по ФИО сотрудника: ';
$body.='<input type="text" name="sotrudnic_fio" 
value="'.$_GET['sotrudnic_fio'].'">.';
 
$body.=' <input type="submit" value="Применить">';
$body.='</form>';
 
// Формирование таблицы со сводным отчетом
$body.='<table class="show_table">';
// Заголовок таблицы
$body.='<tr>';
$body.='<th>ID сотрудника</th>';
$body.='<th>Фамилия</th>';
$body.='<th>Должность</th>';
$body.='<th>Название услуг</th>';
$body.='<th>Кол-во услуг</th>';
$body.='<th>Заработок</th>';
$body.='<th>Выплата без НДС</th>';
$body.='</tr>';
// Цикл по всем полям таблицы
while($line=$result->fetch_assoc())
	{
	$body.='<tr>';
	foreach ($line as $key=>$val)
		{
		$body.='<td>'.$val.'</td>';
		}
	$body.='</tr>';
	}
$body.='</table>';
?>
