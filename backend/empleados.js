window.onload = function () {
    // Realizar la solicitud para obtener los empleados
    axios.get('http://127.0.0.1:8000/empleados')
        .then(function (response) {
            console.log(response)
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
                    <td>${empleado.telefono}</td>
                    <td>
                        <button onclick="editarFila(this)">Editar</button>
                        <button class="btn-eliminar" onclick="confirmarEliminar(${empleado.id})">Eliminar</button>
                    </td>`;
                tabla.appendChild(row);
            });
        })
        .catch(function (error) {
            console.error('Error al obtener empleados:', error);
        });
}

// Función para iniciar sesión
async function login(username, password) {
    const response = await fetch("http://127.0.0.1:8000/login_json", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    if (response.ok) {
        const data = await response.json();
        return data.access_token; // Retorna el token
    } else {
        const error = await response.json();
        throw new Error(error.detail);
    }
}


function buscar() {
    const input = document.querySelector('.search-input');
    const filter = input.value.toLowerCase();
    const tabla = document.getElementById('tablaEmpleados');
    const filas = tabla.getElementsByTagName('tr');

    for (let i = 1; i < filas.length; i++) {
        let mostrarFila = false;
        const celdas = filas[i].getElementsByTagName('td');

        for (let j = 0; j < celdas.length - 1; j++) {
            const textoCelda = celdas[j].textContent || celdas[j].innerText;
            if (textoCelda.toLowerCase().indexOf(filter) > -1) {
                mostrarFila = true;
                break;
            }
        }

        filas[i].style.display = mostrarFila ? '' : 'none';
    }
}

function buscarEmpleado() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toLowerCase();
    const tabla = document.getElementById('tabla');
    const filas = tabla.getElementsByTagName('tr');

    // Recorre todas las filas de la tabla
    for (let i = 1; i < filas.length; i++) { // Empieza en 1 para saltar el encabezado
        let mostrarFila = false;
        const celdas = filas[i].getElementsByTagName('td');

        // Revisa todas las celdas de la fila
        for (let j = 0; j < celdas.length; j++) {
            const textoCelda = celdas[j].textContent || celdas[j].innerText;
            if (textoCelda.toLowerCase().indexOf(filter) > -1) {
                mostrarFila = true;
                break;
            }
        }

        // Muestra u oculta la fila según el resultado
        filas[i].style.display = mostrarFila ? '' : 'none';
    }
}

// Evento de búsqueda
document.getElementById('searchInput').addEventListener('keyup', buscarEmpleado);


        // Funciones del modal
        function mostrarModalAgregar() {
            document.getElementById('modalTitle').textContent = 'Agregar Empleado';
            document.getElementById('empleadoForm').reset();
            document.getElementById('empleadoModal').style.display = 'block';
        }

        function editarFila(boton) {
            const fila = boton.closest('tr');
            const celdas = fila.cells;
            const modal = document.getElementById('modalEdicion');
            
            document.getElementById('editId').value = celdas[0].textContent;
            document.getElementById('editNombre').value = celdas[1].textContent;
            document.getElementById('editApellido').value = celdas[2].textContent;
            document.getElementById('editCorreo').value = celdas[3].textContent;
            document.getElementById('editTelefono').value = celdas[4].textContent;
            
            modal.style.display = 'block';
        }

        function guardarCambios() {
            const id = document.getElementById('editId').value;
            const nombre = document.getElementById('editNombre').value;
            const apellido = document.getElementById('editApellido').value;
            const correo = document.getElementById('editCorreo').value;
            const telefono = document.getElementById('editTelefono').value;
        
            // Llamada al backend para actualizar
            axios.put(`http://127.0.0.1:8000/empleados/${id}`, {
                nombre: nombre,
                apellido: apellido,
                email: correo,
                telefono: telefono
            })
            .then(response => {
                // Actualizar la fila en la tabla si el backend respondió correctamente
                const fila = document.querySelector(`tr[data-id="${id}"]`);
                if (fila) {
                    fila.cells[1].textContent = nombre;
                    fila.cells[2].textContent = apellido;
                    fila.cells[3].textContent = correo;
                    fila.cells[4].textContent = telefono;
                }
                cerrarModal();
            })
            .catch(error => {
                console.error("Error al guardar cambios:", error);
                alert("Ocurrió un error al guardar los cambios.");
            });
        }

        function AgregarEmpleado() {
            const nombre = document.getElementById('nombre').value;
            const apellido = document.getElementById('apellido').value;
            const correo = document.getElementById('correo').value;
            const telefono = document.getElementById('telefono').value;
        
            // Llamada al backend para actualizar
            axios.post(`http://127.0.0.1:8000/empleados/`, {
                nombre: nombre,
                apellido: apellido,
                email: correo,
                telefono: telefono
            })
            .then(response => {
                // Actualizar la fila en la tabla si el backend respondió correctamente
                const fila = document.querySelector(`tr[data-id=""]`);
                if (fila) {
                    fila.cells[1].textContent = nombre;
                    fila.cells[2].textContent = apellido;
                    fila.cells[3].textContent = correo;
                    fila.cells[4].textContent = telefono;
                }
                cerrarModal();
            })
            .catch(error => {
                console.error("Error al guardar cambios:", error);
                alert("Ocurrió un error al guardar los cambios.");
            });
        }



        function cerrarModal() {
            document.getElementById('modalEdicion').style.display = 'none';
        }
        function cerrarModal2() {
            document.getElementById('empleadoModal').style.display = 'none';
        }


// Manejar envío del formulario para agregar o actualizar
document.getElementById('empleadoForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Capturar datos del formulario
    const empleadoData = {
        nombre: document.getElementById('nombre').value,
        apellido: document.getElementById('apellido').value,
        email: document.getElementById('correo').value,
        telefono: document.getElementById('telefono').value
    };

    const id = document.getElementById('empleadoId').value;

    try {
        if (id) {
            // Actualizar empleado si existe un ID
            const response = await axios.put(`http://127.0.0.1:8000/empleados/${id}`, empleadoData);

            // Actualizar fila en la tabla
            const fila = document.querySelector(`tr[data-id="${id}"]`);
            if (fila) {
                fila.cells[1].textContent = empleadoData.nombre;
                fila.cells[2].textContent = empleadoData.apellido;
                fila.cells[3].textContent = empleadoData.email;
                fila.cells[4].textContent = empleadoData.telefono;
            }
        } else {
            // Agregar empleado si no hay ID
            const response = await axios.post('http://127.0.0.1:8000/empleados', empleadoData);

            // Agregar nueva fila a la tabla
            const empleado = response.data;
            const tabla = document.getElementById('tablaEmpleados');
            const nuevaFila = tabla.insertRow();

            nuevaFila.setAttribute('data-id', empleado.id);
            nuevaFila.innerHTML = `
                <td>${empleado.id}</td>
                <td>${empleado.nombre}</td>
                <td>${empleado.apellido}</td>
                <td>${empleado.email}</td>
                <td>${empleado.telefono}</td>
                <td>
                    <button onclick="editarFila(this)">Editar</button>
                    <button onclick="eliminarEmpleado(${empleado.id})">Eliminar</button>
                </td>
            `;
        }

        // Limpiar formulario y cerrar modal
        cerrarModal();
    } catch (error) {
        console.error("Error al procesar el formulario:", error);
        alert("Ocurrió un error al procesar el formulario.");
    }
});

function confirmarEliminar(id) {
    // Muestra el modal de confirmación
    document.getElementById('modalConfirmDelete').style.display = 'block';

    // Asigna el ID del empleado al campo oculto
    document.getElementById('deleteId').value = id;

}

function eliminarEmpleado() {
    
    const id = document.getElementById('deleteId').value;
    
    // Llamada al backend para eliminar el empleado
    axios.delete(`http://127.0.0.1:8000/empleados/${id}`)
        .then(() => {
            // Eliminar la fila de la tabla correspondiente al empleado
            const fila = document.querySelector(`tr[data-id="${id}"]`);
            if (fila) {
                fila.remove();
            }

            // Cerrar el modal de confirmación
            cerrarModalConfirm();
        })
        .catch(error => {
            console.error("Error al eliminar el empleado:", error);
            alert("Ocurrió un error al intentar eliminar el empleado.");
        });
}

function cerrarModal() {
    // Cierra el modal de edición
    document.getElementById('modalEdicion').style.display = 'none';
}

function cerrarModalConfirm() {
    // Cierra el modal de confirmación
    document.getElementById('modalConfirmDelete').style.display = 'none';
}
