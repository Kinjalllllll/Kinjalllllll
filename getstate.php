<?php
$con = mysqli_connect("localhost","root","","college");
$cid = $_POST['cid']; 
$sql = "select * from `states` where `country_id`'='$cid'";
$res = mysqli_query($con,$sql);
while($row=mysqli_fetch_assoc($res))

{
    ?>
    <option value="<?php echo $row['id'];?>"><?php echo $row['name'];?></option>
    <?php
   
}
?>

