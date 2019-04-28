(function($) {
    'use strict';

    

    $(document).ready(function() {
        console.log('hello oder');

        $("#lookup_id_vehicle" ).click(function(event) {
            if ($("#id_arrival_time_0").val() == "") {
                alert("Please enter the arrival date");
            } else if ($("#id_arrival_time_1").val() == "") {
                alert("Please enter the arrival time");
            } else if ($("#id_departure_time_0").val() == "") {
                alert("Please enter the departure date");
            } else if ($("#id_departure_time_1").val() == "") {
                alert("Please enter the departure time");
            } else {
                var arrival_time = $("#id_arrival_time_0").val() + " " + $("#id_arrival_time_1").val();
                var departure_time = $("#id_departure_time_0").val() + " " + $("#id_departure_time_1").val();

                var url1 = "&order__arrival_time__gte=" + arrival_time + "&order__arrival_time__lt=" + departure_time;
                var url2 = "&order__departure_time__gte=" + arrival_time + "&order__departure_time__lt=" + departure_time;
                var url = url1 + url2;
           
                set_vehicle_lookup($("#lookup_id_vehicle"), url);
            }
        });

        $("#lookup_id_guide" ).click(function(event) {
            if ($("#id_arrival_time_0").val() == "") {
                alert("Please enter the arrival date");
            } else if ($("#id_arrival_time_1").val() == "") {
                alert("Please enter the arrival time");
            } else if ($("#id_departure_time_0").val() == "") {
                alert("Please enter the departure date");
            } else if ($("#id_departure_time_1").val() == "") {
                alert("Please enter the departure time");
            } else {
                var arrival_time = $("#id_arrival_time_0").val() + " " + $("#id_arrival_time_1").val();
                var departure_time = $("#id_departure_time_0").val() + " " + $("#id_departure_time_1").val();

                var url1 = "&order__arrival_time__gte=" + arrival_time + "&order__arrival_time__lt=" + departure_time;
                var url2 = "&order__departure_time__gte=" + arrival_time + "&order__departure_time__lt=" + departure_time;
                var url = url1 + url2;
           
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

        // function getAction(url) {
        //     var sub = url.substr(0, url.length - 1);
        //     var action = sub.substr(sub.lastIndexOf("/") + 1);
        //     return action;
        // }

        // function getOrderType(str) {
            
        //     switch(str) {
        //         case "Vehicle":
        //         return "0";

        //         case "Driver":
        //         return "1";

        //         case "Tourguide":
        //         return "2";

        //         case "Driver & Tourguide":
        //         return "3";

        //         case "Driver & Vehicle":
        //         return "4";
        //     }
        // }

        // function getDeliveryType(str) {
        //     if (str == "Self") {
        //         return "0";
        //     } else {
        //         return "1";
        //     }
        // }

        function convertSpecialCharacter(str) {
            var arrEntities={'lt':'<','gt':'>','nbsp':' ','amp':'&','quot':'"'};
            return str.replace(/&(lt|gt|nbsp|amp|quot);/ig,function(all,t){return arrEntities[t];});
        }
    });

    
}(django.jQuery));