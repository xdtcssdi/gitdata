$(function(){
    //无点击效果
    $('.menus li').each(function(){
        $('.menus li').mouseover(function(){
            var index = $(this).index();
            $('.menus .bg').css('left',(index-1)*150+'px');
            $('.menus li').css('color','#000');
            $(this).css('color','#ff4941');
        });
        $('.menus li').mouseout(function(){
            $('.menus li').css('color','#000');
            $('.menus .bg').css('left','0');
            $('.menus li').eq(0).css('color','#ff4941');
        });
    })
});
