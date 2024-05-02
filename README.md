# utilities

Random utilities and useful commands

```bash
# Outputting the entire git tree to txt file:
find . -type f -not -path '*/.git/*' -not -path '*/venv/*' > tree_all.txt

# Outputting only root paths to txt file:
find . -maxdepth 1 -type d > tree_root.txt
```
