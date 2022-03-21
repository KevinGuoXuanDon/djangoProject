function show1()
// show liked states
{
    var value = document.getElementById("div3").style.display;
    if(value=="none")
    {
        document.getElementById("div3").style.display="block";
        document.getElementById("div5").style.display="none";
    }
    else
        document.getElementById("div3").style.display="none";
        document.getElementById("div5").style.display="block";
}