window.onscroll = ()=>{
    if (window.scrollY > 50){
        scroll = window.scrollY;
        $("#header").addClass('hide');
    }else if(window.scrollY > -50){
        $("#header").removeClass('hide');
    }
    // if(document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
    //     document.getElementById('header').style.top = "-4rem";
    // }else if(document.body.scrollTop > -50 || document.documentElement.scrollTop > -50){
    //     document.getElementById('header').style.top = "0";
    // }else{
    //     document.getElementById('header').style.top = "0";
    // }
}

const openSearch = ()=>{
    closeMenu();
    document.getElementById('search-input').style.top = "4rem";
    document.getElementById('search-input').style.display = "block";
}
const closeSearch = ()=>{
    document.getElementById('search-input').style.top = "0";
    document.getElementById('search-input').style.display = "none";
    document.getElementById('suggestion').style.display = "none";
    document.getElementById('header-input').value ='';
}
const suggestText = ()=>{
    document.getElementById('suggestion').style.display = "block";
    console.log(document.getElementById('header-input').value);
}
const openMenu = ()=>{
    closeSearch();
    document.getElementById('menu-drawer').style.right = "0";
}
const closeMenu = ()=>{
    document.getElementById('menu-drawer').style.right = "-70%";
}
const togglePassword = (eye)=>{
    if(eye){
        document.getElementById('password').type = 'password';
        document.getElementById('pass-eye').style.display = 'none';
    }else{
        document.getElementById('password').type = 'text';
        document.getElementById('pass-eye').style.display = 'block';
    }
}