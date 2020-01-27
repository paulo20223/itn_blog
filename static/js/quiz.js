$(document).ready(function () {
    var question_number = 0;

    $("#answer").click(function () {

        $("#image-quiz").hide("slide", {direction: "left"}, 500);
        $("#started_dashboard").fadeOut(500);

        setTimeout(function () {

            $("#quiz_previous").show("slide", {direction: "left"}, 500);

        }, 500);

    });
});


function change_quiz(object, question_number) {
    q[question_number].result = $(object).parent().find('input:radio').val();
    $('input:radio').prop('checked', false);
    $('#questions').html();

    setTimeout(function () {
        $('#quiz').show();
        $('#question').html(q[question_number].Q);
        let questions = '';

        $.each(q[questionNo].C, function (i, a) {
            questions += "<ul>\n" +
                "<li>" +
                "<input type='radio' name='selector' value='" + a + "'>" +
                "<label for='f-option' class='element-animation'>" + a + "</label>\n" +
                "<div class='check\'></div>\n" +
                "</li>" +
                "</ul>";
        });
        $('#questions').html(questions);
    }, 600)
}

$(function () {


    var questionNo = 0;
    var q = {
        0: {'Q': 'Have you had any experience creating MLM-teams?', 'A': 3, 'C': ['Yes', 'No']},

        1: {
            'Q': 'How do you write "Hello World" in an alert box?',
            'A': 2,
            'C': ['msg("Hello World");', 'alert("Hello World");', 'alertBox("Hello World");']
        },
        2: {
            'Q': 'Have you had any experience creating MLM-teams?',
            'A': 1,
            'C': ['if (i == 5)', 'if i = 5 then', 'if i == 5 then']
        },
        3: {
            'Q': 'How does a FOR loop start?',
            'A': 2,
            'C': ['for (i = 0; i <= 5)', 'for (i = 0; i <= 5; i++)', 'for i = 1 to 5']
        },
        4: {
            'Q': 'What is the correct way to write a JavaScript array?',
            'A': 3,
            'C': ['var colors = "red", "green", "blue"', 'var colors = (1:"red", 2:"green", 3:"blue")', 'var colors = ["red", "green", "blue"]']
        }
    };


    $(document.body).on('click', "label.element-animation", function (e) {


        $('#quiz').hide(400);

        if ((questionNo + 1) === Object.keys(q).length) {
            alert("Quiz completed, Now click ok to get your answer");
            $('label.element-animation').unbind('click');
            setTimeout(function () {
                var toAppend = '';
                $.each(q, function (i, a) {
                    toAppend += '<tr>';
                    toAppend += '<td>' + (i + 1) + '</td>';
                    toAppend += '<td>' + a.A + '</td>';
                    toAppend += '<td>' + a.result + '</td>';
                    toAppend += '</tr>'
                });
                $('#quizResult').html(toAppend);
                $('#quizResult').show();
                // $('#loadbar').fadeOut();
                $('#result-of-question').show();
                $('#graph-result').show();
                chartMake();
            }, 600);
        } else {
            q[questionNo].result = $(this).parent().find('input:radio').val();
            $('input:radio').prop('checked', false);
            $('#questions').html();

            setTimeout(function () {
                $('#quiz').show();
                $('#question').html(q[questionNo].Q);
                let questions = '';

                $.each(q[questionNo].C, function (i, a) {
                    questions += "<ul>\n" +
                        "<li>" +
                        "<input type='radio' name='selector' value='" + a + "'>" +
                        "<label for='f-option' class='element-animation'>" + a + "</label>\n" +
                        "<div class='check\'></div>\n" +
                        "</li>" +
                        "</ul>";
                });
                $('#questions').html(questions);
            }, 600);

        }
        questionNo++;
    });


// chartMake();
    function chartMake() {

        var chart = AmCharts.makeChart("chartdiv",
            {
                "type": "serial",
                "theme": "dark",
                "dataProvider": [{
                    "name": "Correct",
                    "color": "#00FF00",
                    "bullet": "http://i2.wp.com/img2.wikia.nocookie.net/__cb20131006005440/strategy-empires/images/8/8e/Check_mark_green.png?w=250"
                }, {
                    "name": "Incorrect",
                    "color": "red",
                    "bullet": "http://4vector.com/i/free-vector-x-wrong-cross-no-clip-art_103115_X_Wrong_Cross_No_clip_art_medium.png"
                }],
                "valueAxes": [{
                    "maximum": q.length,
                    "minimum": 0,
                    "axisAlpha": 0,
                    "dashLength": 4,
                    "position": "left"
                }],
                "startDuration": 1,
                "graphs": [{
                    "balloonText": "<span style='font-size:13px;'>[[category]]: <b>[[value]]</b></span>",
                    "bulletOffset": 10,
                    "bulletSize": 52,
                    "colorField": "color",
                    "cornerRadiusTop": 8,
                    "customBulletField": "bullet",
                    "fillAlphas": 0.8,
                    "lineAlpha": 0,
                    "type": "column",
                }],
                "marginTop": 0,
                "marginRight": 0,
                "marginLeft": 0,
                "marginBottom": 0,
                "autoMargins": false,
                "categoryField": "name",
                "categoryAxis": {
                    "axisAlpha": 0,
                    "gridAlpha": 0,
                    "inside": true,
                    "tickLength": 0
                }
            });
    }
});
