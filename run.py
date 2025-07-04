import yaml

with open('repos.yaml', 'r') as file:
    repos = yaml.safe_load(file)


r_release = "4.5.0"
r_devel = "4.6.0"
r_oldrel = "4.4"
r_wasm = "4.2.0"

template = """|
[`{repo_name}`](https://github.com/{repo}/)
| [![](https://github.com/{repo}/actions/workflows/check.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/check.yaml?query=branch%3Amain)
| [![](https://github.com/{repo}/actions/workflows/docs.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/docs.yaml?query=branch%3Amain)
| [![](https://github.com/{repo}/actions/workflows/scheduled.yaml/badge.svg?branch=main)](https://github.com/{repo}/actions/workflows/scheduled.yaml?query=branch%3Amain)
| [![](https://raw.githubusercontent.com/{repo}/_xml_coverage_reports/data/main/badge.svg)](https://github.com/{repo})
|
  [![]({shield_badge}{repo_name}&query=_jobs%5B0%5D.check&logo=linux&logoColor=white&label=R%2C{r_devel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B1%5D.check&logo=linux&logoColor=white&label=R%2C{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B2%5D.check&logo=apple&logoColor=white&label=R%2C{r_oldrel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B3%5D.check&logo=apple&logoColor=white&label=R%2C{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B4%5D.check&logo=R&logoColor=white&label=R%2C{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B5%5D.check&logo=webassembly&logoColor=white&label=R%2C{r_oldrel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B5%5D.check&logo=webassembly&logoColor=white&label=R%2C{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B6%5D.check&logo=windows&logoColor=white&label=R%2C{r_devel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B7%5D.check&logo=windows&logoColor=white&label=R%2C{r_oldrel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_jobs%5B8%5D.check&logo=windows&logoColor=white&label=R%2C{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)

|
  [![]({shield_badge}{repo_name}&query=_binaries%5B0%5D%5Bstatus%2Ccheck%5D&logo=linux&logoColor=white&label=R{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_binaries%5B4%5D%5Bstatus%2Ccheck%5D&logo=linux&logoColor=white&label=R{r_devel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_binaries%5B5%5D%5Bstatus%2Ccheck%5D&logo=linux&logoColor=white&label=R{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)

|
  [![]({shield_badge}{repo_name}&query=_binaries%5B1%5D%5Bstatus%2Ccheck%5D&logo=apple&logoColor=white&label=R{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_binaries%5B3%5D%5Bstatus%2Ccheck%5D&logo=apple&logoColor=white&label=R{r_oldrel})](https://pharmaverse.r-universe.dev/{repo_name}/)

|
  [![]({shield_badge}{repo_name}&query=_binaries%5B8%5D%5Bstatus%2Ccheck%5D&logo=windows&logoColor=white&label=R{r_oldrel})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_binaries%5B7%5D%5Bstatus%2Ccheck%5D&logo=windows&logoColor=white&label=R{r_release})](https://pharmaverse.r-universe.dev/{repo_name}/)
  <br>
  [![]({shield_badge}{repo_name}&query=_binaries%5B6%5D%5Bstatus%2Ccheck%5D&logo=windows&logoColor=white&label=R{r_devel})](https://pharmaverse.r-universe.dev/{repo_name}/)

|
  [![]({shield_badge}{repo_name}&query=_binaries%5B5%5D%5Bstatus%2Ccheck%5D&logo=webassembly&logoColor=white&label=R{r_wasm})](https://pharmaverse.r-universe.dev/{repo_name}/)
"""


no_columns = template.count('|')
columns = ["Repository", "Main check", "Main docs", "Main scheduled", "Main coverage", "Pharmaverse checks", "Linux binaries", "Mac binaries", "Windows binaries", "WebAssembly binaries"]
max_column_length = max(len(col) for col in columns)
columns_fixed = [col + "<br>" + "_" * max_column_length for col in columns] # this is to keep the column width fixed in the markdown table

table_header = "| " + " | ".join(columns_fixed) + " |\n" + "|:---:" * no_columns + "|\n"

res = table_header

for repo in repos:
    repo_name = repo.split('/')[1]
    repo_res = template.format(**{
      'shield_badge': "https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpharmaverse.r-universe.dev%2Fapi%2Fpackages%2F",
      'repo_name': repo_name,
      'repo' : repo,
      'r_devel' : r_devel, 'r_release' : r_release, 'r_oldrel' : r_oldrel,'r_wasm' : r_wasm
    })
    repo_res = repo_res.replace('\n', '')
    res = res + repo_res + "\n"

with open('README.md', 'w') as file:
    file.write(res)

