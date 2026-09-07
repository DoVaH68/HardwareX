const registerButton = document.getElementById("register");
const loginButton = document.getElementById("login");
const container = document.getElementById("container");


// ===============================
// CAMBIAR ENTRE LOGIN Y REGISTRO
// ===============================

registerButton.addEventListener("click", () => {
    container.classList.add("right-panel-active");
});

loginButton.addEventListener("click", () => {
    container.classList.remove("right-panel-active");
});


// ===============================
// LOGIN
// ===============================

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const formData = new FormData(loginForm);

    try {

        const response = await fetch("/login/", {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        });

        const data = await response.json();

        if (response.ok) {

            console.log("Inicio de sesión exitoso:", data);

            // Guardamos los datos del usuario
            sessionStorage.setItem(
                "usuario",
                JSON.stringify(data.usuario)
            );

            // Redirigir al inicio
            window.location.href = "/";

        } else {

            alert(
                data.detail ||
                data.message ||
                "Correo o contraseña incorrectos."
            );
        }

    } catch (error) {

        console.error("Error al iniciar sesión:", error);

        alert("No se pudo conectar con el servidor.");
    }

});