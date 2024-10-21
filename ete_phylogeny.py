from ete3 import Tree, TreeStyle, NodeStyle, TextFace, AttrFace


def build_tree():

    tree = Tree('/maffted.fasta.treefile')
    return tree


def customize_tree(tree):

    ts = TreeStyle()
    ts.show_leaf_name = True

    treestyle=NodeStyle()
    treestyle["shape"]="square"
    for tree_element in tree.iter_leaves():
        tree_element.set_style(treestyle)

    
    #Clade Ia
    clade_Ia = tree.get_common_ancestor("PP601199.1", "JX878413.1")
    nstyle_cladeIa = NodeStyle()
    nstyle_cladeIa["bgcolor"] = "LightSteelBlue"
    label_clade_Ia = TextFace("Clade Ia", fsize=6, fgcolor="blue")
    clade_Ia.add_face(label_clade_Ia, column=0, position="branch-top")
    clade_Ia.set_style(nstyle_cladeIa)
    #Clade IIb
    clade_IIb = tree.get_common_ancestor("ON755039.1", "NC_063383.1")
    nstyle_cladeIIb= NodeStyle()
    nstyle_cladeIIb["bgcolor"]="DarkSeaGreen"
    label_clade_IIb=TextFace("Clade IIb",fsize = 6, fgcolor="green")
    clade_IIb.add_face(label_clade_IIb,column= 0 ,position="branch-top")
    clade_IIb.set_style(nstyle_cladeIIb)
    #Clade Ib
    clade_Ib=tree.get_leaves_by_name("PP601228.1")
    clade_Ib=clade_Ib[0]
    nstyle_cladeIb = NodeStyle()
    nstyle_cladeIb["bgcolor"] = "LightPink"
    label_clade_Ib = TextFace("Clade Ib", fsize=6, fgcolor="red")
    clade_Ib.add_face(label_clade_Ib, column=0, position="branch-top")
    clade_Ib.set_style(nstyle_cladeIb)

    return ts, tree


def prune_reroot_tree(tree,outgroup):
    tree.set_outgroup(tree&outgroup)
    leaf_names = tree.get_leaf_names()
    leaf_names.remove(outgroup)
    tree.prune(leaf_names)
    return tree

def draw_tree(tree,ts):
    tree.show(tree_style=ts)

# Main function to execute the workflow
def main():
    tree = build_tree()
    #Prune Vacv outgroup
    outgroup = "OP868847.1"
    tree = prune_reroot_tree(tree,outgroup)
    treestyle,tree = customize_tree(tree)
    draw_tree(tree,treestyle)

if __name__ == "__main__":
    main()
