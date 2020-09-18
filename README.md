# bgl 🥯

Make bash environment variables accessible between multiple terminals

## Setup
```
bash <(curl -s https://raw.githubusercontent.com/bytebutcher/bgl/master/install)
```

## Usage

```
bgl: bgl [option]
    manage global shell variables

    Options:
      <name=value ...>      export shell variable
      list                  list exports
      unset <name ...>      unset export
      reload                reload exports
      clear                 clear exports
      help                  display this help
```

## Examples
Use the ```bgl export``` command to export shell variables:
```
$ bgl export name1=value1
$ echo $name1
value1
```

To speed things up you can ommit the ```export``` argument and export multiple shell variables at once:
```
$ bgl name2=value2 name3=value3
$ echo $name2 $name3
value2 value3
```

When opening a new terminal the exported variables can be used right away. 
```
$ echo $name1 $name2 $name3
value1 value2 value3
```

To sync changes in an already opened terminal you need to issue the ```bgl reload``` command:
```
$ echo $name1 $name2 $name3

$ bgl reload
$ echo $name1 $name2 $name3
value1 value2 value 3
```

To unset exported variables you can use the ```bgl unset``` command:
```
$ bgl unset name2 name3
```

To distribute managed exports between computers you can use the result of the ```bgl list``` command:
```
$ bgl list
export name1=value1
```

To clear all exports managed by ```bgl``` use the ```bgl clear``` command:
```
$ bgl clear
```
