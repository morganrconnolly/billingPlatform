/*Menu Toggle and Sidebar Select Script --> */

    $("#menu-toggle-button").click(function(e) {
        e.preventDefault();
        $(".sidebar").toggleClass("toggled");
    });

    $(".sidebar-nav a").click(function(e) {
        $(".sidebar-nav>li.active").removeClass("active");
        $(this).closest('li').addClass("active");
    });


/* select the first button */
    $(".btn-group .btn").first().button("toggle");


/* Insert the date on the page */

    var day;
    if(Math.random()<.5){
        day = moment("09/28/2016").format("dddd, MMMM Do YYYY");
    }else{
        day = moment("06/07/2016").format("dddd, MMMM Do YYYY");
    }
    var commaSpot = day.indexOf(",");
    day = "<span>" + day.substring(0, commaSpot +2) + "</span>" + day.substring(commaSpot+2);
    $(".long-date").html(day);

/* Clicks for different date buttons */
    var confirmDiscardButtons = '<span class="areyousure">Are you sure?</span><button type="button" class="btn btn-default btn-sm yes-button">Yes</button><button type="button" class="btn btn-default btn-sm no-button">No</button>';

    var checkMarkDetailsButton = '<button type="button" class="btn btn-default btn-sm confirmed"><span class="glyphicon glyphicon-ok confirmed-session-icon"></span>&nbsp;Confirmed</button><button type="button" class="btn btn-link btn-sm modify">Modify</button>';

    var confirmedByBrianSkinner = '<div class="col-xs-11 col-xs-offset-1 toggled"><span class="glyphicon glyphicon-ok confirmed-session-icon"></span><span class="details-text">Confirmed by Brian Skinner on 4/6/2015</span></div>';



    var showDetails = function(e) {
        $(this).parent().parent().next().children(".details-box div").addClass("toggled"); 
    };
    $("button.confirmed").hover(showDetails);


    var handleModifyClicked = function(e) {
        //show the new buttons
        $(this).parent().html('<button type="button" class="btn btn-default btn-sm session-moved">Move</button><button type="button" class="btn btn-default btn-sm session-canceled">Cancel</button><button type="button" class="btn btn-link btn-sm discard">Discard</button>');

        //also need to register listeners on the new buttons
        $("button.session-moved").off('click', handleSessionMovedClicked).on('click', handleSessionMovedClicked);
        $("button.session-canceled").off('click', handleSessionCanceledClicked).on('click', handleSessionCanceledClicked);
        $("button.discard").off('click', handleDiscardClicked).on('click', handleDiscardClicked);
    };

    var handleDiscardClicked  = function(e) {
        $(this).parent().html('previous state depends on if already confirmed');
    };

    var handleYesClicked  = function(e) {

        if($(this).parent().prev().children().length > 0){
            //note: confirming a session date change will also run the confirm process
            console.log('session date changed');

            var newDate = $(this).parent().prev().find("input").val();
            var dayPretty = moment(newDate).format("dddd, MMMM Do YYYY");
            $(this).parent().prev().html(dayPretty);

            $(this).parent().parent().next(".details-box").html(confirmedByBrianSkinner);

            $(this).parent().html(checkMarkDetailsButton); 


        }else{
            console.log('session canceled');

            $(this).parent().parent().hide("slow");
            $(this).parent().parent().next().hide("slow");
        }

    };


    var handleSessionMovedClicked  = function(e) {
        $(this).parent().prev().html('<input type="text" class="form-control" value="07/14/2016">');

        $('.long-date input').datepicker({
            autoclose: true
        });
        $('.long-date input').datepicker('show');

        $('.long-date input').datepicker()
            .on('hide', function(e) {
                //show the 'Are you sure dialog'
                $(this).parent().next().html(confirmDiscardButtons);

                //put listeners on the buttons
                $("button.no-button").off('click', handleDiscardClicked).on('click', handleDiscardClicked);
                $("button.yes-button").off('click', handleYesClicked).on('click', handleYesClicked);

        });

        //should this discard be a different class than the other type of discard (on modify)?
        $(this).parent().next().html('<button type="button" class="btn btn-link btn-sm discard-button">Discard</button>');
    }

    var handleSessionCanceledClicked  = function(e) {
        console.log("session canceled");

        //show the 'Are you sure dialog'
        $(this).parent().html(confirmDiscardButtons);

        //put listeners on the buttons
        $("button.no-button").off('click', handleDiscardClicked).on('click', handleDiscardClicked);
        $("button.yes-button").off('click', handleYesClicked).on('click', handleYesClicked);
    };

    $("button.confirm").click(function(e) {        
        //show the details that were just created
        $(this).parent().parent().next().html(confirmedByBrianSkinner);

        //clear the parent html
        $(this).parent().html(checkMarkDetailsButton);

        //also need to register listeners on the new buttons
        $("button.modify").off('click', handleModifyClicked).on('click', handleModifyClicked);
    });

    $("button.session-moved").off('click', handleSessionMovedClicked).on('click', handleSessionMovedClicked);
    $("button.session-canceled").off('click', handleSessionCanceledClicked).on('click', handleSessionCanceledClicked);
    $("button.modify").off('click', handleModifyClicked).on('click', handleModifyClicked);


    $('#sandbox-container input').datepicker({
        autoclose: true
    });


/* pay-as-you-go vs pre-pay */
    $('.btn-group input').change(function() {
        var intValue = parseInt($(".total").html());

        if ($(this).attr('id') == 'pas-as-you-go') {
            console.log("Pay as you go selected");
            $(".total").html(intValue - 1170);
        }
        else if ($(this).attr('id') == 'prepay-for-10') {
            console.log("Prepay for 10 selected");
            $(".total").html(intValue + 1170);
        }

        $(".additional-10").toggleClass("toggled"); 
    });

/* billing / history button */

    $(".billing-history-button").click(function(e) {        
        if($(this).html().includes("History")){
            window.location.href = "payment_history.html";
        }else{
            window.location.href = "billing.html";
        }
    });

/* administrator pages */

    $(".dropdown-menu").on('click', 'li a', function(){
        $(".dropdown-toggle:first-child").html($(this).text()+' <span class="caret"></span>');
   });
