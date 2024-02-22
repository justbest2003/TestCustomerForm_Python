<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $firstname = $_POST["firstname"];
    $lastname = $_POST["lastname"];
    $age = $_POST["age"];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Details</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            margin-bottom: 20px;
            text-align: center;
        }
        .details {
            margin-bottom: 10px;
        }
        .details label {
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Customer Details</h1>
    <div class="details">
        <label for="firstname">First Name:</label>
        <span id="firstname"><?php echo $firstname; ?></span>
    </div>
    <div class="details">
        <label for="lastname">Last Name:</label>
        <span><?php echo $lastname; ?></span>
    </div>
    <div class="details">
        <label for="age">Age:</label>
        <span><?php echo $age; ?></span>
    </div>
</div>

</body>
</html>
<?php
} else {
    // If not submitted, redirect back to the form page or do something else
    // For example:
    header("Location: ./index.html");
    exit;
}
?>
