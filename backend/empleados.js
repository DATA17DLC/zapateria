window.onload = function () {
    // Realizar la solicitud para obtener los empleados
    axios.get('http://127.0.0.1:8000/empleados')
        .then(function (response) {
            // Obtener el elemento de la tabla por ID
            const tabla = document.getElementById('tabla');
            
            // Limpiar el contenido previo (en caso de que haya)
            tabla.innerHTML = '';

            // Iterar sobre los empleados y agregarlos a la tabla
            response.data.forEach(empleado => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${empleado.id}</td>
                    <td>${empleado.nombre}</td>
                    <td>${empleado.apellido}</td>
                    <td>${empleado.email}</td>
                    <td>${empleado.telefono}</td>`;
                tabla.appendChild(row);
            });
        })
        .catch(function (error) {
            console.error('Error al obtener empleados:', error);
        });
}
