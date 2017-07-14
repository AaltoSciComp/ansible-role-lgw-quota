<?php
$gid=addslashes($_GET["gid"]);

if (is_numeric($gid)) {
  $str="sudo /root/bin/quota.lustre $gid";
  $quota=exec($str);
  echo "$quota ";
}
?>
