<?php
include "config.php";
$sql = "select * from `employoee` where `department`='sales'";
$res =mysqli_query($con,$sql);


?>
<table class="table table-bordered">
    <tr>
        <th>#</th>
        <th>name</th>
        <th>joining date</th>
        <th>risiginin date</th>
        <th>leaves</th>
        <th>salary</th>
        <th>department</th>
</tr>
<?php
    while($row = mysqli_fetch_array($res))
    {
        $i++;
        ?>
        <tr>
            <td><?php echo $i; ?></td>
            <td><?
    }
