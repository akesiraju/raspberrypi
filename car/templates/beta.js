
var mDown = false;
var mouseX = -1;
var mouseY = -1;
var margin = 10;
var height = 512;
var width = 512;

function signal(v) {
    $.getJSON('http://192.168.2.18:5002/' + v, function (data) {
        h3 = document.getElementById('h3')
        h3.innerText = data['status'];
    });
}

function onMouseMove(e, isReverse) {
    if (mDown == true) {

        var x = e.clientX;
        var y = e.clientY;

        //move right
        if (x > mouseX + margin) {
            console.log('right');
            signal(261);
            mouseX = x;
        }

        //move left
        else if (x < mouseX - margin) {
            console.log('left');
            signal(260);
            mouseX = x;
        }
    }
}

function onMouseUp() {
    mDown = false;
    console.log('brakes');
    // break
    signal(32);
}



function onMouseDown(e, isReverse) {
    mouseX = e.clientX;
    mouseY = e.clientY;

    mDown = true;

    if (isReverse) {
        console.log('reverse');
        signal(258);
    }
    else {
        console.log('forward');
        signal(259);
    }

    // console.log('mouseDOwn ' + mouseDown+ ' at ' + mouseX+ ' - ' + mouseY);
}