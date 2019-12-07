data = '[{"blue" : "is ok", "red" : "is my fave color"}]';
path_json = 'post/content.json'

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    console.log(myObj.post[0].title)
  }
};
xmlhttp.open("GET", path_json, true);
xmlhttp.send();