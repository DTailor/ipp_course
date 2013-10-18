$(document).ready(function () {
    var player1 = {'clicks': 0};
    var player2 = {'clicks': 0};
    var turn = 1;
    var finished_turn = [];
    var game_on = false;

    function reset_game() {
        game_on = false;
        if ($.inArray(finished_turn, finished_turn) === -1) {
            finished_turn.push(turn);
        }
        $('#player_turn').text('Next players turn');
        console.log(finished_turn)

    }


    $(document).keyup(function (evt) {
        if (!game_on) {
            if (evt.keyCode === 48) {
                if ($.inArray(2, finished_turn) === -1) {
                    turn = 2;
                    console.log('2');
                    game_on = true;
                    setTimeout(reset_game, 10000);

                }
            } else if (evt.keyCode === 49) {
                if ($.inArray(1, finished_turn) === -1) {
                    turn = 1;
                    game_on = true;
                    setTimeout(reset_game, 10000);


                }
            }


        } else {
            if (evt.keyCode === 48) { // 0 press
                if (turn === 2) {
                    player2['clicks']++;
                    $('#p2').text(player2['clicks']);
                    $('#player_turn').text(turn)
                }

            } else if (evt.keyCode === 49) { // 1 press
                if (turn === 1) {
                    player1['clicks']++;
                    $('#p1').text(player1['clicks']);
                    $('#player_turn').text(turn)
                }
            }
        }

    });

});