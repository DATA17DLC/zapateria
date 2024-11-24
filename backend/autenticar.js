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
        window.location = "dashboard.html";  // Redirigir a otra página si el login es exitoso
    })
    .catch(function (error) {
        console.error(error.response.data);  // Si ocurre un error
        alert("Login failed: " + error.response.data.detail);
    });
});

// Hacer la solicitud POST con Axios
axios.post('http://127.0.0.1:8000/login', {
    username: username,
    password: password
})
.then(function (response) {
    const token = response.data.access_token; // Capturar el token
    console.log("Token generado:", token);  // Imprimir el token en la consola
    document.body.innerHTML += `<p>Token generado: <strong>${token}</strong></p>`; // Mostrar en el DOM
    alert("Login successful!");
    window.location = "dashboard.html";  // Redirigir si es necesario
})
.catch(function (error) {
    console.error(error.response.data);  // Si ocurre un error
    alert("Login failed: " + error.response.data.detail);
});

const token = response.data.access_token; // Capturar el token
console.log("Token generado:", token);  // Imprimir el token en la consola
document.body.innerHTML += `<p>Token generado: <strong>${token}</strong></p>`; // Mostrar en el DOM
