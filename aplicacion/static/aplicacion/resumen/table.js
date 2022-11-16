function selection_gastos(){
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
    else if (selected == 4){
        gastos = document.getElementById("resumen_anual");
    }
    document.getElementById("table_resumen").innerHTML = gastos.outerHTML;
    document.querySelectorAll(".table-sortable th").forEach(headerCell => {
        headerCell.addEventListener("click", () => {
            const tableElement = headerCell.parentElement.parentElement.parentElement;
            const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
            const currentIsAscending = headerCell.classList.contains("th-sort-asc");
    
            sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
        });
    });
}

function selection_ingresos(){
    var selected = parseInt(document.getElementById("data-range2").value); 
    var ingresos;
    if (selected == 1){
        ingresos = document.getElementById("table_ingresos1");
    }
    else if (selected == 2){
        ingresos = document.getElementById("table_ingresos2");
    }
    else if (selected == 3){
        ingresos = document.getElementById("table_ingresos3");
    }
    else if (selected == 4){
        ingresos = document.getElementById("resumen_anual_ingresos");
    }
    document.getElementById("table_resumen_ingresos").innerHTML = ingresos.outerHTML;
    document.querySelectorAll(".table-sortable th").forEach(headerCell => {
        headerCell.addEventListener("click", () => {
            const tableElement = headerCell.parentElement.parentElement.parentElement;
            const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
            const currentIsAscending = headerCell.classList.contains("th-sort-asc");
    
            sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
        });
    });
}


 function sortTableByColumn(table, column, asc = true) {
	const dirModifier = asc ? 1 : -1;
	const tBody = table.tBodies[0];
	const rows = Array.from(tBody.querySelectorAll("tr"));

	// Sort each row
	const sortedRows = rows.sort((a, b) => {
		const aColText = a.querySelector(`td:nth-child(${column + 1})`).textContent.trim();
		const bColText = b.querySelector(`td:nth-child(${column + 1})`).textContent.trim();

        var date_a = new Date(aColText);
        var date_b = new Date(bColText);
        if (date_a instanceof Date && !isNaN(date_a.valueOf())){
            return (date_a - date_b >= 0)? (1*dirModifier):(-1*dirModifier);
        }

		return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
	});

	// Remove all existing TRs from the table
	while (tBody.firstChild) {
		tBody.removeChild(tBody.firstChild);
	}

	// Re-add the newly sorted rows
	tBody.append(...sortedRows);

	// Remember how the column is currently sorted
	table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
	table.querySelector(`th:nth-child(${column + 1})`).classList.toggle("th-sort-asc", asc);
	table.querySelector(`th:nth-child(${column + 1})`).classList.toggle("th-sort-desc", !asc);
}

document.querySelectorAll(".table-sortable th").forEach(headerCell => {
	headerCell.addEventListener("click", () => {
		const tableElement = headerCell.parentElement.parentElement.parentElement;
		const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
		const currentIsAscending = headerCell.classList.contains("th-sort-asc");

		sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
	});
});