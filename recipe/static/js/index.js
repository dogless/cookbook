function changeActive(){
	var index = $( ".active" ).index();
	$("li").get(index).className = "";
	$("li").get(index+1).className = "active";
}

