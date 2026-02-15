document.addEventListener("DOMContentLoaded", function()
{
    const input = document.getElementById("busqueda");

    input.addEventListener("input", function()
    {
        const query = input.value;
        const params = new URLSearchParams(window.location.search);
        params.set("q", query);

        fetch(`?${params.toString()}`)
            .then(response => response.text())
            .then(html => {
                const newDoc = new DOMParser().parseFromString(html, "text/html")
                const contenedor = newDoc.querySelector("#contenedor-actividades");
                document.querySelector("#contenedor-actividades").innerHTML = contenedor.innerHTML;
            })
    })
})

// Esta parte fue hecha con IA
// This part was made by AI