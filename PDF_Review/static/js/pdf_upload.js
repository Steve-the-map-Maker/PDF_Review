console.log('coming from pdf_upload.js!!!!!')

// Function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Get the form elements
const pdfUploadForm = document.getElementById('pdf-upload-form');
const pdfTitle = document.getElementById('pdf-title');
const pdfFile = document.getElementById('pdf-file');
const pdfOwner = document.getElementById('pdf-owner');  // New line

// Listen for form submission
pdfUploadForm.addEventListener('submit', function(event) {
    event.preventDefault();

    // Create FormData object and append the title, file, and owner
    const formData = new FormData();
    formData.append('title', pdfTitle.value);
    formData.append('file', pdfFile.files[0]);
    formData.append('owner', pdfOwner.value);  // New line

    // Make the API call to upload the PDF
    fetch('/api/documents/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle success - maybe refresh the list of documents or redirect the user
        console.log('Success:', data);
    })
    .catch((error) => {
        // Handle failure
        console.error('Error:', error);
    });
});
