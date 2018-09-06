from conan.packager import ConanMultiPackager
import copy
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager(archs = ["x86_64"], build_types = ["Release"])
    builder.add(settings={"arch": "x86_64", "build_type": "Release"})
    builder.run()
