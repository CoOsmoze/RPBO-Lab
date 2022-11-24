<?php
session_start();
/*Проверка соответствия проверочного кода */
var_dump($_POST['captcha']);
var_dump($_SESSION['captcha']);
if(isset($_POST['captcha']) && ($_POST['captcha']) !== '' && $_SESSION['captcha'] == $_POST['captcha']){
    /*Какой то код*/
   $_SESSION['success'] = 'Форма успешно отправлена';
   $_SESSION['timeout'] = 0;
}
else{
    $_SESSION['error'] = 'Неверно введен проверочный код';
}
header('Location: index.php');
exit();
?>