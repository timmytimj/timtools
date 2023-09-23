# MacPerlConfigManager

MacPerlConfigManager is a Perl script for configuring and managing MacOS user default settings. 

## Description

The script uses the `defaults read` command to retrieve all MacOS user defaults on your system, which are then parsed into a Perl data structure, sorted by domains. Each domain contains various keys and their corresponding values. The parsed user defaults are subsequently printed to the console for review.

## Dependencies

-  MacOS (with a Unix-based terminal)
-  Perl 5

## Usage

1. Ensure Perl 5 is installed on your MacOS system. 
2. Copy the script and save it to a file, e.g., `mac_config_manager.pl`
3. Apply the required execute permissions on the file:

    ```bash
    chmod +x mac_config_manager.pl
    ```

4. Run the script via Terminal:

    ```bash
    ./mac_config_manager.pl
    ```

The output will display all user defaults organized by domains and key-value pairs.

## Output

The console output is in the following format:

```
Domain: <domain1>
  <key>: <value>

Domain: <domain2>
  <key>: <value>
```

Each domain represents a specific collection of user defaults with corresponding keys and values.

## License

This project is license-free. You can use, modify, or distribute this script for any purpose.

---

**Note:** This script may produce extensive output data, especially on systems with a large number of user defaults. The process might take some time to complete, and the resulting output might be extensive. To alleviate this, consider filtering the output where necessary.

