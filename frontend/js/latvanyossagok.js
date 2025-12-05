const serverURL = "http://127.0.0.1:8000"

function allLatvanyossagok(){
    fetch(`${serverURL}/api/latvanyossagok`).
    then(res=>res.json()).
    then(res=>{
        res.forEach(element => 
            {
                document.querySelector("#latvanyossagokGrid").innerHTML +=
                `
                <div class="col-12 col-md-6 col-lg-3">
                    <div class="card overflow-scroll" style="width: 18rem;">
                        <img class="card-img-top" src="${element.URL}" alt="${element.Nev}" title="${element.Nev}">
                        <div class="card-body">
                            <h5 class="card-title">${element.Nev}</h5>
                            <p class="card-text">${element.RLeiras}</p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">${element.VId.OId.Nev}: ${element.VId.Nev}</li>
                            <li class="list-group-item">${element.AtlagErtekeles}</li>
                            <li class="list-group-item">Nyitvatartás: ${element.Nyitvatartas}</li>
                        </ul>
                        <div class="card-body">
                            <a href="${element.URL}" target="_blank" class="card-link">Kép megnyitása</a><br />
                            <a href="" onclick="javascript:deleteLatvanyossag(${element.id})" class="btn btn-danger">Törlés</a>
                        </div>
                        </div>
                </div>
                `;
            
            })
    });
}

function deleteLatvanyossag(id)
{
    fetch(`http://127.0.0.1:8000/api/torles/${id}`,
        {
            method:"DELETE",
            headers:
            {
                'Content-Type':'application/json'
            }
        }).then(res=>
        {
            if (res.ok)
            {
                console.log("Látványosság törölve.");
                window.location.reload();
            }
            else
            {
                console.log("A látványosság törlése nem sikerült.")
            }
        }).catch(error=>{console.log(error)});
}

allLatvanyossagok();



/**/
/*
function uploadImage()
{
    let data = new FormData();
    data.append("title",document.querySelector("#imageTitle").value);
    data.append("petImage", document.querySelector("#imageFile").files[0]);
    fetch( `${serverURL}/api/images`,
        {
            method: 'POST',
            headers: {'Accept':'application/JSON'},
            body: data
        }
    ).then(alert("OK"))
}

function selectPet(){
    fetch(`${serverURL}/api/random/Cat`).
    then(res=>res.json()).
    then(res=>
    {
        document.querySelector("#petoftheday").innerHTML = `
        <img src="${serverURL}${res.petImage}" />`;
    }
    )
}
*/