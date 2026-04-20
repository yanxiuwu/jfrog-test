from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.files import copy  # ✅ 必须导入

class MyDemoRecipe(ConanFile):
    name = "mydemo"
    version = "5.0.0"

    author = "yanxiuw"
    license = "MIT"
    description = "Demo package for Artifactory"

    requires = "fmt/10.2.1", "spdlog/1.12.0"
    exports_sources = "CMakeLists.txt", "main.cpp", "*.hpp"

    settings = "os", "compiler", "build_type", "arch"

    def generate(self):
        toolchain = CMakeToolchain(self)
        toolchain.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # ✅ Conan 2.x 正确写法
        copy(self, "*.hpp", self.source_folder, self.package_folder + "/include")
        copy(self, "*.a", self.build_folder, self.package_folder + "/lib")
        copy(self, "*.dylib", self.build_folder, self.package_folder + "/lib")

    def package_info(self):
        self.cpp_info.libs = ["mydemo"]
