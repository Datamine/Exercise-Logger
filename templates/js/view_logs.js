function populate_logs (){
    $.get({
        url: '/api/request_logs',
        success: function (response) {
            console.log(response);
            $("#exercise-logs").append(response);
            $.each(response, function (date, list_of_exercises) {
                $.each(list_of_exercises, function (exercise_row) {
                    console.log(exercise_row)
                    $("#exercise-logs").append(
                        '<div class="log-line">'  + '</div>'
                    );
                });
            });
        },
    });
}

$(document).ready(function (){
    populate_logs();
});
