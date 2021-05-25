$('.message span').click(function(){
$('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});

// $(document).ready(function(){
// 	$(".h").click(function(){
// 		$(".form-control").show(1000);
// 	})
// })


$('#owl-one').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    navText:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:2
        }
    }
})

owl = $('#owl-two')
  owl.owlCarousel({
    // center: true,
      // stagePadding: 30,
    loop: false,
    margin: 10,
    items: 2,
    dots : false,
    responsive: {
      0: {
        items: 1,
        navigation: true,
        nav: true,
        slideBy: 1 // <!-- HERE
      },
      640: {
        items: 5,
        navigation: true,
        nav: true,
        slideBy: 2 // <!-- HERE
      },
      1000: {
        items: 5,
        navigation: true,
        nav: true,
        slideBy: 2 
      }
    },
    scrollPerPage: true,
    navigation: true
  }).css("z-index", 0)

// $('#owl-two').owlCarousel({
//     loop:true,
//     margin:10,
//     nav:true,
//     dots:false,
//     navText: "<>",
//     responsive:{
//         0:{
//             items:1
//         },
//         600:{
//             items:3
//         },
//         1000:{
//             items:1
//         }
//     }
// })
$('#owl-three').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    // dots:false,
    // navText: "<>",
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

$('#owl-four').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    // dots:false,
    // navText: "<>",
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:1
        }
    }
})
$('#owl-five').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    // dots:false,
    // navText: "<>",
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:1
        }
    }
})
$('#owl-six').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    // dots:false,
    // navText: "<>",
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:1
        }
    }
})
$('#owl-seven').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    // dots:false,
    // navText: "<>",
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:1
        }
    }
})


