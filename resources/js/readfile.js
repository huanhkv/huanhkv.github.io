var page = location.href.split("/").slice(-1)

var categories_url = 'data/categories.json';
var posts_url = 'data/posts.json';
var bucketList_url = 'data/bucket-list.json';

function loadDoc(url, callback) {
    var xhttp;
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var obj = JSON.parse(this.responseText);
            callback(obj);
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function readCategories(obj) {
    // Create tag div for categories
}

function readPost(obj) {
	$.each(obj.post, function(index, value){
        value.categories
		// var temp = "<li>"+ checked[value.checked] + " " + value.content + "</li>"
        // $(".show-bucket-list").append(temp)
        
        // <a href="" class="card text-center">
        //     <img src="images/Untitled.png" class="card-img-top" alt="...">
        //     <div class="card-header">
        //         <h5 class="card-title">Card title</h5>
        //     </div>
        //     <div class="card-body">
        //         <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
        //     </div>
        // </a>
	})	
}

function readBucketList(obj) {
	checked = ['✗', '✓'];
	$.each(obj.bucket, function(index, value){
		var temp = "<li>"+ checked[value.checked] + " " + value.content + "</li>"
		$(".show-bucket-list").append(temp)
	})	
}

if (page == "") {
    loadDoc(categories_url, readCategories);
    loadDoc(posts_url, readPost);
} else if (page == "bucket.html") {
    loadDoc(bucketList_url, readBucketList);
}
