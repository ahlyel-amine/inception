window.onload =()=> {
    const body = document.querySelector("body")

    body.style.background = "green"
    const tab = document.createElement("table")
    const tabBody = document.createElement("tbody")
    for (let i = 0; i < 8; i++) {
        const row = document.createElement("tr")
        for (let j = 0; j < 8; j++) {
            const cell = document.createElement("td")
                cell.style.backgroundColor = "green"
                cell.style.width = "256"
                cell.style.height = "256"
                row.appendChild(cell)
            }
        tabBody.appendChild(row)
    }
    body.appendChild(tab)
}
