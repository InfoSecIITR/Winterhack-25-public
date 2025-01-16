<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Listings</title>
    <style>

        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            box-sizing: border-box; 
        }
        h1 {
            margin: 30px ;
            color: #333;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
            gap: 30px;
            padding: 0 20px;
        }
        .hotel-card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            box-sizing: border-box;
            position: relative; 
        }
        .hotel-card img {
            width: 100%;
            height: 100%;
            max-height: 250px; 
            border-radius: 8px;
            object-fit: cover;
            position: relative;
        }
        .price {
            position: absolute;
            top: 25px;
            left: 25px;
            padding: 8px 15px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 5px;
            z-index: 10;
        }
        .hotel-card h3 {
            margin-top: 15px;
            font-size: 1.4rem;
            color: #333;
        }
        .hotel-card p {
            color: #555;
            font-size: 1rem;
            margin-top: 10px;
        }

    </style>
</head>
<body>

    <?php include 'search.php'; ?>

<h1>Hotel Listings</h1>

<div class="container">
    <?php
    $db = new PDO('sqlite:data.db'); 
    $stmt = $db->query('SELECT * FROM hotels WHERE visible = 1');
    
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo '<div class="hotel-card">';
        echo '<img src="images/' . htmlspecialchars($row['image']) . '" alt="' . htmlspecialchars($row['name']) . '">';
        echo '<span class="price">$' . htmlspecialchars($row['price']) . '</span>';  // Price overlay on the image
        echo '<h3>' . htmlspecialchars($row['name']) . '</h3>';
        echo '<p>' . htmlspecialchars($row['description']) . '</p>';
        echo '</div>';
    }
    ?>
</div>

</body>
</html>
