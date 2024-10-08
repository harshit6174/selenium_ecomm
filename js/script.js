document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('featured-products')) {
        loadFeaturedProducts();
    }

    if (document.getElementById('product-list')) {
        loadProductList();
    }

    if (document.getElementById('product-detail')) {
        loadProductDetail();
    }

    if (document.getElementById('cart-items')) {
        loadCartItems();
    }

    if (document.getElementById('checkout-form')) {
        document.getElementById('checkout-form').addEventListener('submit', handleCheckout);
    }

    if (document.getElementById('add-to-cart')) {
        document.getElementById('add-to-cart').addEventListener('click', addToCart);
    }
});

function loadFeaturedProducts() {
    
    const products = [
        { id: 1, name: 'Product 1', image: 'https://via.placeholder.com/150', price: 100 },
        { id: 2, name: 'Product 2', image: 'https://via.placeholder.com/150', price: 200 },
        { id: 3, name: 'Product 3', image: 'https://via.placeholder.com/150', price: 300 },
    ];
    displayProducts(products, 'featured-products');
}

function loadProductList() {
    
    const products = [
        { id: 1, name: 'Product 1', image: 'https://via.placeholder.com/150', price: 100 },
        { id: 2, name: 'Product 2', image: 'https://via.placeholder.com/150', price: 200 },
        { id: 3, name: 'Product 3', image: 'https://via.placeholder.com/150', price: 300 },
    ];
    displayProducts(products, 'product-list');
}

function loadProductDetail() {
   
    const product = { id: 1, name: 'Product 1', image: 'https://via.placeholder.com/150', price: 100, description: 'This is a great product.' };
    displayProductDetail(product);
}

function addToCart() {
   
    const product = { id: 1, name: 'Product 1', price: 100 };
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Product added to cart!');
}

function loadCartItems() {
    
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    displayCartItems(cart);
}

function handleCheckout(event) {
    event.preventDefault();
    alert('Order placed successfully!');
    localStorage.removeItem('cart');
}

function displayProducts(products, elementId) {
    const container = document.getElementById(elementId);
    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
            <a href="product-detail.html?id=${product.id}">View Details</a>
        `;
        container.appendChild(productElement);
    });
}

function displayProductDetail(product) {
    const container = document.getElementById('product-detail');
    container.innerHTML = `
        <img src="${product.image}" alt="${product.name}">
        <h3>${product.name}</h3>
        <p>$${product.price}</p>
        <p>${product.description}</p>
    `;
}

function displayCartItems(cart) {
    const container = document.getElementById('cart-items');
    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'cart-item';
        itemElement.innerHTML = `
            <h3>${item.name}</h3>
            <p>$${item.price}</p>
        `;
        container.appendChild(itemElement);
    });
}
