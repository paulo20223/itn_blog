$(document).ready(function () {
    var question_number = 0;
    var q = {
        0: {
            'Q': 'Have you had any experience creating MLM-teams?',
            'pk': 0,
            'C': ['Yes', 'No']
        },
        1: {
            'Q': 'How many active MLM-lines and people are on your team?\n',
            'pk': 1,
            'C': ['up to 100', 'from 100 to 500', 'from 500']
        },
        2: {
            'Q': 'Have you worked with investment projects (crypto)?',
            'pk': 2,
            'C': ['Yes', 'No']
        },
    };

    $("#answer").click(function () {

        $("#image-quiz").hide("slide", {direction: "left"}, 500);
        $("#started_dashboard").fadeOut(500);

        setTimeout(function () {

            $("#quiz_previous").show("slide", {direction: "left"}, 500);
            change_quiz()

        }, 500);

    });

    $(document).on("click", ".element-animation", function (event) {
        $('#quiz').fadeOut(400);

        let message = $(this).find("label").text();

        if ((question_number + 1) === Object.keys(q).length) {
            setTimeout(function () {
                let toAppend = '';

                $.each(q, function (i, a) {
                    toAppend += '<tr>';
                    toAppend += '<td>' + (i + 1) + '</td>';
                    toAppend += '<td>' + a.pk + '</td>';
                    toAppend += '<td>' + a.result + '</td>';
                    toAppend += '</tr>'
                });

                $('#quizResult').html(toAppend).show();
                $('#result-of-question').show();
                $('#graph-result').show();
            }, 600);
        } else {
            setTimeout(function () {
                change_quiz(message);
                question_number++;

            }, 600)
        }

    });

    function change_quiz(result = null) {
        if (result) {
            q[question_number].result = result;
        }

        $('#quiz').fadeIn(400);
        $('#question').html(q[question_number].Q);
        let questions = '';

        $.each(q[question_number].C, function (i, a) {
            questions += "<ul>\n" +
                "<li class='element-animation'>" +
                "<input type='radio' name='selector' value='" + a + "'>" +
                "<label for='f-option'>" + a + "</label>\n" +
                "<div class='check\'></div>\n" +
                "</li>" +
                "</ul>";
        });
        $('#questions').html(questions);
    }
});
