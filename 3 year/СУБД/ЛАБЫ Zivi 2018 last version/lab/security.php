<?
/*
	Скрипт для идентификации и аутентификации пользователя
*/
 
// Извлекается логин и пароль из переданных данных
$user_data['login']= isset($_POST['security_login']) ? $_POST['security_login'] : (isset($_COOKIE['security_login']) ? $_COOKIE['security_login'] : '');
$user_data['password']=isset($_POST['security_password']) ? $_POST['security_password'] : (isset($_COOKIE['security_password']) ? $_COOKIE['security_password'] : '');
 
// Изначально устанавливается id пользователя=0 (пользователя нет)
$user_data['id']=0;
 
// Если заданы логин и пароль, проверяется их актуальность
if($user_data['login'] != '' && $user_data['password'] != '')
	{
	$query="SELECT * FROM `security_user` WHERE `login`='".preg_replace("/[^a-zA-Z0-9_]/","",$user_data['login'])."' AND `password`='".md5($user_data['password'])."'";
	$result=$mysqli->query($query);
 
	// Если пользователь с такими данными найден
	if ($mysqli->affected_rows>0)
		{
		$row=$result->fetch_assoc();
 
		// Данные о пользователе сохраняются в переменную
		$user_data['id']=$row['id'];
 
		// Данные о правах пользователя преобразуются в формат массива
		$user_data['rights']=unserialize($row['rights']);
		// В цикле по правам пользователя на таблицы
		for($key=1;$key<=count($tables);$key++)//each($user_data['rights'] as $key => $val)
			{//Код прав на таблицу переводится в двоичный вид, дополняется до 4 знаков, разбивается на массив
			$user_data['rights'][$key]=str_split(str_pad(decbin($user_data['rights'][$key]),2, '0', STR_PAD_LEFT));
			}
		// Если необходимо произвести выход из приложения	
		if(isset($_GET['exit']) && $_GET['exit']==1)
			{// В качестве времени жизни COOKIE-данных устанавливается просроченное значение
			$cookie_time=time() - 3600;
			header('Refresh: 0; url='.$main_directory);
			}
		// Иначе, время жизни COOKIE-данных продлевается на 24 часа
		else
			{
			$cookie_time=time() + 24 * 3600;
			}
 
		// Логин и пароль сохраняются в COOKIE пользователя
		setcookie('security_login', $user_data['login'], $cookie_time, "/", $_SERVER['HTTP_HOST']);
		setcookie('security_password', $user_data['password'], $cookie_time, "/", $_SERVER['HTTP_HOST']);
 
		// При попытке совершения любого действия над таблицами, проверяется, есть ли у пользователя право на данное действие над данной таблицей
		if
			(
			$menu_id>0
			&&	(
				!isset($user_data['rights'][$menu_id])
				|| ($tables_action=='select' && $user_data['rights'][$menu_id][0]=='0')
				|| ($tables_action=='insert' && $user_data['rights'][$menu_id][1]=='0')
				|| ($tables_action=='update' && $user_data['rights'][$menu_id][1]=='0')
				|| ($tables_action=='delete' && $user_data['rights'][$menu_id][1]=='0')
				)
			)
				{//Если прав на данное действие у пользователя нет, действие не учитывается и формируется сообщение об ошибке
				$tables_action='error';
				$msg='Ошибка доступа.';
				}
		}
	else
		{
		$msg='Неправильный логин или пароль.';
		}
	}
 
// Если пользователь не задан или не найден, формируется форма для ввода логина и пароля
if($user_data['id']==0)
	{
	$body.='<div class="security_div">';
	$body.='Войдите в систему: <br>';
	$body.='<form method="post" action="'.$main_directory.'">';
	$body.='	<table>';
	$body.='		<tr><td>Логин:</td><td><input type="text" name="security_login" value="'.$_POST['security_login'].'"></td></tr>';
	$body.='		<tr><td>Пароль:</td><td><input type="password" name="security_password"></td></tr>';
	$body.='		<tr><td colspan="2"><input type="submit" value="Войти"></td></tr>';
	$body.='	</table>';
	$body.='</form>';
	$body.='В качестве логина можно использовать только символы латиницы, цифры и символ подчеркивания.<br>';
	$body.='</div>';
	}
?>
