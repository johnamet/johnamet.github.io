window.onload = function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission
        const passcode = document.querySelector('input[name="passcode"]').value;
        if (passcode === '4673') {
            window.location.href = 'project_page.html'; // Redirect to another webpage
        } else {
            alert('Incorrect passcode. Please try again.'); // Show alert for incorrect passcode
        }
    });
};
