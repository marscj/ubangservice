(function($) {
    'use strict';

    $(document).ready(function() {
        $(".related-lookup").click(function(event){
            if(($(this).parents()[4]).id == "task-group"){
              
                var day = $(this).parent().parent().find(".day").find(".grp-readonly").text();
                var tomorrow = GetDateStr(day, 1);
                var url = "&task__day__gte=" + day + "&task__day__lt=" + tomorrow + "&task__is_freedom_day=1" + "&is_actived=1" ;

                if ($(this).parent().hasClass("guide")){
                    set_guide_lookup(this, url + "&is_tourguide=1");
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

        function GetDateStr(day, AddDayCount) {
            var dd = new Date(day);
            dd.setDate(dd.getDate()+AddDayCount);//获取AddDayCount天后的日期
            var y = dd.getFullYear();
            var m = dd.getMonth()+1;//获取当前月份的日期
            var d = dd.getDate();
            return y+"-"+m+"-"+d;
        }

        function convertSpecialCharacter(str) {
            var arrEntities={'lt':'<','gt':'>','nbsp':' ','amp':'&','quot':'"'};
            return str.replace(/&(lt|gt|nbsp|amp|quot);/ig,function(all,t){return arrEntities[t];});
        }
    });

    
}(django.jQuery));