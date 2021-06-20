BUILD_DIR=../js
SRC_DIR=python
COMPILER=transcrypt
COMPILER_FLAGS=-od ${BUILD_DIR}

build: build_index

build_index: ${SRC_DIR}/index.py
	${COMPILER} ${SRC_DIR}/index.py ${COMPILER_FLAGS}
