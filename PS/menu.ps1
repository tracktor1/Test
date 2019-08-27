$processes = Get-Process
$menu = @{}
for ($i=1;$i -le $processes.count; $i++) 
{ Write-Host "$i. $($processes[$i-1].name)"
$menu.Add($i,($processes[$i-1].name)) }

[int]$ans = Read-Host 'Enter selection'
$selection = $menu.Item($ans) ; Get-Process $selection
