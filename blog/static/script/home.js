function Star(btn) {
    let id = btn.id;
    id = id.substring(9);
    $.ajax({
        type:"POST",
        url: "star/",
        data:{
            id: id
        },
        success: function(data){
            if(btn.src.endsWith('8-64.png')){
                btn.src = '../static/blog/outline-star-64.png';
            }else{
                btn.src = '../static/blog/star-8-64.png';
            }
        }
    })
}
function Star2(btn) {
    let id = btn.id;
    id = id.substring(9);
    $.ajax({
        type:"POST",
        url: "../star/",
        data:{
            id: id
        },
        success: function(data){
            if(btn.src.endsWith('8-64.png')){
                btn.src = '../static/blog/outline-star-64.png';
            }else{
                btn.src = '../static/blog/star-8-64.png';
            }
        }
    })
}

function checkIfStarred() {
    let btns = document.getElementsByClassName('favBtn');
    for(let i=0; i<btns.length; i++){
        let btn = btns[i];
        let id = btn.id;
        id = id.substring(9);
        $.ajax({
            type:"POST",
            url: "checkifstarred/",
            data:{
                id: id
            },
            success: function(data){
                if(data == "False"){
                    btn.src = '../static/blog/outline-star-64.png';
                }else{
                    btn.src = '../static/blog/star-8-64.png';
                }
            }
        })
    }
}