function show2()
{
    var value = document.getElementById("div4").style.display;
    if(value=="none")
    {
        document.getElementById("div4").style.display="block";
        document.getElementById("div6").style.display="none";
    }
    else
        document.getElementById("div4").style.display="none";
        document.getElementById("div6").style.display="block";
}