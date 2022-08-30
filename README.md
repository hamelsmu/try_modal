Let's try [modal](https://modal.com/home) for CI.

## Results

### Modal :fire: 17 Seconds :fire:
### GitHub Actions: 🕐 [3 Minutes](https://github.com/fastai/nbdev/actions/workflows/test.yaml) (at best) 🕥

Logs:

```
(modal) √ try_modal % time python test_nbdev.py                                                                                                          (main)try_modal
✓ Initialized.
✓ Created objects.
├── 🔨 Created ci.
├── 🔨 Mounted /Users/hamel/github/try_modal/test_nbdev.py.
└── 🔨 Mounted ./nbdev.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
Starting /root/nbdev/nbs/09_API/03_process.ipynb
- Completed /root/nbdev/nbs/09_API/03_process.ipynb
Starting /root/nbdev/nbs/09_API/04b_doclinks.ipynb
- Completed /root/nbdev/nbs/09_API/04b_doclinks.ipynb
Starting /root/nbdev/nbs/09_API/11_test.ipynb
- Completed /root/nbdev/nbs/09_API/11_test.ipynb
Starting /root/nbdev/nbs/migrating.ipynb
- Completed /root/nbdev/nbs/migrating.ipynb
Starting /root/nbdev/nbs/09_API/04a_export.ipynb
- Completed /root/nbdev/nbs/09_API/04a_export.ipynb
Starting /root/nbdev/nbs/09_API/06_merge.ipynb
- Completed /root/nbdev/nbs/09_API/06_merge.ipynb
Starting /root/nbdev/nbs/09_API/09a_frontmatter.ipynb
- Completed /root/nbdev/nbs/09_API/09a_frontmatter.ipynb
Starting /root/nbdev/nbs/09_API/09b_processors.ipynb
- Completed /root/nbdev/nbs/09_API/09b_processors.ipynb
Starting /root/nbdev/nbs/09_API/01_config.ipynb
- Completed /root/nbdev/nbs/09_API/01_config.ipynb
Starting /root/nbdev/nbs/09_API/10_clean.ipynb
- Completed /root/nbdev/nbs/09_API/10_clean.ipynb
Starting /root/nbdev/nbs/09_API/15_migrate.ipynb
- Completed /root/nbdev/nbs/09_API/15_migrate.ipynb
Starting /root/nbdev/nbs/09_API/02_maker.ipynb
- Completed /root/nbdev/nbs/09_API/02_maker.ipynb
Starting /root/nbdev/nbs/09_API/05_sync.ipynb
- Completed /root/nbdev/nbs/09_API/05_sync.ipynb
Starting /root/nbdev/nbs/09_API/08_showdoc.ipynb
- Completed /root/nbdev/nbs/09_API/08_showdoc.ipynb
Starting /root/nbdev/nbs/09_API/12_cli.ipynb
- Completed /root/nbdev/nbs/09_API/12_cli.ipynb
Starting /root/nbdev/nbs/09_API/13_quarto.ipynb
- Completed /root/nbdev/nbs/09_API/13_quarto.ipynb
Starting /root/nbdev/nbs/09_API/14_qmd.ipynb
- Completed /root/nbdev/nbs/09_API/14_qmd.ipynb
Starting /root/nbdev/nbs/09_API/17_release.ipynb
- Completed /root/nbdev/nbs/09_API/17_release.ipynb
Starting /root/nbdev/nbs/getting_started.ipynb
- Completed /root/nbdev/nbs/getting_started.ipynb
Success.
✓ App completed.
python test_nbdev.py  0.75s user 0.14s system 5% cpu 16.538 total
````
