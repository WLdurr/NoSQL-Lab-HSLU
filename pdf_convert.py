import os
import pypandoc
import tempfile

# jupyter nbconvert too latex (check gpt)

# Set the path to MiKTeX (adjust if necessary)
os.environ["PATH"] += r"path\to\MikTeX"

# Input and output file paths
input_file = 'wow_items.ipynb'  # Your Jupyter notebook
output_file = 'wow_analysis.pdf'  # Desired output PDF file name

# LaTeX preamble to customize text colors and code blocks
latex_preamble = r'''
\usepackage{xcolor}  % Allow colors
\usepackage{listings}  % Use listings package for code formatting
\definecolor{darkgray}{rgb}{0.5,0.5,0.5}  % Define a darker gray color
\definecolor{orange}{rgb}{1.0,0.647,0.0}
\lstset{
    backgroundcolor=\color{darkgray},  % Background color for code blocks
    basicstyle=\ttfamily,                % Use monospaced font for code
    frame=single,                        % Frame around the code
    rulesepcolor=\color{black},         % Color of the frame
    framesep=5pt,                       % Space between frame and code
    linewidth=\textwidth,               % Set the width of the code block
    xleftmargin=5pt,                    % Margin to the left
    xrightmargin=5pt,                   % Margin to the right
}
\setlength{\fboxsep}{5pt}  % Set the padding for the box
\newcommand{\fullwidthline}{\noindent\rule{\textwidth}{0.5pt}}

% Make section headers bold and larger
\renewcommand{\section}[1]{\textbf{\large #1}}  % Change \large to \Large or \LARGE for larger sizes
\renewcommand{\subsection}[1]{\textbf{\normalsize #1}}  % Change \normalsize to \large for larger sizes
\renewcommand{\subsubsection}[1]{\textbf{\normalsize #1}}  % Change \small to \normalsize for larger sizes

% Adjust paragraph spacing
\setlength{\parindent}{0pt}  % Remove indentation for paragraphs
\setlength{\parskip}{2em}  % Increase space between paragraphs
'''

# Create a temporary file for the LaTeX preamble
with tempfile.NamedTemporaryFile(delete=False, suffix='.tex') as preamble_file:
    preamble_file.write(latex_preamble.encode('utf-8'))
    preamble_file_path = preamble_file.name

# Convert the Jupyter notebook to PDF
output = pypandoc.convert_file(
    input_file,
    'pdf',
    outputfile=output_file,
    extra_args=[
        '--pdf-engine=xelatex',  # Use xelatex engine for custom fonts
        '--variable', 'geometry:margin=0.8in',  # Smaller margins
        '--variable', 'mainfont=Arial',  # Set the main font to Arial
        '--include-in-header', preamble_file_path,  # Include the LaTeX preamble from the temporary file
    ]
)

print("Conversion finished. Output saved as:", output_file)
