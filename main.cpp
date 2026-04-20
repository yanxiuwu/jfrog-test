#include <fmt/core.h>
#include <spdlog/spdlog.h>

int main() {
    fmt::print("Hello Conan + fmt!\n");
    fmt::print("Hello Yan + fmt!\n");
    spdlog::info("Hello spdlog!");
    return 0;
}
