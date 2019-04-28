(function($) {
    'use strict';

    $(document).ready(function() {
        console.log("hello task");

        $(".related-lookup").click(function(event){
            if(($(this).parents()[4]).id == "task-group"){
                var day = $(this).parent().parent().find(".day").find(".grp-readonly").text();
                var url = "&task__day=" + day;

                if ($(this).parent().hasClass("guide")){
                    set_guide_lookup(this, url);
                } else if ($(this).parent().hasClass("vehicle")){
                    set_vehicle_lookup(this, url);
                }
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