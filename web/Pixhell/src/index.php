<?php
$allowed_extensions = ['png', 'jpg', 'jpeg', 'gif'];

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];
    $upload_dir = 'uploads/';

    $file_extension = strtolower(explode('.', $file['name'])[1]);
    if (in_array($file_extension, $allowed_extensions)) {

        $new_filename = $file['name'];
        $upload_path = $upload_dir . $new_filename;

        if (move_uploaded_file($file['tmp_name'], $upload_path)) {
            $uploaded_image_url = $upload_path;
            echo "<div class='result success'>
                    <h3>Image uploaded successfully!</h3>
                    <p><a href='$uploaded_image_url' target='_blank'>Click here to view the image</a></p>
                  </div>";
        } else {
            echo "<div class='result error'>
                    <p>Error uploading the file. Please try again.</p>
                  </div>";
        }
    } else {
        echo "<div class='result error'>
                <p>Invalid file type! Only .png, .jpg, .jpeg, .gif images are allowed.</p>
              </div>";
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Store</title>
    <style>
        body,
        h1,
        p,
        form,
        button {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f4f7fc;
            color: #333;
            font-size: 16px;
            line-height: 1.5;
            padding: 50px 10px;
        }

        h1 {
            text-align: center;
            color: #2d87f0;
            font-size: 42px;
            margin-bottom: 20px;
        }

        p {
            text-align: center;
            font-size: 18px;
            margin-bottom: 40px;
            color: #555;
        }

        .form-container {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 500px;
            margin: 0 auto;
            transition: box-shadow 0.3s ease-in-out;
        }

        .form-container:hover {
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
        }

        .form-container form {
            display: flex;
            flex-direction: column;
        }

        .form-container label {
            font-size: 18px;
            margin-bottom: 10px;
            color: #555;
        }

        .form-container input[type="file"] {
            display: block;
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }

        .form-container input[type="file"]:focus {
            border-color: #2d87f0;
        }

        .form-container button {
            background-color: #2d87f0;
            color: #fff;
            padding: 15px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s ease;
        }

        .form-container button:hover {
            background-color: #1a64d2;
        }

        .result {
            text-align: center;
            margin-top: 30px;
            padding: 25px;
            border-radius: 10px;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }

        .result.success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .result.error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        .result a {
            color: #2d87f0;
            text-decoration: none;
        }

        .result a:hover {
            text-decoration: underline;
        }

        @media (max-width: 600px) {
            .form-container {
                padding: 30px;
                max-width: 90%;
            }

            h1 {
                font-size: 32px;
            }

            .form-container button {
                font-size: 16px;
                padding: 12px 20px;
            }
        }
    </style>
</head>

<body>
    <h1>Welcome to the Image Store!</h1>
    <p>Upload your images and share them with the world.</p>

    <div class="form-container">
        <form action="index.php" method="post" enctype="multipart/form-data">
            <label for="file">Choose an image to upload:</label>
            <input type="file" name="file" id="file" accept=".png, .jpg, .jpeg, .gif" required>
            <button type="submit">Upload Image</button>
        </form>
    </div>

</body>

</html>