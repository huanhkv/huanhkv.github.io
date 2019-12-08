var page = location.href.split("/").slice(-1)[0];

// Add Tab div
var header = 	`<header class="navbar navbar-expand-md navbar-dark navbar-custom sticky-top border-bottom">
					<a class="navbar-brand" href=".">Winter HoKha</a>

					<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
						<span class="navbar-toggler-icon"></span>
					</button>

					<div class="collapse navbar-collapse flex-grow-0 ml-auto" id="navbarSupportedContent">
						<ul class="navbar-nav mr-auto">
							<li class="nav-item ${(page == "" || page == "index.html") ? "active" : ""}">
								<a class="nav-link" href="index.html">Home</a>
							</li>
							<li class="nav-item ${(page == "about.html") ? "active" : ""}">
								<a class="nav-link" href="about.html">About</a>
							</li>
							<li class="nav-item ${(page == "bucket.html") ? "active" : ""}">
								<a class="nav-link" href="bucket.html">Bucket list</a>
							</li>
						</ul>
					</div>
				</header>`;

$("body").prepend(header);



$(".card").hover(
	function() {
		if (!$(this).attr("class").includes("non-pointer"))
			$(this).addClass('shadow-lg').css('cursor', 'pointer');
	}, function() {
		if (!$(this).attr("class").includes("non-pointer"))
			$(this).removeClass('shadow-lg');
	}
);