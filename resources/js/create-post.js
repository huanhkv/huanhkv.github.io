// Validation input before submit create post
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

// Event button review post
$("#btn-review").click(function(){
    let title = $("#postTitleForm").val();
    let created = new Date();
    let content = $("#contentPost").val();

    $("#review-title").html(title);
    $("#review-created").html(created.toJSON());
    $("#review-content").html(content);

    var export_json =   `{
                            "title":"${title}",
                            "created":"${created.toJSON()}",
                            "update":"",
                            "categories":"${$('input[name=category]:checked').val()}",
                            "featureImage":"${$("#featuredImage").val()}",
                            "content":"${content.replace(/\r?\n/g, '<br>').replace(/"/g, "'")}"
                        }`;
    console.log(export_json);
});

$("input[name='create-post-form']").submit(function(event) {
    console.log("Got")
    event.preventDefault();
    return false;
});