if (A_IsAdmin = 0)
{
	try
	{
		if (A_IsCompiled)
		{
			Run *RunAs "%A_ScriptFullPath%" /restart
		}
		else
		{
			Run *RunAs "%A_AhkPath%" /restart "%A_ScriptFullPath%"
		}
	}
	ExitApp
}

Loop
{
	ControlFocus, Button1, make_file_x64 v1.5 ; Focus on the control
	ControlClick, Button1, make_file_x64 v1.5 ; Click the control
	Sleep, 10
}
return

F2::ExitApp