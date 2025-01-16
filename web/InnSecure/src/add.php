<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $price = $_POST['price'];
    $description = $_POST['description'];
    $visible = isset($_POST['visible']) ? 1 : 0;

    $targetDir = "images/";
    $targetFile = $targetDir . basename($_FILES["image"]["name"]);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

    if (isset($_POST["submit"])) {
        $check = getimagesize($_FILES["image"]["tmp_name"]);
        if ($check !== false) {
            $uploadOk = 1;
        } else {
            echo "❌ File is not an image.";
            $uploadOk = 0;
        }
    }

    if ($_FILES["image"]["size"] > 2000000) {
        echo "❌ Sorry, your file is too large.";
        $uploadOk = 0;
    }

    if (!in_array($imageFileType, ['jpg', 'jpeg', 'png', 'gif'])) {
        echo "❌ Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
        $uploadOk = 0;
    }

    if ($uploadOk && move_uploaded_file($_FILES["image"]["tmp_name"], $targetFile)) {
        $image = basename($_FILES["image"]["name"]);

        $db = new PDO('sqlite:data.db');
        $stmt = $db->prepare('INSERT INTO hotels (name, price, description, image, visible) VALUES (?, ?, ?, ?, ?)');
        $stmt->execute([$name, $price, $description, $image, $visible]);

        header('Location: index.php');
        exit();
    } else {
        echo "❌ Sorry, there was an error uploading your file.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Hotel Listing</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8fafc;
        }

        nav {
            background-color: #1e293b;
            color: white;
            padding: 10px 0;
            text-align: center;
        }

        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-size: 1rem;
            padding: 8px 15px;
            border-radius: 5px;
            transition: background 0.3s;
        }

        nav a:hover {
            background-color: #334155;
        }

        .form-container {
            max-width: 600px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .form-container h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        .form-container label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #555;
        }

        .form-container input,
        .form-container textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
            font-size: 1rem;
        }

        .form-container input[type="file"] {
            padding: 5px;
        }

        .form-container input[type="checkbox"] {
            width: auto;
            margin-right: 10px;
        }

        .form-container button {
            width: 100%;
            background-color: #333;
            color: white;
            padding: 12px;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        }

        .form-container button:hover {
            background-color: #360;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            padding: 10px;
            background-color: #1e293b;
            color: white;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

<?php include 'search.php'; ?>

<div class="form-container">
    <h1>Add a New Hotel</h1>
    <form action="add.php" method="POST" enctype="multipart/form-data">
        <label for="name">Hotel Name</label>
        <input type="text" id="name" name="name" placeholder="Enter hotel name" required>

        <label for="price">Price ($)</label>
        <input type="number" id="price" name="price" placeholder="Enter price per night" required>

        <label for="description">Description</label>
        <textarea id="description" name="description" rows="4" placeholder="Enter a brief description" required></textarea>

        <label for="image">Upload Image</label>
        <input type="file" id="image" name="image" accept="image/*" required>

        <label>
            <input type="checkbox" id="visible" name="visible"> Make this listing visible
        </label>

        <button type="submit">Add Hotel</button>
    </form>
</div>

</body>
</html>
