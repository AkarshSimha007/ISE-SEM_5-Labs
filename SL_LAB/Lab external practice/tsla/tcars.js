window.onload=function(){

    var teslaModels=[
        {
            "model":"modelS",
            "name":"Model S",
            "price":69500,
            "year":2016
        },
        {
            "model":"modelX",
            "name":"Model X",
            "price":89500,
            "year":2017
        },
        {
            "model":"model3",
            "name":"Model 3",
            "price":35000,
            "year":2017
        }
    ];

    teslaModels.forEach(function(item,index){
        listEle=document.createElement("th");
        listEle.id=item.model;
        listEle.innerHTML=item.name;
        document.getElementById("menu").appendChild(listEle);
    })

    teslaModels.forEach(mouseOverHandler);

    function mouseOverHandler(item,index){
        var ele=document.getElementById(item.model);
        ele.onmouseover=function(){
            var details=item;
            if(details!=null){
                document.getElementById("data").removeAttribute("hidden");
                document.getElementById("model").innerHTML=details.name;
                document.getElementById("pic").innerHTML='<img src="img/'+details.model+'.jpg" width=100px>';
                document.getElementById("cost").innerHTML=details.price;
                document.getElementById("year").innerHTML=details.year;
            }
        }

    }
};