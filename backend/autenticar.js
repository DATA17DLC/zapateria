// login.js

// Capturar el formulario de login
const form = document.getElementById('loginForm');

// Añadir el evento de submit
form.addEventListener('submit', function (e) {
    e.preventDefault();  // Evitar recarga de la página

    // Obtener los valores de los campos del formulario
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Hacer la solicitud POST con Axios
    axios.post('http://127.0.0.1:8000/login_users', {
        email: email,
        password: password
    })
    .then(function (response) {
        console.log(response.data);  // Si el login es exitoso
        alert("Login successful!");
        // Redirigir a otra página si es necesario
        // window.location = "dashboard.html"; 
    })
    .catch(function (error) {
        console.error(error.response.data);  // Si ocurre un error
        alert("Login failed: " + error.response.data.detail);
    });
<<<<<<< HEAD
    // abrir ventana dashboard si los datos son correctos
=======
>>>>>>> 6e755babc9a6c84e51be285bf6a1a6b78870dbea
    window.location = "dashboard.html";
});
