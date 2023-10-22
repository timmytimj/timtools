# App Describer

This script, part of the `timtools` collection, fetches a brief description of any given macOS application using the OpenAI API. It then uses this description to update the Finder's headline and Comments section associated with the application.

## Installation

1. Clone the `timtools` repository to your local machine:

   ```bash
   git clone https://github.com/timmytimj/timtools.git
   ```

2. Navigate to the `scripts` directory:

   ```bash
   cd timtools/scripts
   ```

3. Make the script executable:

   ```bash
   chmod +x app_describer
   ```

4. (Optional) Add the `scripts` directory to your `$PATH` for easier access:

   ```bash
   echo 'export PATH=$PATH:/path/to/your/timtools/scripts' >> ~/.bashrc
   ```

   Replace `/path/to/your` with the actual path to the `timtools` directory. If you're using a shell other than bash, replace `~/.bashrc` with the configuration file of your shell (e.g., `~/.zshrc` for zsh).

## Prerequisites

1. A Bash or Zsh shell.
2. [jq](https://stedolan.github.io/jq/), a command-line JSON processor.
3. OpenAI API token.

Before running the script, please add your OpenAI API token to your environment variables:

```bash
export OPENAI_API_TOKEN=<Your OpenAI API token here>
```

## Usage

To run this script:

```bash
app_describer /Applications/YourApplication.app
```

Note: The script only works with `.app` applications.

The script extracts the Bundle ID from the selected application, prepares a prompt using the Bundle ID, and sends a request for a description to the OpenAI API. The script then uses the received description to update the Finder's headline and Comments field of the application.

## Limitations

This script is designed for macOS. It may not work as intended on other operating systems.

## License

This project is licensed under the MIT License - for more details, see the [LICENSE](https://github.com/timmytimj/timtools/blob/main/LICENSE) file.

## Author

(c) 2023 Timmytimj. [Github](https://github.com/timmytimj)

