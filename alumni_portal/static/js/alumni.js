function achievements_show_hide()
{
	if (document.getElementById("achievements_show_hide").style.display=="none")
	{
		document.getElementById("achievements_show_hide").style.display="inline";
		document.getElementById("achievements_show_hide_btn").innerHTML = '-';
	}
	else
	{
		document.getElementById("achievements_show_hide").style.display="none";
		document.getElementById("achievements_show_hide_btn").innerHTML = '+';
	}
}