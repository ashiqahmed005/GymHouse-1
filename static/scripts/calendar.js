/**
 *  Add a getWeek() method in Javascript inbuilt Date object.
 * This function is the colsest I could find which is ISO-8601 compatible. This is what php's `Date->format('w')` uses.
 * ISO-8601 means.
 *    Week starts from Monday.
 *    Week 1 is the week with first thurday of the year or the week which has 4th jan in it.
 * @param  {[Date]}   Prototype binding with Date Object. 
 * @return {[Int]}    Integer from 1 - 53 which denotes the week of the year.
 */
/*
Date.prototype.getWeek = function() { 

  // Create a copy of this date object  
  var target  = new Date(this.valueOf());  

  // ISO week date weeks start on monday, so correct the day number  
  var dayNr   = (this.getDay() + 6) % 7;  

  // Set the target to the thursday of this week so the  
  // target date is in the right year  
  target.setDate(target.getDate() - dayNr + 3);  

  // ISO 8601 states that week 1 is the week with january 4th in it  
  var jan4    = new Date(target.getFullYear(), 0, 4);  

  // Number of days between target date and january 4th  
  var dayDiff = (target - jan4) / 86400000;    

  if(new Date(target.getFullYear(), 0, 1).getDay() < 5) {
    // Calculate week number: Week 1 (january 4th) plus the    
    // number of weeks between target date and january 4th    
    return 1 + Math.ceil(dayDiff / 7);    
  }
  else {  // jan 4th is on the next week (so next week is week 1)
    return Math.ceil(dayDiff / 7); 
  }
};
*/
//Month number 1...12
getMonthName = function(month){
    var monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    return monthNames[(month-1)];
};
/*
Date.prototype.getDayOfWeek = function() {
    return (new Date().getDay() || 7 - 1);
};


function daysInMonth(month, year) {
  return new Date(year, month, 0).getDate();
}

//DOESNT WORK
function getWeekRange(weekNo){
    var d1 = new Date();
    var d2 = new Date();
    var numOfdaysPastSinceLastMonday = d1.getDay()- 1;
    d1.setDate(d1.getDate() - numOfdaysPastSinceLastMonday);
    var weekNoToday = d1.getWeek();
    var weeksInTheFuture = weekNo - weekNoToday;
    d1.setDate(d1.getDate() + ( 7 * weeksInTheFuture ));
    d2.setDate(d1.getDate() + 6);
    return [d1.getDate(),d1.getMonth()+1,d2.getDate(),d2.getMonth()+1];
}
*/
/*
function getWeekRange(dateStr) {
    if (!dateStr) dateStr = new Date().getTime();
    var dt = new Date(dateStr);
    dt = new Date(dt.getFullYear(), dt.getMonth(), dt.getDate());
    dt = new Date(dt.getTime() - (dt.getDay() > 0 ? (dt.getDay() - 1) * 1000 * 60 * 60 * 24 : 6 * 1000 * 60 * 60 * 24));
    dt2 = new Date(dt.getTime() + 1000 * 60 * 60 * 24 * 7 - 1);
    return [dt.getDate(), dt.getMonth()+1, dt2.getDate(), dt2.getMonth()+1];
}
*/


addDatesToCalendar = function(week, year){
    /*
    var date = new Date();

    //var dt = new Date(year, )

    //var month = date.getMonth() + 1; // month eg, 11

    //gets the month from the last day of the current week
    var month = getWeekRange(week)[1];
    var month2 =getWeekRange(week)[3];
    console.log("THE WEEK WERE CURRENTLY OBSERVING IS " + week + "," +year);
    console.log("MONTHS: " + month + ", " + month2);
    console.log("Week range: " + getWeekRange(week));
    console.log("Week range2 = " + getWeekRange(week));
    
    var dayToday = date.getDate();       //day eg. 21
    var firstDay = getWeekRange(week)[0];
    //var weekDay = date.getDayOfWeek();    //day of the week eg. 1. (monday)
    


    console.log("day = " + dayToday + "firstDay = " + firstDay);
    console.log("month =" + month);
    */

    console.log("creating new moment with week " + week +" and year " + year);
    var currentMonday = new moment().year(year).isoWeek(week);

    console.log("moment currentMonday = " + currentMonday);
    console.log("moment currentMonday.format = " + currentMonday.format("DD/MM/YYYY"));

    currentMonday.isoWeekday(1);
    year = currentMonday.year();
    console.log("Set year according to currentMonday = " + year);

    console.log("Setting currentMonday to monday of the week: " + currentMonday.format("DD/MM/YYYY"));



    $(".dayElementContainer").html(""); //clear the container before rendering
    var $dayElement;
    var month = currentMonday.month()+1;
    var month2 = currentMonday.clone().add(6,'days').month()+1;
    console.log("month1 =" + month +" month2 = " + month2);


    var lastDay = currentMonday.clone().add(6,'days').date();

    for(var i = 0; i < 7; i++){
        var currentDay = currentMonday.clone().add(i,'days');   
        var currentMoment = currentDay;
        currentDay = currentDay.date();
        var currentMonth = currentMoment.month()+1;
        //lastDay
        console.log("currentDay = " + currentDay + ", month=" + currentMonth +" lastDay =" + lastDay);
        
        if(i==6){
            month2=currentMonth;
        }


        //A new month started but the month variable holds the new month
        /*
        if (getWeekRange(week)[1]!=getWeekRange(week)[3]){
            console.log("MONTH CHANGED");
            if (currentDay <= lastDay) {
                currentMonth=month;
                console.log("CURRENTDAY NOT OF NEW MONTH");
            }
            else{
                currentMonth=month+1;
                if (month > 12) month = 1;
                if (month < 1 ) month = 12;
                currentDay = currentDay%lastDay;
                console.log("currentday IS NEW MONTH");
            }
            lastDay = daysInMonth(currentMonth, year);
            console.log("month: " + month +" currentmonth = " + currentMonth);
        }
        */
        console.log("Calculating days i="+i+". Current: "+currentDay+", NEWlast"+lastDay);
        


        $dayElement = $(
            "<div class='dayElement' id="+i+">" +
                "<div class='dayOfMonth'>"+currentDay+"."+currentMonth+".</div>" +
                "<div class='classes'>" +
                    "<div class='timeSlots'></div>" +
                "</div>" +
            "</div>"
        );


    /*
    for(var i = 0; i < 7; i++){
        var currentDay = firstDay+i;
        var currentMonth = month;
        var lastDay = daysInMonth(currentMonth,year);
        console.log("month: " + month +" currentmonth = " + currentMonth);
        //A new month started but the month variable holds the new month
        if (getWeekRange(week)[1]!=getWeekRange(week)[3]){
            console.log("MONTH CHANGED");
            if (currentDay <= lastDay) {
                currentMonth=month;
                console.log("CURRENTDAY NOT OF NEW MONTH");
            }
            else{
                currentMonth=month+1;
                if (month > 12) month = 1;
                if (month < 1 ) month = 12;
                currentDay = currentDay%lastDay;
                console.log("currentday IS NEW MONTH");
            }
            lastDay = daysInMonth(currentMonth, year);
            console.log("month: " + month +" currentmonth = " + currentMonth);
        }
        console.log("Calculating days i="+i+". Current: "+currentDay+", NEWlast"+lastDay);
        


        $dayElement = $(
            "<div class='dayElement' id="+i+">" +
                "<div class='dayOfMonth'>"+currentDay+"."+currentMonth+".</div>" +
                "<div class='classes'>" +
                    "<div class='timeSlots'></div>" +
                "</div>" +
            "</div>"
        );
    */






        for (var j = 8; j<20; j++){
            $dayElement.find(".timeSlots").append(
                "<div id='"+ (j-8) +"' class='time'>" + 
                    "Timeslot from " + j +". " +
                "</div>"
                //HERE WILL BE DATA FOR CLASSES ETC
            );
        }
        console.log("---------__");
        $(".dayElementContainer").append($dayElement);
        /*
        if(firstDay+i==dayToday){
            $dayElement.addClass('active');
        }
        */
    }
    console.log("#######################");
    $(".weeknumber").text("Week "+ week);
    var monthName = getMonthName(month);
    if (month != month2)
        monthName += ("/"+getMonthName(month2));
    $(".monthYear").text(monthName +", " + year);

    var nextWeekMoment = currentMonday.add(1,'week');
    console.log("nextWeekMoment = " + nextWeekMoment.format("DD/MM/YYYY"));
    console.log("Isoweek: " + nextWeekMoment.isoWeek());

    return [nextWeekMoment.isoWeek(),year];
};


$(document).ready(function(){
    /*
    var date = new Date();
    var year = date.getFullYear(); //year eg, 2016
    //var month = date.getMonth() + 1; // month eg, 11
    var week = date.getWeek();
    //var day = date.getDate();       //day eg. 21
    //var weekDay = date.getDayOfWeek();    //day of the week eg. 1. (monday)
    //var firstDay = getDateRangeOfWeek(week)[0];
    //console.log("Date = " + year +", " + month +", " + day + ". Day num = " + weekDay);
    //console.log("Week starts with: " + getDateRangeOfWeek(week));


    var dateToday = new Date();
    var dt = new Date();
    var daysFromMonday = ((dateToday.getDate() || 6)+1);
    var mondayDate = dateToday.getDate() - daysFromMonday;

    console.log("mondayDate="+mondayDate);

    mondayDate = (dt.setDate(date.getDate()-7)) -daysFromMonday;
    console.log("mondayDate last week="+mondayDate);
*/


    //MOMENTMOMENTMOMENTMOMENTMOMENTMOMENTMOMOENTM
    var m = new moment();
    console.log("MOMENT : " + m.format("DD/MM/YYYY"));
    var myear = m.year();
    var mmonth = m.month() +1;
    var mday = m.date();
    var mweekday = m.isoWeekday();
    var mweek = m.isoWeek();

    console.log("MOMENT DMY: " + myear + " " + mmonth +
        " " + mday + " " + mweekday + " week: " + mweek);

    console.log(typeof(mweek));


    addDatesToCalendar(mweek,myear);


    //Add hours to column "hours"
    for(var i = 0; i<12; i++){
        $(".timeLabel").find(".hours").append(
            "<div class='hour'>"+(i+8)+ "-" + (i+9) + "</div>"
        );
    }



    $(".prev").click(function(){
        console.log("clicked PREVIOUS!");
        // week-=1;
        // if (week < 1){
        //     week = 52;
        //     year-=1;
        // }
        if (mweek==1){
            myear-=1;
        }
        var ar = addDatesToCalendar(mweek,myear);
        mweek = ar[0];
        myear = ar[1];
    });
    $(".next").click(function(){
        console.log("clicked NEXT!");
        // week+=1;
        // if (week> 52){
        //     week = 1;
        //     year+=1;
        // }
        if (mweek==52){
            myear+=1;
        }
        var ar = addDatesToCalendar(mweek,myear);
        mweek = ar[0];
        myear = ar[1];
    });

});