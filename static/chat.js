var socket;
$(document).ready(function(){
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat/io');

    socket.on('message', function(data) {
        $('#chat').val($('#chat').val() + data.message + '\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });

    $('#text').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code == 13 && $('#text').val() != '') {
            message = $('#text').val();
            user = $('#user').val();
            $('#text').val('');
            socket.emit('message', {user: user, message: message});
        }
    });
});
