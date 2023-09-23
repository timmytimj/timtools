on run argv
	set filePath to item 1 of argv
	set timestamp to (do shell script "date +%s")
	set folderName to timestamp as string
	
	set tmpPath to POSIX path of (path to home folder as string) & "tmp/"
	set newFolderPath to tmpPath & folderName
	
	do shell script "mkdir " & quoted form of newFolderPath
	set newFilePath to newFolderPath & "/" & (do shell script "basename " & quoted form of filePath)
	do shell script "cp " & quoted form of filePath & " " & quoted form of newFilePath
	
	set unrpaPath to "/usr/local/bin/unrpa"
	set args to "--silent --continue-on-error --path " & quoted form of newFolderPath & " " & quoted form of newFilePath
	
	do shell script unrpaPath & " " & args
	
	return newFolderPath
end run
