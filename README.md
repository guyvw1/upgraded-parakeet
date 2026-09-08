# Analyse NESO Data from their API

The data comes from the [NESO Data Portal](https://www.neso.energy/data-portal),
free UK energy market data. No API key required.

This guide assumes you're on a Mac...

---

## 1. Open the Terminal

Press `Cmd` + `Space`, type `Terminal`, press `Enter`.

Copy each command below into it, press `Enter`, wait for it to finish, then move
to the next one. It doesn't matter what folder you start in.

---

## 2. Install Homebrew

Homebrew installs software from the Terminal.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

It will ask for your Mac password (nothing appears as you type)
and may ask to install Apple's Command Line Tools. Say yes.

At the end it may print a couple of `Next steps` commands; run those too, then
check it worked:

```bash
brew --version
```

---

## 3. Install the tools

```bash
brew install git                          # downloads and tracks code projects
brew install --cask visual-studio-code    # the editor you'll write code in
brew install python                       # the language itself
brew install uv                           # runs Python projects for you
```

Check they all installed:

```bash
git --version && python3 --version && uv --version
```

---

## 4. Get the code

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/guyvw1/upgraded-parakeet.git
cd upgraded-parakeet
code .
```

That downloads ("clones") the project and opens it in VS Code. If VS Code offers
to install the **Python** and **Jupyter** extensions, say yes.

---

## 5. Start with the notebook

The easiest way to see what the API data looks like is the notebook. It walks
through fetching the data, inspecting the response, loading it into a table,
and making a chart. Each step has its code and output together on the page.

## 6. What's in the repo

| File | What it is |
| --- | --- |
| `notebooks/api_data_exploration.ipynb` | **Start here.** The API walkthrough, run one cell at a time, and allows you to see the output. |
| `api_demo.py` | The same pipeline as one script: fetch data from the API, print it, load it into a table, and save a bar chart. |
| `pipeline.py` | The same thing, split into small functions. This is what typical Python code should look like. |
| `pyproject.toml` | The project's settings and its list of dependencies. |

Jargon:

- **API:** a URL you fetch data from. It returns structured data (JSON) instead of a web page.
- **Package:** code someone else wrote that this project uses. `httpx` fetches from the web, `pandas` handles tables, `matplotlib` draws charts.
- **Virtual environment (`.venv`):** a private folder holding this project's packages, so projects don't interfere with each other. `uv` creates it for you.

---

## 7. Set up and run

`uv` reads `pyproject.toml`, creates the virtual environment and downloads the
packages. Run in the VS Code or Mac terminal:

```bash
uv sync
```

Run the notebook first:

Open `notebooks/api_data_exploration.ipynb` it'll prompt you to Select Kernel in the top
right, choose **Python Environments** -> this project's `.venv`, then press
`Shift` + `Enter` to run each cell in turn.

Once you have seen the notebook, try the same workflow as a script. This is sometimes how Python code is presented, in a `.py` file rather than as `.ipynb` notebook.

```bash
uv run api_demo.py
```

You should see a record printed, the size of the table, the first five rows, and
a note that it saved `order_status.png`. Open that image from the file list on
the left of VS Code to see your chart.

Then try:

```bash
uv run pipeline.py
```

`pipeline.py` is more typical of what a production Python pipeline looks like - functions split out into modular functions, each function serving a specific purpose.

---

## 8. Making changes

Edit a file, save with `Cmd` + `S`, then re-run it with `uv run api_demo.py`.

Things to try in the notebook or `api_demo.py`:

- Change `"limit": 100` to `"limit": 5`; fewer rows come back.
- Add `print(df.columns)` to see every column name available.
- Print a single column: `print(df["status"])`.

### New exercise: explore another dataset

Use the code examples in the each file to read five records from this different NESO dataset:

[Open the API data](https://api.neso.energy/api/3/action/datastore_search?resource_id=7c0411cd-2714-4bb5-a408-adb065edf34d&limit=5)

Create a new notebook or `.py` file for this exercise. Use it to read in the
data, then analyse the data. Use `matplotlib` to create a new diagram.

- The URL already contains the dataset's `resource_id` and asks for five records.
- `httpx` can fetch the URL directly, or you can use the same `API_URL` and `params` pattern as the example.
- The response has the same broad shape as before: look inside `result`, then find the records.
- Load the records into a DataFrame and use `df.head()` and `df.columns` to discover what this dataset contains.

#### Bonus exercise

Using the info in the data portal [guidance](https://www.neso.energy/data-portal/api-guidance), return a list of all the datasets available via the NESO API (hint, look at the package_list endpoint.)

---

## Troubleshooting

- **`command not found: brew`:** reopen the Terminal, or run the `Next steps` commands Homebrew printed when it installed.
- **`command not found: code`:** in VS Code press `Cmd` + `Shift` + `P`, type `Shell Command: Install 'code' command in PATH`, press `Enter`.
- **`No such file or directory`:** you're in the wrong folder. Run `cd ~/Projects/upgraded-parakeet`.
- **An `httpx` error:** the API is probably down or you have no internet. Wait a minute and retry.
