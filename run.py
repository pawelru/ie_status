import yaml

with open('repos.yaml', 'r') as file:
    repos = yaml.safe_load(file)

template = """|
[`{repo_name}` ](https://github.com/{repo}/)
| [![](https://github.com/{repo}/actions/workflows/check.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/check.yaml?query=branch%3Amain)
| [![](https://github.com/{repo}/actions/workflows/docs.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/docs.yaml?query=branch%3Amain)
| [![](https://github.com/{repo}/actions/workflows/scheduled.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/scheduled.yaml?query=branch%3Amain)
| [![](https://raw.githubusercontent.com/{repo}/_xml_coverage_reports/data/main/badge.svg)](https://github.com/{repo})
|
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_linuxdevel&logo=linux&logoColor=white&label=linuxdevel)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_macbinary&logo=apple&logoColor=white&label=macbinary)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_winbinary&logo=windows&logoColor=white&label=winbinary)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_windevel&logo=windows&logoColor=white&label=windevel)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_wasmbinary&logo=webassembly&logoColor=white&label=wasmbinary)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B0%5D%5Bstatus%2Ccheck%5D&logo=linux&logoColor=white&label=R4.5.0)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B1%5D%5Bstatus%2Ccheck%5D&logo=linux&logoColor=white&label=R4.4.1)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B2%5D%5Bstatus%2Ccheck%5D&logo=apple&logoColor=white&label=R4.3.3)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B3%5D%5Bstatus%2Ccheck%5D&logo=apple&logoColor=white&label=R4.4.1)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B7%5D%5Bstatus%2Ccheck%5D&logo=windows&logoColor=white&label=R4.3.3)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B8%5D%5Bstatus%2Ccheck%5D&logo=windows&logoColor=white&label=R4.4.1)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B6%5D%5Bstatus%2Ccheck%5D&logo=windows&logoColor=white&label=R4.5.0)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B4%5D%5Bstatus%2Ccheck%5D&logo=webassembly&logoColor=white&label=R4.3.3)](https://pharmaverse.r-universe.dev/{repo_name}/)
  [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_binaries%5B5%5D%5Bstatus%2Ccheck%5D&logo=webassembly&logoColor=white&label=R4.4.1)](https://pharmaverse.r-universe.dev/{repo_name}/)
"""

no_columns = template.count('|')
col_width = '_______________'
table_header = ("| " + col_width + " ") * no_columns + "|\n" + "|---" * no_columns + "|\n"

res = table_header

for repo in repos:
    repo_name = repo.split('/')[1]
    repo_res = template.format(**{'repo_name': repo_name, 'repo': repo})
    repo_res = repo_res.replace('\n', '')
    res = res + repo_res + "\n"

with open('README.md', 'w') as file:
    file.write(res)
