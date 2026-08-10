from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

DOCS = [
    ("01_期末备考讲义.md", "01_期末备考讲义.tex", "01_期末备考讲义.pdf"),
    ("02_高频题库与预测卷.md", "02_高频题库与预测卷.tex", "02_高频题库与预测卷.pdf"),
    ("03_期末备考详细自学讲义.md", "03_期末备考详细自学讲义.tex", "03_期末备考详细自学讲义.pdf"),
]


def escape_latex(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def code_latex(text: str) -> str:
    escaped = text.replace("\\", r"\textbackslash{}")
    escaped = escaped.replace("}", r"\}").replace("{", r"\{")
    return r"\code{\detokenize{" + escaped + "}}"


def convert_bold(text: str) -> str:
    out: list[str] = []
    pos = 0
    for match in re.finditer(r"\*\*(.+?)\*\*", text):
        out.append(escape_latex(text[pos : match.start()]))
        out.append(r"\textbf{" + escape_latex(match.group(1)) + "}")
        pos = match.end()
    out.append(escape_latex(text[pos:]))
    return "".join(out)


def inline_latex(text: str) -> str:
    parts = re.split(r"(`[^`]*`|\$[^$]+\$)", text)
    out: list[str] = []
    for part in parts:
        if part.startswith("`") and part.endswith("`"):
            code = part[1:-1]
            if looks_like_math_code(code):
                out.append("$" + mathify_code(code) + "$")
            else:
                out.append(code_latex(code))
        elif part.startswith("$") and part.endswith("$"):
            out.append(part)
        else:
            out.append(convert_bold(part))
    return "".join(out)


def looks_like_math_code(text: str) -> bool:
    if any(ext in text for ext in (".md", ".pdf", ".py", ".tex", ".txt", ".csv")):
        return False
    if any(mark in text for mark in ("\\", "^", "_", "||", "<", ">", "{", "}", "=")):
        return True
    if re.search(r"\b(rho|omega|alpha|beta|lambda|mu|Sigma)\b", text):
        return True
    return False


def mathify_code(text: str) -> str:
    replacements = {
        "rho": r"\rho",
        "omega": r"\omega",
        "alpha": r"\alpha",
        "beta": r"\beta",
        "lambda": r"\lambda",
        "mu": r"\mu",
        "Sigma": r"\Sigma",
        "ρ": r"\rho",
        "ω": r"\omega",
        "α": r"\alpha",
        "β": r"\beta",
        "λ": r"\lambda",
        "μ": r"\mu",
        "Σ": r"\Sigma",
    }
    result = text.replace("±", r"\pm ")
    result = result.replace("||", r"\|")
    for plain, latex in replacements.items():
        if plain.isascii():
            result = re.sub(rf"\b{plain}\b", lambda _m, value=latex: value, result)
        else:
            result = result.replace(plain, latex)
    return result


def heading_text(text: str) -> str:
    return escape_latex(text.replace("`", ""))


def close_list(out: list[str], list_env: str | None) -> str | None:
    if list_env:
        out.append(r"\end{" + list_env + "}")
    return None


def mermaid_summary() -> list[str]:
    return [
        r"\begin{quote}",
        r"\textbf{知识主线：}",
        r"\begin{itemize}",
        r"\item 线性方程组 $Ax=b$：LU/PLU、Cholesky/$LDL^T$、追赶法。",
        r"\item 最小二乘：正则方程、QR 分解、Householder 变换。",
        r"\item 迭代法：Jacobi、Gauss-Seidel、SOR、共轭梯度法。",
        r"\item 特征值：幂法、Hessenberg 化、QR 方法、Schur 分解、SVD。",
        r"\item 误差与范数：向量/矩阵范数、条件数、扰动估计。",
        r"\end{itemize}",
        r"\end{quote}",
    ]


def convert_markdown(md_text: str) -> tuple[str, str]:
    lines = md_text.splitlines()
    title = "数值代数期末备考材料"
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    out: list[str] = []
    list_env: str | None = None
    in_math = False
    math_buf: list[str] = []
    in_code = False
    code_lang = ""
    code_buf: list[str] = []

    for line in lines:
        stripped = line.strip()

        if in_code:
            if stripped.startswith("```"):
                if code_lang == "mermaid":
                    out.extend(mermaid_summary())
                else:
                    out.append(r"\begin{verbatim}")
                    out.extend(code_buf)
                    out.append(r"\end{verbatim}")
                in_code = False
                code_lang = ""
                code_buf = []
            else:
                code_buf.append(line)
            continue

        if stripped.startswith("```"):
            list_env = close_list(out, list_env)
            in_code = True
            code_lang = stripped[3:].strip()
            code_buf = []
            continue

        if in_math:
            math_buf.append(line)
            if stripped == r"\]":
                in_math = False
                out.append("\n".join(math_buf))
                math_buf = []
            continue

        if stripped == r"\[":
            list_env = close_list(out, list_env)
            math_buf = [line]
            in_math = True
            continue

        if not stripped:
            continue

        if stripped == "---":
            list_env = close_list(out, list_env)
            out.append(r"\bigskip\hrule\bigskip")
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            list_env = close_list(out, list_env)
            level = len(heading.group(1))
            text = heading_text(heading.group(2))
            if level == 1:
                continue
            if level == 2:
                out.append(r"\phantomsection")
                out.append(r"\section*{" + text + "}")
                out.append(r"\addcontentsline{toc}{section}{" + text + "}")
            elif level == 3:
                out.append(r"\phantomsection")
                out.append(r"\subsection*{" + text + "}")
                out.append(r"\addcontentsline{toc}{subsection}{" + text + "}")
            else:
                out.append(r"\subsubsection*{" + text + "}")
            continue

        unordered = re.match(r"^-\s+(.*)$", stripped)
        if unordered:
            if list_env != "itemize":
                list_env = close_list(out, list_env)
                out.append(r"\begin{itemize}")
                list_env = "itemize"
            out.append(r"\item " + inline_latex(unordered.group(1).rstrip()))
            continue

        ordered = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ordered:
            if list_env != "enumerate":
                list_env = close_list(out, list_env)
                out.append(r"\begin{enumerate}")
                list_env = "enumerate"
            out.append(r"\item " + inline_latex(ordered.group(1).rstrip()))
            continue

        list_env = close_list(out, list_env)
        out.append(inline_latex(stripped.rstrip()))

    close_list(out, list_env)
    return title, "\n\n".join(out)


def latex_document(title: str, body: str) -> str:
    escaped_title = escape_latex(title)
    return rf"""\documentclass[11pt,a4paper]{{ctexart}}
\usepackage{{amsmath,amssymb,mathtools,bm}}
\usepackage{{geometry}}
\usepackage{{enumitem}}
\usepackage{{hyperref}}
\usepackage{{xcolor}}
\usepackage{{fancyhdr}}
\usepackage{{titlesec}}
\usepackage{{booktabs,longtable,array}}

\geometry{{left=2.05cm,right=2.05cm,top=2.0cm,bottom=2.2cm}}
\setmonofont{{Consolas}}
\hypersetup{{
  colorlinks=true,
  linkcolor=blue!45!black,
  urlcolor=blue!45!black,
  citecolor=blue!45!black,
  pdftitle={{{escaped_title}}},
  pdfauthor={{Codex}}
}}
\setlist{{nosep,leftmargin=2em}}
\allowdisplaybreaks
\sloppy
\pagestyle{{fancy}}
\setlength{{\headheight}}{{14pt}}
\fancyhf{{}}
\fancyhead[L]{{数值代数期末备考}}
\fancyhead[R]{{{escaped_title}}}
\fancyfoot[C]{{\thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\newcommand{{\code}}[1]{{\begingroup\ttfamily\small #1\endgroup}}
\titlespacing*{{\section}}{{0pt}}{{1.4em}}{{0.5em}}
\titlespacing*{{\subsection}}{{0pt}}{{1.0em}}{{0.35em}}
\titlespacing*{{\subsubsection}}{{0pt}}{{0.8em}}{{0.25em}}

\title{{\bfseries {escaped_title}}}
\author{{基于历年卷、非上机作业与课程讲义整理}}
\date{{2026年6月26日}}

\begin{{document}}
\maketitle
\tableofcontents
\newpage

{body}

\end{{document}}
"""


def build_doc(md_name: str, tex_name: str, pdf_name: str) -> None:
    md_path = ROOT / md_name
    tex_path = ROOT / tex_name
    pdf_path = ROOT / pdf_name
    title, body = convert_markdown(md_path.read_text(encoding="utf-8"))
    tex_path.write_text(latex_document(title, body), encoding="utf-8")

    for _ in range(2):
        subprocess.run(
            [
                "xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_path.name,
            ],
            cwd=ROOT,
            check=True,
        )
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)


def main() -> int:
    try:
        for doc in DOCS:
            build_doc(*doc)
    except subprocess.CalledProcessError as exc:
        print(f"LaTeX failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
