# ASF: Minimal directory and file bookmarking

ASF is a utility for easily finding directories and files you need often with as little syntax as possible.

## Installation

Assuming that you already have bash, curl and python3 installed, to install ASF run:

```sh
curl -s https://raw.githubusercontent.com/LucasIkuhara/asf/main/install.sh | sudo bash -s
```

## Usage

When inside a directory, you can create a shortcut by using the following command:

```sh
asf <shortcut-name>
```

from now on, whenever you enter this command, ASF will take you there!

To delete a shortcut, use:

```sh
asf -r <shortcut-name>
```

To list all current shortcuts, use:
```sh
asf -l
```
