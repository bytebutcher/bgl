# bgl

bgl - make bash environment variables accessible between multiple terminals

## Usage

```
$ bgl export name1=value1
$ echo $name1
value1
$ bgl export name2=value2
$ echo $name2
value2
```

When opening a new terminal the exported variables can be used right away. 
```
$ echo $name1 $name2
value1 value2
```

To sync changes in an already opened terminal you need to issue the ```bgl reload``` command:
```
$ echo $name1 $name2

$ bgl reload
$ echo $name1 $name2
value1 value2
```

To unset exported variable and stop them from being updated when issuing ```bgl reload``` you can use the ```bgl unset``` command:
```
$ bgl unset name2
```

To distribute managed exports between computers you can use the result of the ```bgl list``` command:
```
$ bgl list
export name1=value1
```

## Installation
```
bash <(curl -s https://raw.githubusercontent.com/bytebutcher/bgl/master/install)
```

