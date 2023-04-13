import jinja2
from jinja2 import Template
import os, time


# Jinja2 environment variables
latex_jinja_env_back = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('./templates/back'))
)


# Compile function
# def compile_latex(path_file,var1):
#     template = latex_jinja_env.get_template(path_file)
#     o = template.render(section1=var1)
#     with open('./pdf/front/test.tex', 'w') as f:
#         f.write(o)
#     os.chdir("./pdf/front")
#     os.system("pdflatex test.tex")