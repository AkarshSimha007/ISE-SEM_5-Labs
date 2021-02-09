window.onload=function(){

    var teslaModels=[
        {
            "model":"modelX",
            "name":"Model X",
            "price":85000,
            "year":2016
        },
        {
            "model":"model3",
            "name":"Model 3",
            "price":35000,
            "year":2017
        },
        {
            "model":"modelS",
            "name":"Model s",
            "price":65000,
            "year":2017
        }
]

teslaModels.forEach(function(item,index){
    var element=document.createElement("th")
    element.id=item.model
    element.innerHTML=item.name
    document.getElementById("menu").appendChild(element)
})

teslaModels.forEach(mouseOverHanlder);

function mouseOverHanlder(item,index){
    var e=document.getElementById(item.model)
    e.onmouseover=function(){
        var detail=item
        if(detail!=null){
            document.getElementById("data").removeAttribute("hidden")
            document.getElementById("name").innerHTML=detail.name
            document.getElementById("pic").innerHTML='<img src="img/'+detail.model+'.jpg" width=100px>'
            document.getElementById("cost").innerHTML=detail.price
            document.getElementById("year").innerHTML=detail.year
        }
    }

}
}