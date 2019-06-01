(function($) {
    'use strict';

    $(document).ready(function() {

        $("#lookup_id_vehicle" ).click(function(event) {
            if ($("#id_start_time_0").val() == "") {
                alert("Please enter the arrival date");
            } else if ($("#id_start_time_1").val() == "") {
                alert("Please enter the arrival time");
            } else if ($("#id_end_time_0").val() == "") {
                alert("Please enter the departure date");
            } else if ($("#id_end_time_1").val() == "") {
                alert("Please enter the departure time");
            } else {
                var start_time = $("#id_start_time_0").val() + " " + $("#id_start_time_1").val();
                var end_time = $("#id_end_time_0").val() + " " + $("#id_end_time_1").val();

                var url1 = "&order__start_time__gte=" + start_time + "&order__start_time__lt=" + end_time;
                var url2 = "&order__end_time__gte=" + start_time + "&order__end_time__lt=" + end_time;
                var url = url1 + url2 + '&is_actived=1';
           
                set_vehicle_lookup($("#lookup_id_vehicle"), url);
            }
        });

        $("#lookup_id_guide" ).click(function(event) {
            if ($("#id_start_time_0").val() == "") {
                alert("Please enter the arrival date");
            } else if ($("#id_start_time_1").val() == "") {
                alert("Please enter the arrival time");
            } else if ($("#id_end_time_0").val() == "") {
                alert("Please enter the departure date");
            } else if ($("#id_end_time_1").val() == "") {
                alert("Please enter the departure time");
            } else {
                var start_time = $("#id_start_time_0").val() + " " + $("#id_start_time_1").val();
                var end_time = $("#id_end_time_0").val() + " " + $("#id_end_time_1").val();

                var url1 = "&order__start_time__gte=" + start_time + "&order__start_time__lt=" + end_time;
                var url2 = "&order__end_time__gte=" + start_time + "&order__end_time__lt=" + end_time;
                var url = url1 + url2 + "&is_tourguide=1" + "&is_actived=1";
           
                set_guide_lookup($("#lookup_id_guide"), url);
            }
        }); 

        function get_lookup(id) {
            return $(id).attr('href');
        }

        function set_vehicle_lookup(id, url) {
            if (set_vehicle_lookup.url == null) {
                set_vehicle_lookup.url = get_lookup(id);
            }

            $(id).attr('href', set_vehicle_lookup.url + url);
        }

        function set_guide_lookup(id, url) {
            if (set_guide_lookup.url == null) {
                set_guide_lookup.url = get_lookup(id);
            }

            $(id).attr('href', set_guide_lookup.url + url);
        }

        function convertSpecialCharacter(str) {
            var arrEntities={'lt':'<','gt':'>','nbsp':' ','amp':'&','quot':'"'};
            return str.replace(/&(lt|gt|nbsp|amp|quot);/ig,function(all,t){return arrEntities[t];});
        }
    });

    
}(django.jQuery));