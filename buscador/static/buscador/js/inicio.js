document.addEventListener("DOMContentLoaded", function()
{
    const input = document.getElementById("busqueda");

    input.addEventListener("input", function()
    {
        const query = input.value;
        const params = new URLSearchParams(window.location.search);
        params.set("q", query);

        params.set("q", query);

        fetch(`?${params.toString()}`)
            .then(response => response.text())
            .then(html => {
                const newDoc = new DOMParser().parseFromString(html, "text/html")
                const ul = newDoc.querySelector("#actividades ul");
                const actividades = document.querySelector("#actividades");

                if(ul)
                {
                    actividades.innerHTML = `<ul>${ul.innerHTML}</ul>`;
                }
                else
                {
                    actividades.innerHTML = `<ul>${ul.innerHTML}</ul>`;
                }
            })
            .catch(err => console.error(err))
    })
})

// Esta parte fue hecha con IA
// This part was made by AI