window.onload = function () {
    // Realizar la solicitud para obtener los productos
    axios.get('http://127.0.0.1:8000/productos')
        .then(function (response) {
            // Obtener el elemento de la tabla por ID
            const tabla = document.getElementById('tabla');
            
            // Limpiar el contenido previo (en caso de que haya)
            tabla.innerHTML = '';

            // Iterar sobre los productos y agregarlos a la tabla
            response.data.forEach(producto => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${producto.id}</td>
                    <td>${producto.nombre}</td>
                    <td>${producto.descripcion}</td>
                    <td>${producto.precio}</td>
                    <td>${producto.cantidad}</td> 
                `;
                tabla.appendChild(row); // Asegúrate de que esto esté fuera del template literal
            });
        })
        .catch(function (error) {
            console.error('Error al obtener productos:', error);
        });
}

