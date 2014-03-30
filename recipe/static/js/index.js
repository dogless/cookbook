function moveActiveLeft(){
	var index = $( ".active" ).index();
	if (index != 0){
		$(".recipe-item").get(index).className = "recipe-item";
		$(".recipe-item").get(index-1).className = "active recipe-item";
	}
}

function moveActiveRight(){
	var lis = $("#recipes li");
	var index = $( ".active" ).index();

	if (index != lis.length-1){
		$(".recipe-item").get(index).className = "recipe-item";
		$(".recipe-item").get(index+1).className = "active recipe-item";
	}
}

function moveActiveDown(){
	var lis = $("#recipes li");
	var index = $( ".active" ).index();

	if (index < lis.length-5){
		$(".recipe-item").get(index).className = "recipe-item";
		$(".recipe-item").get(index+5).className = "active recipe-item";
	}
}

function moveActiveUp(){
	var index = $( ".active" ).index();
	if (index - 5 >= 0){
		$(".recipe-item").get(index).className = "recipe-item";
		$(".recipe-item").get(index-5).className = "active recipe-item";
	}
}

function openRecipe(){
	var index = $( ".active" ).val();
	var newLocation = "/recipe/" + index;
	location.href = newLocation;
}
