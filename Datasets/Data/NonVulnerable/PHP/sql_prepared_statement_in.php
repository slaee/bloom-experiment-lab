<?php
  $username = $_GET['username'];
  $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
  $stmt->bind_param("s", $username);
  $stmt->execute();
  $result = $stmt->get_result();
  while ($row = $result->fetch_assoc()) {
    echo "User ID: " . $row["user_id"] . ", Name: " . $row["name"] . "<br>";
  }
  $stmt->close();
?>
