document.getElementById('imageForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData();
    const imageFile = document.getElementById('imageInput').files[0];
    formData.append('image', imageFile);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "Generating captions...";

    try {
        const response = await fetch('http://127.0.0.1:5000/generate_caption', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        resultDiv.innerHTML = "<h3>Generated Captions:</h3><ul>";
        data.captions.forEach(caption => {
            resultDiv.innerHTML += `<li>${caption}</li>`;
        });
        resultDiv.innerHTML += "</ul>";
    } catch (error) {
        resultDiv.innerHTML = "Failed to generate captions. Please try again.";
    }
});
