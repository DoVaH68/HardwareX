const registerButton = document.getElementById("register");
const loginButton = document.getElementById("login");
const container = document.getElementById("container");

// ===============================
// CAMBIAR ENTRE LOGIN Y REGISTRO
// ===============================

if (registerButton && container) {
    registerButton.addEventListener("click", () => {
        container.classList.add("right-panel-active");
    });
}

if (loginButton && container) {
    loginButton.addEventListener("click", () => {
        container.classList.remove("right-panel-active");
    });
}


// ===============================
// LOGIN
// ===============================

const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {

        event.preventDefault();

        const formData = new FormData(loginForm);

        try {

            const response = await fetch(
                loginForm.action,
                {
                    method: "POST",
                    body: formData,
                    credentials: "same-origin",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest"
                    }
                }
            );

            const data = await response.json();

            if (!response.ok) {
                alert(
                    data.detail ||
                    "Correo o contraseña incorrectos."
                );
                return;
            }

            sessionStorage.setItem(
                "usuario",
                JSON.stringify(data.usuario)
            );

            window.location.href =
                data.redirect_url || "/";

        } catch (error) {

            console.error(
                "Error al iniciar sesión:",
                error
            );

            alert(
                "No se pudo conectar con el servidor."
            );
        }
    });
}


// ===============================
// REGISTRO
// ===============================

const registerForm =
    document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener(
        "submit",
        async (event) => {

            event.preventDefault();

            const formData =
                new FormData(registerForm);

            try {

                const response = await fetch(
                    registerForm.action,
                    {
                        method: "POST",
                        body: formData,
                        credentials: "same-origin",
                        headers: {
                            "X-Requested-With":
                                "XMLHttpRequest"
                        }
                    }
                );

                const data =
                    await response.json();

                if (!response.ok) {

                    alert(
                        data.detail ||
                        "No se pudo realizar el registro."
                    );

                    return;
                }

                alert(
                    data.message ||
                    "Registro exitoso."
                );

                registerForm.reset();

                if (container) {
                    container.classList.remove(
                        "right-panel-active"
                    );
                }

            } catch (error) {

                console.error(
                    "Error al registrar:",
                    error
                );

                alert(
                    "No se pudo conectar con el servidor."
                );
            }
        }
    );
}