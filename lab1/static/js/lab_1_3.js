$(document).ready(function () {
    var player = {'clicks': 0};
    var turn = '';
    var finished_turn = [];
    var game_on = false;

    function reset_game() {
        game_on = false;
        if ($.inArray(finished_turn, finished_turn) === -1) {
            finished_turn.push(turn);
        }
        $('#player_turn').text('Next players turn');
        player['clicks'] = 0;
    }

    $(document).keyup(function (evt) {
        var player_id = String.fromCharCode(evt.keyCode);

        if (!game_on) {
            if ($.inArray(player_id, finished_turn) === -1) {
                turn = player_id;
                var dummy_player = $('#dummy_player').clone();
                dummy_player.find('.player').text('Player' + turn);
                dummy_player.find('#dummy_id').text(player['clicks']);
                dummy_player.find('#dummy_id').attr('id', 'p' + turn);
                $('.players').append(dummy_player);
                $('#player_turn').text(turn);
                setTimeout(reset_game, 10000);
                game_on = true;
            }

        } else {
            if (turn === player_id) {
                player['clicks']++;
                $('#p' + turn).text(player['clicks']);
            }

        }

    });

});