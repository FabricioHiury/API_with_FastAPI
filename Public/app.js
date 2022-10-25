async function loadProducts(){
    const response = await axios.get('http://localhost:8000/products').then(response => console.log(response.data))

    const products = response.data

    const list = document.getElementById('list-products')

    products.forEach(product => {
        const item = document.createElement('li')
        item.innerText = product.name

        list.appendChild(item)
    });
    
}

function manipulateForm() {
    const form_product = document.getElementById('form-product')
    const input_name = document.getElementById('name')

    form_product.onsubmit = (event)=> {
        event.preventDefault()
        const name_product = input_name.value
        alert(`submit chamado ${name_product}`)
    }
}

function app() {
    console.log("API started")
    loadProducts()
    manipulateForm()
}

app()