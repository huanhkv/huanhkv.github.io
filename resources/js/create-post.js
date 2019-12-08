$("#btn-review").click(function(){
    $("#review").html($("#contentPost").val())
});

$("input[name='create-post-form']").submit(function(event) {
    console.log("Got")
    event.preventDefault();
    return false;
});