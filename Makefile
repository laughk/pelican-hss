# Install using:
#
#   pip install pygments
#
# built in styles: ['monokai', 'manni', 'rrt', 'perldoc', 'borland', 'colorful',
# 'default', 'murphy', 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs',
# 'vim', 'pastie', 'friendly', 'native']

STYLE = default

pygments:
	pygmentize -S ${STYLE} -f html -a ".highlight pre" > ./static/css/pygments.css

gen_css:
	sassc --style compressed ./static/css/style.scss ./static/css/style.min.css
