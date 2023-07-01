<?php
$filename = "player.csv";

// Open the CSV file in write mode
$file = fopen($filename, "w");

if ($file) {
    // Write the header row
    fputcsv($file, array("Name", "DOB", "Percentage"));

    // Write the player data rows
    // Example data for 3 players
    $players = array(
        array("John Doe", "1990-01-01", "80%"),
        array("Jane Smith", "1995-05-10", "90%"),
        array("Michael Johnson", "1985-12-15", "75%")
    );

    foreach ($players as $player) {
        fputcsv($file, $player);
    }

    // Close the file
    fclose($file);

    // Send a success response
    echo "CSV file created successfully!";
} else {
    // Send an error response
    echo "Error creating CSV file!";
}
?>
