Set-Alias -Name history -Value Get-History

Set-Alias -Name psconfig -Value {Start-Process "C:\ProgramData\chocolatey\bin\notepad++.exe" -ArgumentList $PROFILE}

$MaximumHistoryCount = 10000

Set-PSReadLineOption -PredictionSource History

Set-Alias -Name whereis -Value Get-Command -ErrorAction SilentlyContinue

function whereis {
    Get-Command $args[0] -ErrorAction SilentlyContinue | Select-Object -Property Name, Module, Path
}