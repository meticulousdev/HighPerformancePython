$ python setup.py build_ext --inplace                                                           de  15:30:50
running build_ext
building 'cdiffusion' extension
Warning: Can't read registry to find the necessary compiler setting
Make sure that Python modules winreg, win32api or win32con are installed.
C compiler: clang -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -fwrapv -O2 -Wall -fPIC -O2 -isystem /opt/homebrew/Caskroom/miniforge/base/envs/de/include -arch arm64 -fPIC -O2 -isystem /opt/homebrew/Caskroom/miniforge/base/envs/de/include -arch arm64

creating build
creating build/temp.macosx-11.0-arm64-3.9
compile options: '-I/opt/homebrew/Caskroom/miniforge/base/envs/de/lib/python3.9/site-packages/numpy/core/include -I/opt/homebrew/Caskroom/miniforge/base/envs/de/include/python3.9 -c'
extra options: '-O3 -std=c11 -Wall -p -pg'
clang: python_interface.c
clang: cdiffusion.c
clang: warning: argument unused during compilation: '-p' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-p' [-Wunused-command-line-argument]