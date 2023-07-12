"""This module defines an ASE interface to RSMD.

https://github.com/myrabiedermann/rsmd

Mainly intended to build input reaction files for RSMD from toml reaction files.

y.mabrouk@fz-juelich.de

"""


import toml

def rxn_to_str(rxn):
    ed = rxn["educts"]
    prod = rxn["products"]
    # no empty reaction
    assert len(ed) > 0
    assert len(prod) > 0
    out_str = f"{ed[0]}"
    for e in ed[1:]:
        out_str += f" + {e}"
    out_str += " -"
    if "rate" in rxn:
        # an optional entry
        out_str += f"[k = {rxn['rate']:0.1f}]"
    out_str += f"-> {prod[0]}"
    for e in prod[1:]:
        out_str += f" + {e}"
    return out_str

with open('reactions.toml', 'r') as f:
    d = toml.load(f)
    for name, rxn in d["reaction"].items():
        rxn_str = rxn_to_str(rxn)
        print(f"{name}:\n\t{rxn_str}")
    print(d)
        
def write_reactions():
    
    with open('reactions.toml', 'r') as f:
        d = toml.load(f)
    
    for name, rxn in d["reaction"].items():
        
        reactant_directive = '# molecule nr    molecule name   atom name   atom nr'
        reactant = rxn["educts"] 
        product_directive = '# molecule nr    molecule name   atom name   atom nr     origin->moleculeNr      origin->atomNr'
        product = rxn["products"]
        
        with open(name+'.reaction', 'w') as myfile:
            
            myfile.write('[name]' + '\n')
            myfile.write(name + '\n'*2)
            myfile.write('[reactants]' + '\n')
            myfile.write(reactant_directive + '\n')
            
            i = 0
            for m in reactant:
                i += 1
                j = 0
                for a in d["molecule"][m]["atoms"]:
                    j +=1
                    myfile.write('  {}              '.format(i)+m+'               '+a+'           {}'.format(j) + '\n')
            myfile.write('\n')
            myfile.write('[products]' + '\n')
            myfile.write(product_directive + '\n')
            
            i = 0
            for m in product:
                i += 1
                j = 0
                for a in d["molecule"][m]["atoms"]:
                    j +=1
                    myfile.write('{}              '.format(i)+m+'              '+a+'           \
                                    {}           1                       1'.format(j) + '\n')
            myfile.write('\n')
            myfile.write('[criteria]' + '\n'*2)
            myfile.write('[rate]' + '\n')
            
