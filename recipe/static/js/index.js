function moveActiveLeft(){
	var index = $( ".active" ).index();
	if (index != 0){
		$("li").get(index).className = "";
		$("li").get(index-1).className = "active";
	}
}

function moveActiveRight(){
	var lis = $("#recipes li");
	var index = $( ".active" ).index();

	if (index != lis.length-1){
		$("li").get(index).className = "";
		$("li").get(index+1).className = "active";
	}
}

function moveActiveDown(){
	var lis = $("#recipes li");
	var index = $( ".active" ).index();

	if (index < lis.length-5){
		$("li").get(index).className = "";
		$("li").get(index+5).className = "active";
	{
}

function moveActiveUp(){
	var index = $( ".active" ).index();
	if (index - 5 > 0){
		$("li").get(index).className = "";
		$("li").get(index-5).className = "active";
	}
}
