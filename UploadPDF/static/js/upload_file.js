$('#id_document').change(function() {
    var ext = $('#id_document').val().split('.').pop().toLowerCase();
//    var txt = $('#id_document').val().split('\\')
//    $('#file-txt').val(txt[2])
    if($.inArray(ext, ['pdf']) == -1) {
        swal({
            title: "Oops!!",
            text: "Selected file is invalid. Please check file extension.",
            icon: "warning",
        })

        $(".swal-button").click(function(){
            $("#id_document").prop('title',"No file chosen");
            $('#id_document').val("")
            $("#id_document").attr("required", "true");
        });
    }
});

////$('#submit').click(function(){
//$("form#upload-file").submit(function(e){
////e.preventDefault();
////$form = $(this)
////var formData = new FormData(this);
////console.log("clicked----",formData)
////    var txt = $('#up').val()
//    var txt = $('input[name="up"]').val().trim();
//    console.log('clicked...'+txt)
//    var token =  Cookies.get('csrftoken');
//    console.log("-------->>>>"+token)
//    if (txt) {
//            // Create Ajax Call
//            $.ajax({
//                headers: { "X-CSRFToken": token },
//                url: '/upload_file/',
//                method: 'POST',
//                data: {
//                    'file': txt,
//                },
//                dataType: 'json',
//                success: function (data) {
//                console.log("success...")
//    //                if (data.user) {
//    //                  appendToUsrTable(data.user);
//    //                }
//                }
//            });
//          } else {
//            alert("All fields must have a valid value.");
//        }
//});