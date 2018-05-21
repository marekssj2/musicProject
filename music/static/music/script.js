var CurAudio = new Audio()
function StopAudio(){
  CurAudio.pause();
  CurAudio.currentTime = 0;
//  var icon = $(this).find('.playIcon')
  $('.playIcon').removeClass('fa-pause');
  $('.playIcon').addClass('fa-play');
  console.log("stop Audio");
  
}

$(document).ready(function() {
  $(".audioPlayer").click(function () {
    var icon = $(this).find('.playIcon')//class
    if(icon.hasClass('fa-pause')){
      StopAudio()
    }else {
      StopAudio()
      audio = new Audio($(this).attr("src"))
      // audio = new Audio(' /media/music/Breaking%20Benjamin/Egypt_Central_-_White_Rabbit_Lyrics.mp3')
      CurAudio = audio;
  //    alert('myClass');
      if(icon.hasClass('fa-play')){
        icon.removeClass('fa-play');
        icon.addClass('fa-pause');
        audio.play();
      }else{
        icon.removeClass('fa-pause');
        icon.addClass('fa-play');
      }
    }
  });
});

// $("#audioPlayer").click(function () {
//   console.log('click');
//   var addressValue = $(this).attr("href");
//   alert(addressValue );
//   var myClass = $(this).attr("class");
//   alert(myClass);

// });
