## How to reproduce the issue

```bash
$ cd _poetry_example
$ python --version
Python 3.8.2
$ poetry --version
Poetry version 1.0.5
$ poetry install
Creating virtualenv poetry-failure-repro in /home/colin/code/poetry-failure-repro/_poetry_example/.venv
Installing dependencies from lock file


Package operations: 1 install, 0 updates, 0 removals

  - Installing another-pkg (0.0.1 70126e5)
$ poetry install

[CalledProcessError]
Command '['git', '--git-dir', '/home/colin/code/poetry-failure-repro/_poetry_example/.venv/src/example-pkg/.git', '--work-tree', '/home/colin/code/poetry-failure-repro/_poetry_example/.venv/src/example-pkg', 'rev-parse', 'HEAD^{commit}']' returned non-zero exit status 128.
```
