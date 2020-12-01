from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'AdafruitGFX'
    version = '1.10.3'
    url = 'https://github.com/hicktech/conan-AdafruitGFX'
    repo_url = 'https://github.com/adafruit/Adafruit-GFX-Library.git'
    generators = 'cmake'
    settings = []
    requires = ['AdafruitBusIO/1.6.0@hicktech/stable']

    def package(self):
        self.copy('*.c*', dst='src', excludes=['*examples*', '*fontconvert*'])
        self.copy('*.h*', dst='include', excludes=['*examples*', '*fontconvert*'])

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
