$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: 'bounceIn'
        },
        out:{
            effect: 'bounceOut'
        },

    });
    //siri configuration
     var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.15",
    autostart: true
  });

  // siri message animation

  $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: 'fadeInUp',
            sync: true,
        },
        out:{
            effect: 'fadeOutUp',
            sync: true,
        },

    });

    //mic buttomn click operation
    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });
});