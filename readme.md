# Common

This tool extracts the registered URL and other inventory in the wayback web archive, and also checks the activity status of the urls.


# Usage
Mode parameter takes 2 values, "active" or "passive". If you want to check the status of the URLs you collect from Web Archive, you should use the active value.

```
python3 wayback-checker.py --target <target.com> --mode active
```

```
python3 wayback-checker.py --target <target.com> --mode passive
```
