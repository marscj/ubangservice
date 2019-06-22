(function($) {
    'use strict';

    $(document).ready(function() {
        
        change_type($("#id_detail_type").val());

        $("#id_detail_type").change(function(){
            change_type($("#id_detail_type").val());
        });

        function change_type(type) {
            switch (type) {
                case "2":
                    $('#id_amount').parent().parent().attr("style","display:none");
                break;

                case "3":
                    $('#id_amount').parent().parent().attr("style","display:block");
                break;
            }
        }
    });

    
}(django.jQuery));