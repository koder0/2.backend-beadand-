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
                        <a href="${element.URL}" target="_blank" class="card-link"><img class="card-img-top" src="${element.URL}" alt="${element.Nev}" title="${element.Nev}"></a>
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
                            <input type="button" onclick="javascript:deleteLatvanyossag(${element.id})" class="btn btn-danger" value="Törlés">
                        </div>
                        </div>
                </div>
                `;
            
            })
    });
}

function allLatvanyossagokTabla(){
    fetch(`${serverURL}/api/latvanyossagok`).
    then(res=>res.json()).
    then(res=>{
        res.forEach(element => 
            {
                document.querySelector("#latvanyossagokTabla").innerHTML+=
                `
                <tr>
                  <td>${element.Nev}</td>
                  <td class="overflow-scroll">${element.RLeiras}</td>
                  <td>${element.VId.OId.Nev}: ${element.VId.Nev}</td>
                  <td>${element.AtlagErtekeles}</td>
                  <td>${element.Nyitvatartas}</td>
                  <td>${element.URL}"</td>        
                </tr>
                `;
            
            })
    });
}

function telepulesekOption(){
    fetch(`${serverURL}/api/telepulesek`).
    then(res=>res.json()).
    then(res=>{
        res.forEach(element => 
            {
                document.querySelector("#telepulesek").innerHTML +=
                `
                <option value="${element.id}">${element.Nev}</option>
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



function addLatvanyossag()
{
    let _nev = document.querySelector("#nev").value;
    let _rLeiras = document.querySelector("#rleiras").value.replaceAll("\n","\r\n");
    let _telepulesId = document.querySelector("#telepulesek").value;
    let _atlagErt = document.querySelector("#atlagErtekeles").value;
    let _nyitva = document.querySelector("#nyitvatartas").value;
    let _url = document.querySelector("#url").value;
    

    let _data = JSON.stringify(
        {
            Nev: _nev,
            RLeiras: _rLeiras,
            AtlagErtekeles: _atlagErt,
            Nyitvatartas: _nyitva,
            URL: _url,
            VId: _telepulesId,
        }
    );
    fetch("http://127.0.0.1:8000/api/latvanyossagok",
        {
            method:'POST',
            headers:
            {
                'Content-Type':'application/json'
            },
            body:_data
        }
    ).then(res=>res.json())
    .then(data=>
        {
            console.log("Látváyosság sikeresen hozzáadva!")
            window.location.reload();
        })
    .catch(error=>console.log(error));
}
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