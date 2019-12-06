$('#v-pills-all-tab a').on('click', function (e) {
    e.preventDefault()
    console.log("ok")
    $('#v-pills-tabContent a[href="#cs"]').tab('show')
    $('#v-pills-tabContent a[href="#poem"]').tab('show')
    $('#v-pills-tabContent a[href="#music"]').tab('show')
  })