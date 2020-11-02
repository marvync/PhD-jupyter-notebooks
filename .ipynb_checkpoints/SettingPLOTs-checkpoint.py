from matplotlib import rcParams
    
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['font.size'] = '10'
# rcParams['font.style'] = 'normal'
# rcParams['font.weight'] = 'medium'
# rcParams['pdf.fonttype'] = '42'

# rcParams['axes.autolimit_mode'] = 'round_numbers'
# rcParams['axes.xmargin'] = 0
# rcParams['axes.ymargin'] = 0
rcParams['axes.axisbelow'] = True

rcParams['axes.grid'] = True
rcParams['grid.linestyle'] = ':'
rcParams['grid.linewidth'] = 0.6
rcParams['grid.alpha'] = 0.3

# rcParams['lines.linewidth'] = 1

rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

rcParams['svg.fonttype'] = 'none'
# rcParams["figure.frameon"] = False
# rcParams['savefig.bbox'] = 'tight'
# rcParams['savefig.transparent'] = True

# rcParams["figure.figsize"] = [4, 3]
# rcParams['figure.autolayout'] = True

def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)
