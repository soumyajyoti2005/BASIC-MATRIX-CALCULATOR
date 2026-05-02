![Matrix Calculator Banner](banner.svg)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-00C897?style=flat-square&logo=streamlit&logoColor=white)](https://basic-matrix-calculator-iiqbrrumsqgvk7v9f3na7y.streamlit.app/)

</div>

---

## Overview

A sleek, browser-based **Matrix Calculator** built with Streamlit and NumPy. Define two matrices of any dimension, choose an operation, and get the result instantly — all wrapped in a custom dark cyberpunk UI with animated gradients and glowing panels.

---

## Features

- **Dynamic matrix input** — specify any number of rows and columns for both Matrix A and Matrix B
- **Three core operations** — Addition (`+`), Subtraction (`−`), and Multiplication (`×`)
- **Real-time computation** using NumPy under the hood
- **Custom dark UI** — animated gradient background, glowing panels, grid overlay, and monospace typography
- **Live result display** — result matrix rendered directly in the browser

---

## Demo

🔗 **[Open Live App](https://basic-matrix-calculator-iiqbrrumsqgvk7v9f3na7y.streamlit.app/)**

---

## Getting Started

### Prerequisites

```bash
python >= 3.9
streamlit
numpy
```

### Installation

```bash
# Clone the repository
git clone https://github.com/soumyajyoti2005/BASIC-MATRIX-CALCULATOR.git
cd BASIC-MATRIX-CALCULATOR

# Install dependencies
pip install streamlit numpy

# Run the app
streamlit run main.py
```

Or using `py`:

```bash
py -3.13 -m streamlit run main.py
```

---

## Usage

1. **Set dimensions** for Matrix A (rows × columns)
2. **Fill in values** for each cell
3. **Pick an operation** — `+`, `×`, or `−`
4. **Set dimensions** for Matrix B accordingly
5. Fill in Matrix B values and hit **Submit**
6. The result matrix appears below

> ⚠️ For multiplication, ensure columns of A equal rows of B.

---

## Project Structure

```
BASIC-MATRIX-CALCULATOR/
├── main.py        # Streamlit app — UI + logic
└── banner.svg     # README banner
```

---

## Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Frontend  | Streamlit + CSS     |
| Compute   | NumPy               |
| Language  | Python 3.13         |
| Deploy    | Streamlit Community Cloud |

---

## Author

**Soumyajyoti Ghosh** — [@soumyajyoti2005](https://github.com/soumyajyoti2005)

---

<div align="center">
<sub>// built with NumPy · Streamlit · Python //</sub>
</div>
