<?php

function valid($fieldName)
{
   if (!isset($_POST[$fieldName])
       return false;

   $forbiddenSymbols = array('\'', '"', '--');

   foreach ($forbiddenSymbols as &$symbol)
	   if (strpos($_POST[$fieldName] , $symbol)) return false;

   return true;
}

function blocked($username)
{
   $attemptsBeforeBlocking = 3;
   $sTimeOut = 60;

   $sample   = $mysqli->query('SELECT loginTime, failsCount FROM users WHERE user =' . $username);  
   $userData = $sample->fetch_assoc();  
 
   if ($userData['failsCount'] >= $attemptsBeforeBlocking) 
      if (time() - strtotime($userData['loginTime']) < $sTimeOut)
          return true

   return false;
}

function succeed()
{
    $avatar = $row['avatar'];  

    $html .= "<p>Welcome to the password protected area {$user}</p>";  
    $html .= "<img src=\"{$avatar}\" />";  

    $mysqli->query('UPDATE users SET failsCount = 0, loginTime = ' . time() . ' WHERE user = ' . $username);  
}

function failed()
{
   $html .= "<pre><br />Username and/or password incorrect.</pre>";

   $mysqli->query('UPDATE users SET failsCount = failsCount + 1 WHERE user = ' . $username);  
}

//------------------------main---------------------------
if (!valid('username') || !valid('password') || !isset($_POST['Login']))      //CWE-89 Проверка отсутствия SQL инъекций
    return;                                               

$user     = $_POST['username'];                           //CWE-598 Получить данные методом  POST (конфиденциальность)
$password = crypt($_POST['password'], $someSalt);         //CWE-327 слабый криптоалгоритм (поменять на SHA256)), CWE-759 (Односторонний хеш без соли (сделать хеш с солью)

$sample  = $mysqli->query('SELECT * FROM users WHERE user = ' . $user . ' AND password = ' . $password;  
$blocked = blocked($username); //CWE-307 Неправильное ограничение чрезмерных попыток аутентификации (добавить количество попыток с ограничением по времени)

if ($sample->num_rows() == 1 && !$blocked)
    succeed();

else if (!$blocked)
    failed();

?>