<?php
$con=mysqli_connect("localhost","root","","college");
$sid=$_POST['sid'];
$sql="select * from `cities` where `state_id`='$sid'";
$res=mysqli_query($con,$sql);
while ($row=mysqli_fetch_assoc($res))

{
    ?>
    <option value="<?php echo $row['id'];?>"><?php echo $row['name'];?></option>
   <?php
}
?>
