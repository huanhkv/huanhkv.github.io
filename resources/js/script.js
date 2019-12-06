$(document).ready(function() {
	$( ".card" ).hover(
		function() {
			if (!$(this).attr("class").includes("non-pointer"))
				$(this).addClass('shadow-lg').css('cursor', 'pointer');
		}, function() {
			if (!$(this).attr("class").includes("non-pointer"))
				$(this).removeClass('shadow-lg');
		}
	);
});

// $(".main-content").css('min-height', 100vh - $("header").innerHeight() - $("footer").innerHeight()+'px')