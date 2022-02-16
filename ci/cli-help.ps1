<#
    Generate CLI help files from Click online help.
    These will get picked up by Sphinx.
 #>
# can i get the command list elsewhere?
$commands = @(
    "drape"
)

$dst = "$($PSScriptRoot)\..\docs\source\cli"
ForEach ($command in $commands)
{
    Write-Host "Writing help for $command"
    $path = Join-Path $dst cli.${command}.txt
    & ${command} --help | Out-File $path
}
