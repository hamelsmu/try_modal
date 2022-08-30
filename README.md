Let's try [modal](https://modal.com/home) for CI.

## Results

### Modal :fire: 7.25 Seconds :fire:
### GitHub Actions: 🕐 [3 Minutes](https://github.com/fastai/nbdev/actions/workflows/test.yaml) (at best) 🕥

Logs:

```
(modal) √ try_modal % time python test_nbdev.py                                                                                                          (main)try_modal
✓ Initialized.
✓ Created objects.
├── 🔨 Created ci.
├── 🔨 Mounted /Users/hamel/github/try_modal/test_nbdev.py.
└── 🔨 Mounted ./nbdev.
⠋ Running app...Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/01_config.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/02_maker.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/03_process.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/04a_export.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/05_sync.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/03_process.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/02_maker.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/05_sync.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/04b_doclinks.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/06_merge.ipynb
⠹ Running app...Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/08_showdoc.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/09a_frontmatter.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/06_merge.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/09b_processors.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/09a_frontmatter.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/04a_export.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/10_clean.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/11_test.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/12_cli.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/13_quarto.ipynb
⠸ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/13_quarto.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/14_qmd.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/14_qmd.ipynb
⠼ Running app...Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/15_migrate.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/08_showdoc.ipynb
⠴ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/01_config.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/12_cli.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/getting_started.ipynb
⠧ Running app...Starting /Users/hamel/github/try_modal/nbdev/nbs/09_API/17_release.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/04b_doclinks.ipynb
Starting /Users/hamel/github/try_modal/nbdev/nbs/migrating.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/migrating.ipynb
- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/17_release.ipynb
⠇ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/15_migrate.ipynb
⠏ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/10_clean.ipynb
⠋ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/11_test.ipynb
⠧ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/09_API/09b_processors.ipynb
⠙ Running app...- Completed /Users/hamel/github/try_modal/nbdev/nbs/getting_started.ipynb
Success.
✓ App completed.
python test_nbdev.py  7.29s user 1.39s system 105% cpu 8.254 total
````
