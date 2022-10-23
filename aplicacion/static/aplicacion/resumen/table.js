function selection(){
    var selected = parseInt(document.getElementById("data-range").value); 
    var gastos;
    if (selected == 1){
        gastos = document.getElementById("table_resumen1");
    }
    else if (selected == 2){
        gastos = document.getElementById("table_resumen2");
    }
    else if (selected == 3){
        gastos = document.getElementById("table_resumen3");
    }
    document.getElementById("table_resumen").innerHTML = gastos.outerHTML;
}