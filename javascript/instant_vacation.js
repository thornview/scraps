$('#vacation').on('click', function(){
    var videos = [
        'http://www.youtube.com/v/qREKP9oijWI&autoplay=1', //palm tree,
        'http://www.youtube.com/v/fIlJyZEbrzo&autoplay=1', //waterfall beach,
        'http://www.youtube.com/v/_ziUhNerFMI&autoplay=1', // sunset waves,
        'http://www.youtube.com/v/BDFSj_MIPis&autoplay=1', // montana falls,
        'http://www.youtube.com/v/njCDZWTI-xg&autoplay=1', // ISS,
        'https://www.youtube.com/v/Q9j1B4z9b1Y&autoplay=1' // Beast,
    ];

    var video = videos[Math.floor(Math.random() * videos.length)];
    var windowFeatures = "menubar=no,location=no,resizable=yes,toolbar=no,height=850,width=1500";
    window.open(video, 'InstantVacation', windowFeatures);

});
