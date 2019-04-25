(function($) {
    'use strict';

    $(document).ready(function() {
        console.log('hello oder')

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
           
                set_lookup($("#lookup_id_vehicle"), url);
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
           
                set_lookup($("#lookup_id_guide"), url);
            }
        }); 

        function get_lookup(id) {
            return $(id).attr('href');
        }

        function set_lookup(id, url) {
            if (set_lookup.url == null) {
                set_lookup.url = get_lookup(id)
            }

            $(id).attr('href', set_lookup.url + url);
        }

        // order__arrival_time__lt=2019-04-25%2000:00&order__arrival_time__gt=2019-04-25%2000:00&_popup=1
        // order__arrival_time__lt=2019-04-25%2000:00&order__arrival_time__gt=2019-04-25%2023:00&_popup=1
        // order__arrival_time__gte=2019-04-25+00%3A00%3A00&order__arrival_time__lt=2019-04-26+00%3A00%3A00



        // delivery($("#id_service_type").val());

        // if (getAction(window.location.href) == "add") {
        //     order($("#id_order_type").val());
        // } else {
        //     var orderType = convertSpecialCharacter($('fieldset').find('p').eq(4).html().trim());
        //     order(getOrderType(orderType));
        // }
        
        // $("#id_service_type").change(function(){
        //     delivery($("#id_service_type").val());
        // });

        // $("#id_order_type").change(function(){
        //     order($("#id_order_type").val());
        // });

        // $('#lookup_id_vehicle').mousedown(function() {
        //     if (getAction(window.location.href) == "add") {
        //         var start_date = $('#id_start_time_0').val();
        //         var start_time = $('#id_start_time_1').val();
        //         var end_date = $('#id_end_time_0').val();
        //         var end_time = $('#id_end_time_1').val();
        //         var orderType = convertSpecialCharacter($('#id_order_type').val());
        //         setupVehicle(getStartTime(start_date, start_time), getEndTime(end_date, end_time), null, orderType);
        //     } else {
        //         var orderId = $('fieldset').find('p').eq(0).html().trim(); 
        //         var start = $('fieldset').find('p').eq(1).html().trim();
        //         var end = $('fieldset').find('p').eq(2).html().trim();
        //         var orderType = convertSpecialCharacter($('fieldset').find('p').eq(4).html().trim());
        //         setupVehicle(start, end, orderId, getOrderType(orderType));
        //     }
        // });

        // $('#lookup_id_staff').mousedown(function() {
        //     if (getAction(window.location.href) == "add") {
        //         var start_date = $('#id_start_time_0').val();
        //         var start_time = $('#id_start_time_1').val();
        //         var end_date = $('#id_end_time_0').val();
        //         var end_time = $('#id_end_time_1').val();
        //         var orderType = convertSpecialCharacter($('#id_order_type').val());
        //         setupStaff(getStartTime(start_date, start_time), getEndTime(end_date, end_time), null, orderType);
        //     } else {
        //         var orderId = $('fieldset').find('p').eq(0).html().trim(); 
        //         var start = $('fieldset').find('p').eq(1).html().trim();
        //         var end = $('fieldset').find('p').eq(2).html().trim();
        //         var orderType = convertSpecialCharacter($('fieldset').find('p').eq(4).html().trim());
        //         setupStaff(start, end, orderId, getOrderType(orderType));
        //     }
        // });

        // function delivery(type) {
        //     if (type == '0' || type == '') {
        //         $('#id_pick_up_addr').parent().parent().attr("style","display:none");
        //         $('#id_drop_off_addr').parent().parent().attr("style","display:none");
        //     } else {
        //         $('#id_pick_up_addr').parent().parent().attr("style","display:block");
        //         $('#id_drop_off_addr').parent().parent().attr("style","display:block");
        //     }
        // }

        // function order(type) {
        //     switch (type) {
        //         case "0":
        //             $('#id_staff').parent().parent().attr("style","display:none");
        //             $('#id_staff_status').parent().parent().attr("style","display:none");
        //             $('#id_vehicle').parent().parent().attr("style","display:block");
        //             $('#id_service_type').parent().parent().attr("style","display:block");
        //             delivery($("#id_service_type").val());
        //         break;

        //         default:
        //             $('#id_staff').parent().parent().attr("style","display:block");
        //             $('#id_staff_status').parent().parent().attr("style","display:block");
        //             $('#id_vehicle').parent().parent().attr("style","display:none");
        //             $('#id_service_type').parent().parent().attr("style","display:none");
        //             delivery('0');
        //         break;
        //     }
        // }

        // function setupUrl(id, url, key, start, end, orderId, orderType) {
        //     if (start == null || end == null) {
        //         $(id).attr('href', url);
        //     } else {
        //         if (orderId != null) {
        //             $(id).attr('href', url + '&' + key + 'start_time=' + start + '&' + key + 'end_time=' + end + '&' + key + 'orderId=' + orderId  + '&' + key + 'order_type=' + orderType);
        //         } else {
        //             $(id).attr('href', url + '&' + key + 'start_time=' + start + '&' + key + 'end_time=' + end + '&' + key + 'order_type=' + orderType);
        //         }
        //     }
        // }

        // function setupVehicle(start, end, orderId, orderType) {
        //     if (setupVehicle.url == null) {
        //         setupVehicle.url = $('#lookup_id_vehicle').attr('href');
        //     }
        //     setupUrl('#lookup_id_vehicle', setupVehicle.url, 'order__', start, end, orderId, orderType);
        // }

        // function setupStaff(start, end, orderId, orderType) {
        //     if (setupStaff.url == null) {
        //         setupStaff.url = $('#lookup_id_staff').attr('href');
        //     }
        //     setupUrl('#lookup_id_staff', setupStaff.url, 'order__', start, end, orderId, orderType);
        // }

        // function getStartTime(date, time) {
        //     if (typeof(date) == "undefined" || typeof(time) == "undefined" || date == "" || time == "") {
        //         alert('Please set the start time ！');
        //         return null
        //     }
        //     return date + ' ' + time;
        // }

        // function getEndTime(date, time) {
        //     if (typeof(date) == "undefined" || typeof(time) == "undefined" || date == "" || time == "") {
        //         alert('Please set the end time ！');
        //         return null
        //     }
        //     return date + ' ' + time;
        // }

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