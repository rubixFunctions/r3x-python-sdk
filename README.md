# RubiX Python SDK
[![CircleCI](https://circleci.com/gh/rubixFunctions/r3x-python-sdk.svg?style=svg)](https://circleci.com/gh/rubixFunctions/r3x-python-sdk)
[![License](https://img.shields.io/badge/-Apache%202.0-blue.svg)](https://opensource.org/s/Apache-2.0)

## Usage
Install Package from PyPi
```
$ python -m pip install --index-url https://test.pypi.org/project/r3x-python-sdk/ --no-deps r3x-python-sdk   
```
With the package installed, import `r3x`. Once imported define a function which returns a `JSON` response. Your function will receive the request body as a json parameter. Finally pass your function to `r3x.execute(your_func)`. The following is an example of using the SDK
```
import r3x
import json

def r3xFunc(input):
    i = json.loads(input)
    for key,value in i.items():
        if str(key) == "name":
            res = {"message": "hello {}".format(value)}
        else:
            res = {"message" : "hello r3x"}
    json_res = json.dumps(res)
    return json_res

if __name__ == "__main__":  
    r3x.execute(r3xFunc)
```
To run locally you will need to set an environment variable for the `PORT`
```
$ export PORT=8080
```
Once done, execute your code.

## Documentation
For full information on how to use the SDK and deploy a function to Knative, refer to our [Documentation here.](https://github.com/rubixFunctions/r3x-docs/blob/master/README.md)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details