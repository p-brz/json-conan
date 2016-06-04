# json-conan

[![badge](https://img.shields.io/badge/conan.io-json%2F1.0.0-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/json/1.0.0/paulobrizolara/stable) [Conan](https://conan.io/) package for [json](https://github.com/open-source-parsers/json) library.

The packages generated from this conanfile can be found on [conan.io](https://www.conan.io/source/json/1.0.0/paulobrizolara/stable).

See [conan docs](http://docs.conan.io/en/latest/) for detailed instructions in how to install conan and use it in your project.

For instructions about the library see [the repository](https://github.com/open-source-parsers/json).

## Quickstart

You can use the 'test_package' as a sample in how to use this library with conan or follow instructions below.

### Install conan.io

Detailed instructions [here](http://docs.conan.io/en/latest/installation.html)

Using [pip](https://pip.pypa.io/en/stable/installing/):

    pip install conan

### Create conan project

You can create a conanfile.txt like this:

    [requires]
    json/1.0.0@paulobrizolara/stable
    #you can include other libraries (search in conan.io)

    [options]

    [generators]
    #see http://docs.conan.io/en/latest/integrations.html for
    # others default generators. You can also search in conan.io
    # for 'community' generators or make your own.
    cmake

Another options is use a conanfile.py (that allows you use python
and build your project from conan). More info [here](http://docs.conan.io/en/latest/conanfile_py.html).

    from conans import ConanFile, CMake

    class PackageTest(ConanFile):
        settings = "os", "compiler", "build_type", "arch"

        # comma separated list of dependencies
        requires = "json/1.0.0@paulobrizolara/stable"
        generators = "cmake"
        default_options = ""


### Install dependencies

    conan install

### Integrate in your project

Depends on the generator (and build system) you are using.
See [integrations](http://docs.conan.io/en/latest/integrations.html) for examples and instructions.
