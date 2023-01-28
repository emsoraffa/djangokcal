function navigateDate(direction) {
    selected = document.getElementById("date").value
    if (direction == "Left"){
        day = Number(selected.split('-')[2])
        newDay = day - 1
        document.getElementById("date").value = selected.split('-')[0]+'-'+selected.split('-')[1]+'-'+newDay
    }
    else {
        day = Number(selected.split('-')[2])
        newDay = day + 1
        document.getElementById("date").value = selected.split('-')[0]+'-'+selected.split('-')[1]+'-'+newDay
    }
  }