let carrito = [];

function agregarAlCarrito(boton) {
    const nombre = boton.dataset.nombre;
    const precio = parseFloat(boton.dataset.precio);

    const producto = { nombre: nombre, precio: precio };
    carrito.push(producto);

    actualizarInterfazCarrito();
    mostrarAviso(`✅ ${nombre} añadido`);
    console.log("Botón clickeado");
}
function actualizarInterfazCarrito() {
    const contenedorItems = document.getElementById('items-carrito');
    const contador = document.getElementById('contador-carrito');
    const totalSuma = document.getElementById('precio-total');
    
    contenedorItems.innerHTML = "";
    let total = 0;

    carrito.forEach((item, index) => {
        total += item.precio;
        const div = document.createElement('div');
        div.classList.add('item-carrito');
        div.innerHTML = `
            <p>${item.nombre} - $${item.precio}</p>
            <button onclick="eliminarDelCarrito(${index})">❌</button>
        `;
        contenedorItems.appendChild(div);
    });

    contador.innerText = carrito.length;
    totalSuma.innerText = total.toFixed(2);
}

function eliminarDelCarrito(index) {
    carrito.splice(index, 1);
    actualizarInterfazCarrito();
}

function toggleCarrito() {
    const carritoElemento = document.getElementById('carrito-lateral');
    // Si tiene la clase se la quita, si no, se la pone
    carritoElemento.classList.toggle('carrito-visible');
}

function vaciarCarrito() {
    carrito = [];
    actualizarInterfazCarrito();
}


function enviarPedido() {
    if (carrito.length === 0) {
        alert("El carrito está vacío");
        return;
    }

    // 1. Creamos el texto del pedido
    let texto = "¡Hola! Quisiera hacer un pedido:\n\n";
    let total = 0;

    carrito.forEach((item, index) => {
        texto += `${index + 1}. ${item.nombre} - $${item.precio}\n`;
        total += item.precio;
    });

    texto += `\n*Total a pagar: $${total.toFixed(2)}*`;

    // 2. Codificamos el texto para la URL
    const mensajeCodificado = encodeURIComponent(texto);
    
    // 3. Creamos el enlace final
    const enlaceWhatsApp = `https://wa.me/${numeroWhatsApp}?text=${mensajeCodificado}`;

    // 4. Abrimos WhatsApp en una nueva pestaña
    window.open(enlaceWhatsApp, '_blank');
}
function mostrarAviso(mensaje) {
    const aviso = document.getElementById('notificacion');
    aviso.innerText = mensaje;
    
    // Mostrar
    aviso.classList.add('notificacion-visible');
    
    // Esconder después de 2 segundos
    setTimeout(() => {
        aviso.classList.remove('notificacion-visible');
    }, 2000);
}
