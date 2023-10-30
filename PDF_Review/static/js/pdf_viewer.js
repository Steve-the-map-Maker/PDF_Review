console.log('coming from js/pdf_viewer.js!!!')

document.addEventListener("DOMContentLoaded", function() {
   

    // Function to render a PDF
    async function renderPDF(url) {
        try {
            const pdf = await pdfjsLib.getDocument(url).promise;
            console.log('PDF loaded');
    
            const pageNumber = 1;
            const page = await pdf.getPage(pageNumber);
            
            console.log('Page loaded');
            
            const scale = 1.5;
            const viewport = page.getViewport({scale: scale});
    
            const canvas = document.getElementById('pdf-viewer');
            const context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;
    
            const renderContext = {
                canvasContext: context,
                viewport: viewport
            };
    
            await page.render(renderContext).promise;
            console.log('Page rendered');
        } catch (error) {
            console.error('Error in rendering PDF:', error);
        }
    }
    
    // Function to fetch and display PDFs
    async function fetchUploadedPDFs() {
        try {
            const response = await fetch('/api/documents/');
            if (!response.ok) {
                console.error('HTTP Error:', response.status);
                return;
            }
    
            const data = await response.json();
            console.log('Fetched Data:', data); // Debug line to print the fetched data
            
            if (Array.isArray(data)) {
                displayPDFList(data);
            } else {
                console.error('Data is not an array:', data);
            }
        } catch (error) {
            console.error('Error fetching PDFs:', error);
        }
    }
    
    // Function to display PDF list in a drop-down and handle change events
    function displayPDFList(data) {
        const pdfDropdown = document.getElementById('pdf-dropdown');
    
        // Clear existing options
        pdfDropdown.innerHTML = '<option value="" disabled selected>Select a PDF</option>';
    
        data.forEach((pdf) => {
            const optionItem = document.createElement('option');
            optionItem.textContent = pdf.title;
            optionItem.value = pdf.file; // `pdf.file` should be the URL of the PDF
            pdfDropdown.appendChild(optionItem);
        });
    
        // Add change event to dropdown
        pdfDropdown.addEventListener('change', function() {
            const selectedPDF = this.value;
            if (selectedPDF) {
                renderPDF(selectedPDF);
            }
        });
    }
    
    // Call the function to fetch and display PDFs
    fetchUploadedPDFs();

  });


