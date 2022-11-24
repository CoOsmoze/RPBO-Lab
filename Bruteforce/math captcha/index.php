<?php 
session_start();
$_SESSION['timeout'];
$min  = 1;
$max  = 300;
$num1 = rand( $min, $max );
$num2 = rand( $min, $max );
$sum  = $num1 + $num2;
function message(){ //Функция вывода сообщений о результате запроса
    if(isset($_SESSION['success'])){
        echo '<p style="color:green;">'.$_SESSION['success'].'</p>';
        unset($_SESSION['success']);
    }
    if(isset($_SESSION['error'])){
        echo '<p style="color:red;">'.$_SESSION['error'].'</p>';
        
    }
}
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <link rel="stylesheet" href="main.css">
        <title>
            Капча
        </title>
    </head>
    <body>
    <div  style="text-align:center;">
        <?php  message(); //Вызов функции вывода сообщений?>
    </div>

    <div class = 'vulnerable_code_area'>
        <h2>Login</h2>
        <form action="#" method="POST">
            Password:<br>
            <input type="password" autocomplete="off" name="password"><br>
            <br>
            <input type="submit" data-res="<?php echo $sum; ?>" value="Login" name="Login">
        </form>
    </div>


    <?php
    // Get password
    if( $_POST[ 'password' ] !="" ) {
        $pass = $_POST[ 'password' ];
        $truepass = 'password';

        if( $truepass == $pass ) {
            // Login successful
            echo  "<p>Welcome to the password protected area admin </p>";
            $_SESSION['timeout'] = 0;
        }
        else {
            // Login failed
            $_SESSION['timeout'] +=1;
            echo "Invalid password";
        }
    }
    if ( $_SESSION['timeout'] >2 || isset($_SESSION['error'])) 
    {
        unset($_SESSION['error']);
        $_SESSION['captcha']= $sum;
        ?>
        <form action="check.php" method="POST">
            Enter captcha code:<br>
            <?php echo $num1 . '+' . $num2; ?>
            <input type="text" autocomplete="off" class="quiz-control" id="quiz" name="captcha">
            <br>
            <input type="submit"  value="Send" name="pas">
        </form>

            <script>
                const submitButton = document.querySelector('[type="submit"]');
                const inputText = document.querySelector('[type="password"]');
                submitButton.setAttribute("disabled", "");
                inputText.setAttribute("disabled", "");
                const quizInput = document.querySelector(".quiz-control");
                
            </script>
        <?php
    }
    ?>  
    </body>
</html>