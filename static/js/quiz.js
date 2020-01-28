$(document).ready(function () {
    var question_number = 0;
    var q = {
        0: {
            'Q': 'How do you write "Hello World" in an alert box?',
            'pk': 0,
            'C': ['msg("Hello World");', 'alert("Hello World");', 'alertBox("Hello World");']
        },
        1: {
            'Q': 'Have you had any experience creating MLM-teams?',
            'pk': 1,
            'C': ['if (i == 5)', 'if i = 5 then', 'if i == 5 then']
        },
        2: {
            'Q': 'How does a FOR loop start?',
            'pk': 2,
            'C': ['for (i = 0; i <= 5)', 'for (i = 0; i <= 5; i++)', 'for i = 1 to 5']
        },
        3: {
            'Q': 'What is the correct way to write a JavaScript array?',
            'pk': 3,
            'C': ['var colors = "red", "green", "blue"', 'var colors = (1:"red", 2:"green", 3:"blue")', 'var colors = ["red", "green", "blue"]']
        }
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
                change_quiz(message)

            }, 600)
        }

        question_number++;
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
