var cb = 0;
var cbtext = ['Coffee Break', 'End Coffee Break'];
$('#disappear').on('click', function(){
    $('.content').fadeToggle(1000);
    if (cb == 0) {
        cb = 1;
    } else {
        cb = 0;
    }
    $('#cbtext').html(cbtext[cb]);
});