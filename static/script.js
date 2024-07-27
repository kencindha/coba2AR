document.querySelector('a-marker').addEventListener('markerFound', () => {
    const ingredient = 'apple';  // Ganti dengan logika untuk mengenali bahan makanan
    fetch(`http://127.0.0.1:5000/get-recipe?ingredient=${ingredient}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.log(data.error);
            } else {
                console.log(data.ingredients);
                console.log(data.steps);
                // Tampilkan data resep di UI
                alert(`Ingredients: ${data.ingredients.join(', ')}\nSteps: ${data.steps.join(', ')}`);
            }
        });
});
