var page = location.href.split("/").slice(-1)[0]

var categories_url = 'data/categories.json';
var posts_url = 'data/posts.json';
var bucketList_url = 'data/bucket-list.json';

// Function read JSON and implement function callback
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

// Function add element about Categories in index.html
function readCategories_index(obj) {
    // Create tag div for categories
    $.each(obj.categories, function(index, value){
        var category = value.toLowerCase().replace(' ', '-');

        // Add sidebar
        var temp = `<a class="list-group-item list-group-item-action" 
                        id="list-${category}-list" 
                        data-toggle="list" 
                        href="#list-${category}" 
                        role="tab" 
                        aria-controls="${category}">
                        ${value}
                    </a>`;
        $(".sidebar-js").append(temp);
        
        // Add main-content
        temp = `<div class="tab-pane fade" id="list-${category}" role="tabpanel" aria-labelledby="list-${category}-list">
                    <h4>${value}</h4>
                    <hr>
                    <div class="card-columns mt-4 list-${category}-js">

                    </div>
                </div>`;
        $(".content-js").append(temp);
    })
    $(`#list-${obj.categories[0].toLowerCase().replace(' ', '-')}-list`).addClass('active')
    $(`#list-${obj.categories[0].toLowerCase().replace(' ', '-')}`).addClass('active show')
}

// Function add element about Post in index.html
function readPost_index(obj) {
	$.each(obj.post, function(index, value){
        var category = value.categories.toLowerCase().replace(' ', '-');
        var date = new Date(value.created);
		var temp = `<a href="" class="card text-center">
                        <img src="${value.featureImage}" class="card-img-top" alt="${value.title}">
                        <div class="card-header">
                            <h5 class="card-title">${value.title}</h5>
                        </div>
                        <div class="card-body">
                            <p class="card-text"><small class="text-muted">Last updated ${date.toDateString()}</small></p>
                        </div>
                    </a>`;
        $(`.list-${category}-js`).append(temp);
        // console.log(date.toUTCString());
	})	
}

// Function add element about Categories in create-posts.html
function readCategories_createPost(obj) {
    // Add Tab choose category
    $.each(obj.categories, function(index, value){
        var category = value.toLowerCase().replace(' ', '-');
        var temp = `<div class="custom-control custom-radio">
                        <input type="radio" class="custom-control-input is-invalid" id="radio-${category}" name="category" value="" required>
                        <label class="custom-control-label" for="radio-${category}">${value}</label>
                    </div>`;
        $(`.choose-category-js`).append(temp)
    });

    var lastRadio = `#radio-${obj.categories.slice(-1)[0].toLowerCase().replace(' ', '-')}`;
    var warningCategory = `<div class="invalid-feedback">Please choose categories</div>`;
    $(lastRadio).parent().append(warningCategory);
}

// Function add bucket list bucket.html
function readBucketList_bucket(obj) {
	checked = ['✗', '✓'];
	$.each(obj.bucket, function(index, value){
		var temp = "<li>"+ checked[value.checked] + " " + value.content + "</li>";
		$(".show-bucket-list").append(temp);
	})	
}

if (page == "" || page == "index.html") {
    loadDoc(categories_url, readCategories_index);
    loadDoc(posts_url, readPost_index);
} else if (page == "bucket.html") {
    loadDoc(bucketList_url, readBucketList_bucket);
} else if (page == "create-post.html") {
    loadDoc(categories_url, readCategories_createPost);
}
