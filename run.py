import yaml

with open('repos.yaml', 'r') as file:
    repos = yaml.safe_load(file)

template = """|
[`{repo_name}` ](https://github.com/{repo}/)
| [![](https://github.com/{repo}/actions/workflows/check.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/check.yaml?query=branch%3Amain)
| [![](https://github.com/{repo}/actions/workflows/docs.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/docs.yaml?query=branch%3Amain)
| [![](https://github.com/{repo}/actions/workflows/scheduled.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/scheduled.yaml?query=branch%3Amain)
| [![](https://raw.githubusercontent.com/{repo}/_xml_coverage_reports/data/main/badge.svg)](https://github.com/{repo})
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_winbinary&logo=windows&logoColor=white&label=r-universe)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_macbinary&logo=apple&logoColor=white&label=r-universe)](https://pharmaverse.r-universe.dev/{repo_name}/)
| [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F{repo_name}&query=_wasmbinary&logo=webassembly&logoColor=white&label=r-universe)](https://pharmaverse.r-universe.dev/{repo_name}/)
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
