// window.onscroll = ()=>{
//     if (window.scrollY > 50){
//         scroll = window.scrollY;
//         $("#header").addClass('hide');
//     }else if(window.scrollY > -50){
//         $("#header").removeClass('hide');
//     }
//     // if(document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
//     //     document.getElementById('header').style.top = "-4rem";
//     // }else if(document.body.scrollTop > -50 || document.documentElement.scrollTop > -50){
//     //     document.getElementById('header').style.top = "0";
//     // }else{
//     //     document.getElementById('header').style.top = "0";
//     // }
// }

// cancel button
const cancelBtn = ()=>{
    history.back();
}

// open  search bar
const openSearch = ()=>{
    closeMenu();
    document.getElementById('search-input').style.top = "4rem";
    document.getElementById('search-input').style.display = "block";
}

// close search bar
const closeSearch = ()=>{
    document.getElementById('search-input').style.top = "0";
    document.getElementById('search-input').style.display = "none";
    document.getElementById('suggestion').style.display = "none";
    document.getElementById('header-input').value ='';
}
// text suggest on input
const suggestText = ()=>{
    document.getElementById('suggestion').style.display = "block";
    console.log(document.getElementById('header-input').value);
}

// open menu 
const openMenu = ()=>{
    closeSearch();
    document.getElementById('menu-drawer').style.right = "0";
}
//close menu
const closeMenu = ()=>{
    document.getElementById('menu-drawer').style.right = "-70%";
}

// toggle parword view or hide 
const togglePassword = (eye)=>{
    if(eye){
        document.getElementById('password').type = 'text';
        document.getElementById('pass-eye').style.display = 'block';
    }else{
        document.getElementById('password').type = 'password';
        document.getElementById('pass-eye').style.display = 'none';
    }
}

// toggle password field for registration form
const toggleRegisterPassword = (eye)=>{
    if(eye){
        document.getElementById('reg-password').type = 'text';
        document.getElementById('reg-pass-eye').style.display = 'block';
    }else{
        document.getElementById('reg-password').type = 'password';
        document.getElementById('reg-pass-eye').style.display = 'none';
    }
}

// toggle confirm password field for registration form
const toggleRegisterConfirmPassword = (eye)=>{
    if(eye){
        document.getElementById('reg-conf-password').type = 'text';
        document.getElementById('conf-pass-eye').style.display = 'block';
    }else{
        document.getElementById('reg-conf-password').type = 'password';
        document.getElementById('conf-pass-eye').style.display = 'none';
    }
}

// checkout form add quantity 
function addQuantity(id, price){
    var quantity = document.getElementById(`product-${id}`);
    if(parseInt(quantity.value)>0){
        var amount = document.getElementById(`price-${id}`);
        quantity.value = ++quantity.value;
        amount.value = parseFloat(amount.value)+price;
    }
}
//  checkout form subtract quantity
function subQuantity(id, price){
    var quantity = document.getElementById(`product-${id}`);
    if(parseInt(quantity.value)>1){
        var amount = document.getElementById(`price-${id}`);
        quantity.value = --quantity.value;
        amount.value = parseFloat(amount.value) - price;
    }
}