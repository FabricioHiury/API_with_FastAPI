async function loadProducts(){
    const response = await axios.get('http://localhost:8000/products').then(response => console.log(response.data))

    const products = response.data

    const list = document.getElementById('list-products')

    products.array.forEach(product => {
        const item = document.createElement('li')
        item.innerText = product.name
        item.innerText = product.price 

        list.appendChild(item)
    });
    
}
function app() {
    console.log("API started")
    loadProducts()
}

app()