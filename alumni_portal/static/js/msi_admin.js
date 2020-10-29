function notice_show_hide()
{
	if (document.getElementById("notice_show_hide").style.display=="none")
	{
		document.getElementById("notice_show_hide").style.display="inline";
		document.getElementById("notice_show_hide_btn").innerHTML = '-';
	}
	else
	{
		document.getElementById("notice_show_hide").style.display="none";
		document.getElementById("notice_show_hide_btn").innerHTML = '+';
	}
}
function slideshow_show_hide()
{
	if (document.getElementById("slideshow_show_hide").style.display=="none")
	{
		document.getElementById("slideshow_show_hide").style.display="inline";
		document.getElementById("slideshow_show_hide_btn").innerHTML = '-';
	}
	else
	{
		document.getElementById("slideshow_show_hide").style.display="none";
		document.getElementById("slideshow_show_hide_btn").innerHTML = '+';
	}
}