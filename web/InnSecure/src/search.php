<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Hotel Listings</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
        }

        .navbar {
            background-color: #333;
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        .navbar a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: bold;

        }

        h1 {
            margin-bottom: 20px;
        }

        .search-form {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        .search-form input {
            padding: 10px;
            width: 250px;
            border: 2px solid #ddd;
            border-radius: 5px;
        }

        .search-form button {
            padding: 10px 20px;
            border: none;
            background-color: #333;
            color: white;
            border-radius: 5px;
            margin-left: 10px;
            cursor: pointer;
        }


        .result {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        .hotel-card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
            padding: 15px;
            transition: transform 0.2s ease-in-out;
        }

        .hotel-card img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .hotel-card h3 {
            margin: 10px 0;
            font-size: 1.2em;
            color: #333;
        }

        .hotel-card p {
            color: #666;
            font-size: 0.9em;
        }

        .no-results {
            text-align: center;
            font-size: 1.2em;
            color: #555;
            margin-top: 20px;
        }
    </style>
</head>

<body>

    <div class="navbar">
        <a href="index.php">Home</a>
        <a href="add.php">Add Listing</a>
    </div>
    <div class="search-form">
        <form action="search.php" method="POST">
            <input type="text" name="search_term" placeholder="Enter hotel name" required>
            <button type="submit">Search</button>
        </form>
    </div>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $search_term = $_POST['search_term'];

        $db = new PDO('sqlite:data.db');
        $query = "SELECT * FROM hotels WHERE name LIKE '%$search_term%' and visible = 1";
        try {
            $stmt = $db->query($query);
        } catch (PDOException $e) {
            echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
            exit;
        }

        echo '<div class="result">';
        $found = false;
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $found = true;
            echo '<div class="hotel-card">';
            echo '<img src="images/' . htmlspecialchars($row['image']) . '" alt="' . htmlspecialchars($row['name']) . '">';
            echo '<h3>' . htmlspecialchars($row['name']) . '</h3>';
            echo '<p>' . htmlspecialchars($row['description']) . '</p>';
            echo '</div>';
        }
        if (!$found) {
            echo '<div class="no-results">No hotels found matching your search.</div>';
        }
        echo '</div>';
    }
    ?>

</body>

</html>