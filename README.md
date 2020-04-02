# python-scripts

A collection of simple python3 scripts to automate boring repetitive stuff

## Installation

Run setup.py - python3 required

```bash
python3 setup.py
```

This will simply copy everything from the scripts folder to /usr/local/bin/

## mkrcp

### Simple script to create a new React Component folder and relative files

This will create:
<br>`./src/components/NewComponent/NewComponent.jsx`
<br>`./src/components/NewComponent/NewComponent.module.scss`
<br>`./src/components/NewComponent/package.json`

```bash
mkrcp NewComponent
```

Show help and list options

```bash
mkrcp -h
```

## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
