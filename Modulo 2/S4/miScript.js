$(document).ready(function() {
	$('#text1').hover(function() {
		$('#text2').toggle();
	});
	$("#caja3").click(function() {
		var fontSize = parseInt($(this).css("font-size"));
		if (fontSize < 18) {
		  fontSize += 2;
		} else {
		  fontSize -= 2;
		}
		$(this).css("font-size", fontSize + "px");
	  });
});