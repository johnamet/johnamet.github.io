<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/main.css">
    <title>B7 Project Work</title>
    <script>
        window.onload = function() {
            document.querySelector('form').addEventListener('submit', function(event) {
                event.preventDefault(); // Prevent form submission
                var passcode = document.querySelector('input[name="passcode"]').value;
                if (passcode === '4673') {
                    window.location.href = 'next_page.html'; // Redirect to another webpage
                } else {
                    alert('Incorrect passcode. Please try again.'); // Show alert for incorrect passcode
                }
            });
        };
    </script>
</head>
<body>
    <h1>Welcome</h1>
    <h2>Please Enter the Passcode to access the project work</h2>
    <form>
        <label>
            <input type="text" name="passcode" pattern="[0-9]{4}" maxlength="4" placeholder="Enter 4-digit passcode" required>
        </label>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
