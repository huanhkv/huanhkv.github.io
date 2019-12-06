$(document).ready(function() {
	$( ".card" ).hover(
		function() {
			$(this).addClass('shadow-lg').css('cursor', 'pointer'); 
			// $(this).children('img').css('transform', 'scale(1.1)');
		}, function() {
			$(this).removeClass('shadow-lg');
			// $(this).children('img').css('transform', 'scale(1)');
		}
	);
});

