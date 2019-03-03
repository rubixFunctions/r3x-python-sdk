import r3x
import json

def r3xFunc():
    res = {'message' : 'hello r3x'}
    json_res = json.dumps(res)
    print (json_res)
    return json_res

if __name__ == "__main__":  
    r3x.execute(r3xFunc)