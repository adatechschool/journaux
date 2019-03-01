
function score(thing) {
    var a = 0; var b = 0;
    for (var i = 0; i < thing.length ; i++) {
        if (thing[i] == "j1") {
            a += 1;
        } else {
            b += 1;
        }
    }

    if (a == 1 ) {
        a = 15;
    } else if (a == 2) {
        a = 30;
    } else if (a == 3) {
        a = 40;
    }
    if (b == 1) {
        b = 15;
    } else if (b == 2) {
        b = 30;
    } else if (b == 3) {
        b = 40;
    }

    return { j1: a , j2: b };
}

console.log(score(["j1", "j2", "j1", "j1"]))
