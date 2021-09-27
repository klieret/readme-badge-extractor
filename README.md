# Readme badge extractor

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/klieret/readme-badge-extractor/main.svg)](https://results.pre-commit.ci/latest/github/klieret/readme-badge-extractor/main)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License](https://img.shields.io/github/license/klieret/readme-badge-extractor.svg)](https://github.com/klieret/readme-badge-extractor/blob/main/LICENSE.txt)
[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

👆 These are called "badges"

👷 **This project is currently in early development, expect API ches** 👷

This repository provides

* a script/API to read a readme file like this one and extract all badges from it.
  The data is returned as a `NamedTuple` containing target url, image url and image alt text. This
  is similar to the objective of the [node-detect-readme-badges](https://github.com/IndigoUnited/node-detect-readme-badges)
  project (but here we're using python 🐍)
* a script/API that that includes badges from certain repositories into a HTML file,
  for example to create overview pages like [mine](https://lieret.net/opensource)
