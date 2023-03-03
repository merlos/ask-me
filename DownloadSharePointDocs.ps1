#
# PowerShell script to download the contents of a sharepoint library
#
# Usage:
#  .\DownloadSharePointDocuments.ps1 -SiteUrl "https://<tenant-name>.sharepoint.com/sites/yoursite/"" 
#                                    -LibraryName "Library"
#                                    -DownloadFolder "./LibraryDocuments"
# # DownloadFolder must exist
#
# To run on OSX it is required to have pwsh
#
#     brew install pwsh
#
# After the package has been installed run
#
#     pwsh
#

Param(
    [Parameter(Mandatory=$true)]
    [string]$SiteUrl,

   
    [Parameter(Mandatory=$true)]
    [string]$LibraryName,


    [Parameter(Mandatory=$true)]
    [string]$DownloadFolder
)


# Check if the required PowerShell modules are installed
$modules = "PnP.PowerShell", "Microsoft.Online.SharePoint.PowerShell"
$installedModules = Get-Module -ListAvailable | Select-Object -ExpandProperty Name
foreach ($module in $modules) {
    if (-not $installedModules.Contains($module)) {
        Write-Host "Installing $module module..."
        Install-Module $module -Scope CurrentUser -Force
    }
}


Connect-PnPOnline -Url $SiteUrl -Interactive

# Get all the files in the library
$files = Get-PnPListItem -List $LibraryName


#(Get-PnPListItem -List $LibraryName).FieldValues | ConvertTo-Csv -NoTypeInformation | Out-File -FilePath "librarydata.csv"

# Convert the file information to a CSV
#$fileData = $files | Select-Object -Property Id, FileLeafRef, Size, Path, FileRef, ContentType, Created, Modified | ConvertTo-Csv -NoTypeInformation

# Save the CSV to a file
#$fileData | Out-File -FilePath "librarydata.csv"

# Download all the files in the specified folder
foreach ($file in $files) {
    # To download only files that are in English
    #$language = $file.FieldValues.Language
    #if( $language -ne "English") {
    #    Write-Host Skipping $file.FieldValues.FileLeafRef because language is $language
    #    continue
    #}
    $fileUrl = $file.FieldValues.FileRef
    $fileName = $file.FieldValues.FileLeafRef
    $filePath = $DownloadFolder + "\" + $fileName
    Write-Host "Downloading " $fileName "in " $filepath
    Get-PnPFile -Url $fileUrl -Path $DownloadFolder -FileName $fileName -AsFile
}
Disconnect-PnPOnline

