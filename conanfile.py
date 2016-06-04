from conans import ConanFile, ConfigureEnvironment
from conans import tools
import platform, os, sys
from os import path

class JsonConan(ConanFile):
    name = "json"
    version = "1.0.0"
    license="MIT"
    #Header only
    settings = None

    #Url of conan repository
    url="https://github.com/paulobrizolara/json-conan.git"

    #Source repository
    REPO = "https://github.com/open-source-parsers/json/"

    #Release info
    VERSION = "1.0.0"
    ZIPNAME = "v%s" % VERSION
    DIRNAME = "json-%s" % VERSION
    SOURCE_URL = REPO + "archive/" + ZIPNAME

    def source(self):
        #Adapted from conanfile in https://github.com/lasote/conan-boost
        ext = ".zip" if sys.platform.startswith("win") else ".tar.gz"
        zip_url = self.SOURCE_URL + ext
        zip_name = self.ZIPNAME + ext

        self.output.info("Downloading %s..." % zip_url)

        tools.download(zip_url, zip_name)
        tools.unzip(zip_name, ".")
        os.unlink(zip_name)

    def build(self):
        pass

    def package(self):
        #Copy all install dir content to the package directory
        self.copy("json.hpp",
                    src=path.join(self.DIRNAME, "src"),
                    dst=path.join(".", "include"))

    def package_info(self):
        #Require c++11
        self.cpp_info.cppflags = ['-std=c++11']
