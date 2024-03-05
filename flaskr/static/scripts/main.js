$(document).ready(function() {
    // Add event listener for each button
    $('button').click(function() {
        // Get the form values
        var value = $(this).val();
        
        // Send the value to the server
        $.ajax({
            type: 'POST',
            url: '/_add',
            data: {value: value},
            success: function(data) {
                // Update the page with the new value
                $('#result').text(data.result);
            }
        });
    });
}
