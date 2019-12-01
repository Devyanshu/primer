## pip
##### By @[Devyanshu](https://github.com/Devyanshu)

pip is the standard package installer and manager that comes included with newer versions of Python (3.4+). It allows users to install and manage third-party packages from [Python Package Index (PyPI)](https://pypi.org/). Though Python comes with a lot of libraries out of the box, it is often required to install other libraries from PyPI's 200, 000+ collection of community shared packages.

``` pip install <package-name>```

pip also helps a lot in managing dependecies when using third-party libraries, it ensures the version of the libraries is same so that you can replicate the environment on other machines.

``` pip install requests>=2.1.0```

This indicates pip to install version of the requests library newer or equal to 2.1.0 i.e , the latest version after 2.1.0 will be installed, if 2.1.0 is the latest version, it will be insatlled.



It is a common practice to use ```requirements.txt``` to list the packages with their exact version so that it can be replicated.

``` pip freeze > requirements.txt```

Further reads
- [What is pip?](https://realpython.com/what-is-pip/)
- [Wikipedia: pip](https://en.wikipedia.org/wiki/Pip_(package_manager))