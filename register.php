<?php

$NAME = $_POST['NAME'];
$AGE = $_POST['AGE'];	
$DEPARTMENT = $_POST['DEPARTMENT'];
$SPORTSNAME = $_POST['SPORTSNAME'];
$MOBILENO = $_POST['MOBILENO'];


if (!empty($NAME) || !empty($AGE) || !empty($DEPARTMENT) || !empty($SPORTSNAME) || !empty($MOBILENO))
{

$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "sport";



// Create connection
$conn = new mysqli ($host, $dbusername, $dbpassword, $dbname); 

if (mysqli_connect_error()){
  die('Connect Error ('. mysqli_connect_errno() .') '
    . mysqli_connect_error());
}
else{
  $SELECT = "SELECT MOBILENO From register Where MOBILENO = ? Limit 1";
  $INSERT = "INSERT Into register (NAME,AGE ,DEPARTMENT,SPORTSNAME,MOBILENO )values(?,?,?,?,?)";

//Prepare statement
     $stmt = $conn->prepare($SELECT);
     $stmt->bind_param("i", $MOBILENO);
     $stmt->execute();
     $stmt->bind_result($MOBILENO);
     $stmt->store_result();
     $rnum = $stmt->num_rows;

     //checking username
      if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->bind_param("ssssi", $NAME,$AGE,$DEPARTMENT,$SPORTSNAME,$MOBILENO);
      $stmt->execute();
      echo "New record inserted sucessfully";
     } else {
      echo "Someone already register using this MOBILE NO";
     }
     $stmt->close();
     $conn->close();
    }
} else {
 echo "All field are required";
 die();
}
?>