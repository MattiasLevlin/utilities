# utilities

Random utilities and useful commands

## find

```bash
# Outputting the entire git tree to txt file:
find . -type f -not -path '*/.git/*' -not -path '*/venv/*' > tree_all.txt

# Outputting only root paths to txt file:
find . -maxdepth 1 -type d > tree_root.txt
```
## disable caps_lock on gnome desktop

```bash
gsettings set org.gnome.desktop.input-sources xkb-options "['caps:none']"
```
