# Python Topology
An easy-to-use module for dealing with topological data in python.

***

## Templates
Templates are used to define the attributes of the nodes and links in a topological space.

    template = Template('a', 'b', c=3)

In the code above, we create a new template called _template_, with attributes _a_, _b_, and _c_. The attributes _a_ and _b_ are both set to _None_ by default, while _c_ is set to _3_. 

Templates are dictionaries that instantiate python objects. The instantiated objects have the attributes stored within the template from which they were created.

## Objects
Objects are the actual nodes and links stored within a topological space.

    object = template(1, 2)

In the code above, we create a new object called _object_, which is instantiated from _template_. The attributes _a_ and _b_ are assigned to _1_ and _2_ respectively, while _c_ is assigned to _3_ by default. It is possible to overwrite the value of _c_, as well as to let _a_ and _b_ remain equal to _None_ by simply not providing different values when instantiating the object.

# Topological Spaces
Topological spaces are made up of nodes instantiated from node templates, and links between nodes instantiated from link templates. 
    
    space = Topology(
        node_template('position'),
        link_template('distance'))

In the code above, we create a new topological space called _space_, with a node template with attribute _position_ and link template with attribute _distance_. We instantiate node and link objects through _space_.

    space.create_node('a', position=(0,0))
    space.create_node('b', position=(0,5))

Here we create two nodes called _a_ and _b_. The node _a_ has a position of _(0,0)_ and _b_ has a position of _(0,5)_. 

    space.create_link('a', 'b', distance=5)
    
We now create a link between _a_ and _b_ with a distance of _5_, based on the positions of the nodes. If we would like to see the list of target nodes for _a_, we can do so through the following code:

    space.get_targets('a')

Which gives us _['b']_. We can also view the source nodes for _b_:

    space.get_sources('b')

Which gives us _['a']_. We can view the node objects directly through the following code:

    space.get_node('a')
    
As well as the link objects:

    space.get_link('a', 'b')
    
We can also remove nodes:

    space.remove_node('a')
    
As well as links:

    space.remove_link('a', 'b')
    
Any time a node is removed, every link associated with that node is also removed.
