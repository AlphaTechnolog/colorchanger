# Colorchanger - Transcrypt

A simple htmljs/js/python/css example using transcrypt to create a web
page using python as native javascript.

# Requirements

- [Transcrypt](https://github.com/QQuick/Transcrypt)
- [Node](https://nodejs.org)
- Yarn: `$ npm install -g yarn` (Optional)

# Getting started

## Cloning

```sh
mkdir -p ~/repo
cd ~/repo
git clone https://github.com/AlphaTechnolog/colorchanger.git
cd colorchanger
```

## Building python -> javascript

To build python to javascript, exists a Makefile:

**Note**: Make sure you have `transcrypt` installed.

```sh
make
```

The command `make` generate a `js` folder, it is the transpiled javascript
code.

## Running

To run install serve, to it, I known two ways:

### Npm

```sh
npm install -g serve
pwd # -> output: $HOME/repo/colorchanger
serve
```

### Yarn

```sh
yarn install -g serve
pwd # -> output: $HOME/repo/colorchanger
yarn exec serve
```

Yarn and npm with serve generate a local server in the port `5000`, go to
your web browser and type [http://localhost:5000](http://localhost:5000)
