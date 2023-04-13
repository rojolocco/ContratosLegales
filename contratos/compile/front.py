import jinja2
from jinja2 import Template
import os, shortuuid


# Jinja2 environment variables
latex_jinja_env_front = jinja2.Environment(
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
	loader = jinja2.FileSystemLoader(os.path.abspath('./templates/front'))
)


# Compile function
# def compile_latex(path_file,var1):
#     template = latex_jinja_env.get_template(path_file)
#     o = template.render(section1=var1)
#     with open('./pdf/front/test.tex', 'w') as f:
#         f.write(o)
#     os.chdir("./pdf/front")
#     os.system("pdflatex test.tex")


# Latex render front contracts
class FrontLatex():
    
    def create_F01012023(self,path_file,cdata):
        template = latex_jinja_env_front.get_template(path_file)
        jinja_render = template.render(section1=cdata)
        latex_path = f"./pdf/front"
        latex_file = f"F01012023-{shortuuid.uuid()}.tex"
        with open(latex_path+"/"+latex_file, 'w') as f:
            f.write(jinja_render)
        return (latex_path,latex_file)