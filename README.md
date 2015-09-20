# printable-binary-files
A short python script that creates a printable python script that when run recreates the original binary file.

Usage

Take the binary `example.png` file and create a printable python script `make-example-png.py`
```
python3 make-printable.py <example.png >make-example-png.py
```

Run the new python script and recreate the binary file, calling it example-new.png
```
python3  make-example-png.py > example-new.png
```
Verify the recreated file
```
diff -s example.png example-new.png 
Files example.png and example-new.png are identical
```
