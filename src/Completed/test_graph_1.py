"""Test for first Graph data structure."""
import pytest
from graph_1 import Graph


@pytest.fixture
def empty_graph():
    """Return an empty graph."""
    return Graph()


@pytest.fixture
def one_node_graph():
    """Return a graph with one node."""
    g = Graph()
    g.add_node('corn')
    return g


@pytest.fixture
def two_node_no_edge_graph():
    """Return a graph with two nodes and no edges."""
    g = Graph()
    g.add_node('corn')
    g.add_node('beans')
    return g


@pytest.fixture
def two_node_with_edge_graph():
    """Return a graph with two nodes and one edge."""
    g = Graph()
    g.add_node('corn')
    g.add_node('beans')
    g.add_edge('corn', 'beans')
    return g


@pytest.fixture
def two_node_two_edge_graph():
    """Return a graph with two nodes and two edges."""
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    return g


@pytest.fixture
def three_node_with_two_edges_graph():
    """Return a graph with two nodes and two edges."""
    g = Graph()
    g.add_node('corn')
    g.add_node(2)
    g.add_node(11)
    g.add_edge('corn', 2)
    g.add_edge(11, 'corn')
    return g


@pytest.fixture
def three_node_cyclical_graph():
    """Return a bi-direcctional cyclical graph.."""
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 1)
    return g


@pytest.fixture
def four_node_cyclical_graph():
    """Return a graph with four nodes that is cyclical."""
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    return g


@pytest.fixture
def five_node_with_five_edges_graph():
    """Return a graph with five nodes and five edges."""
    g = Graph()
    g.add_node('corn')
    g.add_node(2)
    g.add_node(11.1)
    g.add_node('chocolate')
    g.add_node('mustard')
    g.add_edge(2, 11.1)
    g.add_edge('mustard', 'corn')
    g.add_edge(2, 'corn')
    g.add_edge('corn', 2)
    g.add_edge(11.1, 'corn')
    return g


@pytest.fixture
def five_node_simple_nodes_five_edges_graph():
    """Return a graph with five nodes and four edges."""
    g = Graph()
    g.add_node('corn')
    g.add_node(2)
    g.add_node(3)
    g.add_node('meep')
    g.add_node(10)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(2, 'corn')
    g.add_edge('meep', 10)
    return g


@pytest.fixture
def seven_node_heapish_graph():
    """Return a graph with seven nodes that is heap like."""
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 1)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(7, 5)
    return g


def test_nodes_in_empty_graph(empty_graph):
    """Test empty graph has no nodes."""
    assert empty_graph.nodes() == []


def test_nodes_in_one_node_graph(one_node_graph):
    """Test one-node graph has correct node."""
    assert one_node_graph.nodes() == ['corn']


def test_nodes_in_two_node_graph(two_node_no_edge_graph):
    """Test two-node graph has two nodes."""
    assert 'corn' in two_node_no_edge_graph.nodes()
    assert 'beans' in two_node_no_edge_graph.nodes()


def test_nodes_in_three_node_graph(three_node_with_two_edges_graph):
    """Test three-node graph has three correct nodes."""
    assert 'corn' in three_node_with_two_edges_graph.nodes()
    assert 2 in three_node_with_two_edges_graph.nodes()
    assert 11 in three_node_with_two_edges_graph.nodes()
    assert len(three_node_with_two_edges_graph.nodes()) == 3


def test_nodes_in_five_node_graph(five_node_with_five_edges_graph):
    """Test five-node graph has five correct nodes."""
    assert 'corn' in five_node_with_five_edges_graph.nodes()
    assert 2 in five_node_with_five_edges_graph.nodes()
    assert 11.1 in five_node_with_five_edges_graph.nodes()
    assert 'chocolate' in five_node_with_five_edges_graph.nodes()
    assert 'mustard' in five_node_with_five_edges_graph.nodes()
    assert len(five_node_with_five_edges_graph.nodes()) == 5


def test_has_node_one_node(one_node_graph):
    """Test one-node graph has_node method."""
    assert one_node_graph.has_node('corn') is True
    assert one_node_graph.has_node(1) is False


def test_has_node_two_nodes(two_node_no_edge_graph):
    """Test two-node graph has_node method."""
    assert two_node_no_edge_graph.has_node('beans') is True
    assert two_node_no_edge_graph.has_node('picante') is False


def test_has_node_five_nodes(five_node_with_five_edges_graph):
    """Test five-node graph has_node method."""
    assert five_node_with_five_edges_graph.has_node('picante') is False
    assert five_node_with_five_edges_graph.has_node(11.1) is True
    assert five_node_with_five_edges_graph.has_node(2) is True
    assert five_node_with_five_edges_graph.has_node('chocolate') is True
    assert five_node_with_five_edges_graph.has_node('11.1') is False


def test_edges_empty_graph(empty_graph):
    """Test an empty graph for edges."""
    assert empty_graph.edges() == []


def test_edges_one_node_graph(one_node_graph):
    """Test an empty graph for edges."""
    assert one_node_graph.edges() == []


def test_edges_two_node_no_edge_graph(two_node_no_edge_graph):
    """Test an empty graph for edges."""
    assert two_node_no_edge_graph.edges() == []


def test_edges_two_node_graph(two_node_with_edge_graph):
    """Test an empty graph for edges."""
    assert two_node_with_edge_graph.edges() == [('corn', 'beans')]


def test_edges_three_node_graph(three_node_with_two_edges_graph):
    """Test three node graph for two edges."""
    assert ('corn', 2) in three_node_with_two_edges_graph.edges()
    assert (11, 'corn') in three_node_with_two_edges_graph.edges()


def test_edges_five_node_graph(five_node_with_five_edges_graph):
    """Test a five node graph with five edges."""
    assert ('corn', 2) in five_node_with_five_edges_graph.edges()
    assert (2, 11.1) in five_node_with_five_edges_graph.edges()
    assert (2, 'corn') in five_node_with_five_edges_graph.edges()
    assert (11.1, 'corn') in five_node_with_five_edges_graph.edges()
    assert ('mustard', 'corn') in five_node_with_five_edges_graph.edges()


def test_add_node_no_val(one_node_graph):
    """Test adding node with no value raises ValueError."""
    with pytest.raises(ValueError):
        one_node_graph.add_node(None)


def test_add_node_bool(one_node_graph):
    """Test adding node with bool raises ValueError."""
    with pytest.raises(ValueError):
        one_node_graph.add_node(True)


def test_add_node_dupe(two_node_no_edge_graph):
    """Add two nodes to graph."""
    with pytest.raises(ValueError):
        two_node_no_edge_graph.add_node('corn')


def test_add_node_two_times(two_node_no_edge_graph):
    """Add two nodes to graph."""
    two_node_no_edge_graph.add_node('greetings')
    two_node_no_edge_graph.add_node('welcome back')
    assert two_node_no_edge_graph.has_node('greetings')
    assert two_node_no_edge_graph.has_node('welcome back')
    assert 'corn' in two_node_no_edge_graph.nodes()
    assert 'beans' in two_node_no_edge_graph.nodes()
    assert 'greetings' in two_node_no_edge_graph.nodes()
    assert 'welcome back' in two_node_no_edge_graph.nodes()


def test_add_node_once(two_node_no_edge_graph):
    """Add one node to graph."""
    two_node_no_edge_graph.add_node('why')
    assert two_node_no_edge_graph.has_node('why')
    assert 'corn' in two_node_no_edge_graph.nodes()
    assert 'beans' in two_node_no_edge_graph.nodes()
    assert 'why' in two_node_no_edge_graph.nodes()


def test_add_edge_new_nodes_on_empty(empty_graph):
    """Test adding edge creates nodes in empty graph with weight."""
    empty_graph.add_edge('chicken', 'bacon')
    assert 'chicken' and 'bacon' in empty_graph.nodes()
    assert ('chicken', 'bacon') in empty_graph.edges()


def test_add_edge_new_nodes(three_node_with_two_edges_graph):
    """Test adding edge with two new nodes."""
    three_node_with_two_edges_graph.add_edge('beans', 'tomato')
    assert ('corn', 2) in three_node_with_two_edges_graph.edges()
    assert (11, 'corn') in three_node_with_two_edges_graph.edges()
    assert ('beans', 'tomato') in three_node_with_two_edges_graph.edges()
    assert 'beans' and 'tomato' in three_node_with_two_edges_graph.nodes()


def test_add_edge_one_new_node(five_node_simple_nodes_five_edges_graph):
    """Test adding edge to one new node, one existing node."""
    five_node_simple_nodes_five_edges_graph.add_edge('hi', 3)
    assert (2, 3) in five_node_simple_nodes_five_edges_graph.edges()
    assert (2, 'corn') in five_node_simple_nodes_five_edges_graph.edges()
    assert (3, 2) in five_node_simple_nodes_five_edges_graph.edges()
    assert ('meep', 10) in five_node_simple_nodes_five_edges_graph.edges()
    assert ('hi', 3) in five_node_simple_nodes_five_edges_graph.edges()
    assert 'hi' and 3 in five_node_simple_nodes_five_edges_graph.nodes()


def test_add_edge_existing_nodes(five_node_simple_nodes_five_edges_graph):
    """Test adding edge to two existing nodes."""
    five_node_simple_nodes_five_edges_graph.add_edge(3, 'meep')
    assert (2, 3) in five_node_simple_nodes_five_edges_graph.edges()
    assert (2, 'corn') in five_node_simple_nodes_five_edges_graph.edges()
    assert (3, 2) in five_node_simple_nodes_five_edges_graph.edges()
    assert (3, 'meep') in five_node_simple_nodes_five_edges_graph.edges()
    assert ('meep', 10) in five_node_simple_nodes_five_edges_graph.edges()
    assert 3 and 'meep' in five_node_simple_nodes_five_edges_graph.nodes()


def test_delete_node_empty_graph_error(empty_graph):
    """Delete node on empty graph."""
    with pytest.raises(ValueError):
        empty_graph.del_node('delete')


def test_delete_node_graph_error(five_node_with_five_edges_graph):
    """Delete node on populated graph."""
    with pytest.raises(ValueError):
        five_node_with_five_edges_graph.del_node('delete')


def test_delete_node_graph(five_node_with_five_edges_graph):
    """Delete node on populated graph."""
    five_node_with_five_edges_graph.del_node(2)
    assert 2 not in five_node_with_five_edges_graph.nodes()
    assert (2, 'corn', 3) not in five_node_with_five_edges_graph.edges()
    assert (2, 11.1, 2) not in five_node_with_five_edges_graph.edges()


def test_delete_edge_empty_graph_error(empty_graph):
    """Delete node on empty graph."""
    with pytest.raises(ValueError):
        empty_graph.del_edge(1, 2)


def test_delete_edge_graph_error(five_node_with_five_edges_graph):
    """Delete node on empty graph."""
    with pytest.raises(ValueError):
        five_node_with_five_edges_graph.del_edge(1, 2)


def test_delete_edge_graph(five_node_simple_nodes_five_edges_graph):
    """Delete node on empty graph."""
    assert (2, 'corn') in five_node_simple_nodes_five_edges_graph.edges()
    five_node_simple_nodes_five_edges_graph.del_edge(2, 'corn')
    assert (2, 'corn') not in five_node_simple_nodes_five_edges_graph.edges()


def test_neighbors_not_in_graph(five_node_with_five_edges_graph):
    """Test if the node asked for is in the graph to have neighbors."""
    g = five_node_with_five_edges_graph
    with pytest.raises(ValueError):
        g.neighbors('cake')


def test_neighbors_two_nodes_in_graph(two_node_two_edge_graph):
    """Test that the queried node has one neighbor."""
    g = two_node_two_edge_graph
    assert g.neighbors(1) == [2]


def test_neighbors_five_nodes_in_graph(five_node_with_five_edges_graph):
    """Test that the queried node has two neighbors."""
    g = five_node_with_five_edges_graph
    assert g.neighbors(2) == [11.1, 'corn']


def test_adjacent_first_val_not_in_graph(five_node_with_five_edges_graph):
    """Test that the first val is not a node to be adjacent."""
    g = five_node_with_five_edges_graph
    with pytest.raises(ValueError):
        g.adjacent('cake', 11.1)


def test_adjacent_second_val_not_in_graph(five_node_with_five_edges_graph):
    """Test that the second val is not a node to be adjacent."""
    g = five_node_with_five_edges_graph
    with pytest.raises(ValueError):
        g.adjacent('corn', 'pie')


def test_adjacent_both_vals_not_in_graph(five_node_with_five_edges_graph):
    """Test that neither val is a node in the graph to be adjacent."""
    g = five_node_with_five_edges_graph
    with pytest.raises(ValueError):
        g.adjacent('cake', 'pie')


def test_adjacent_two_nodes_in_graph(two_node_two_edge_graph):
    """Test two nodes are adjacent returns True."""
    g = two_node_two_edge_graph
    assert g.adjacent(1, 2) is True


def test_adjacent_five_nodes_in_graph(five_node_with_five_edges_graph):
    """Test two nodes are adjacent returns True twice."""
    g = five_node_with_five_edges_graph
    assert g.adjacent(2, 11.1) is True
    assert g.adjacent(2, 'corn') is True


def test_depth_on_empty_graph(empty_graph):
    """Test a depth traersal on an empty graph."""
    with pytest.raises(ValueError):
        empty_graph.depth_first_traversal(3)


def test_breadth_on_empty_graph(empty_graph):
    """Test a breadth traersal on an empty graph."""
    with pytest.raises(ValueError):
        empty_graph.breadth_first_traversal(3)


def test_depth_non_node_non_empty_graph(two_node_no_edge_graph):
    """Test depth traversal with bad val on non empty graph."""
    with pytest.raises(ValueError):
        two_node_no_edge_graph.depth_first_traversal(6)


def test_breadth_non_node_non_empty_graph(two_node_no_edge_graph):
    """Test breadth traversal with bad val on non empty graph."""
    with pytest.raises(ValueError):
        two_node_no_edge_graph.breadth_first_traversal(6)


def test_depth_two_node_one_edge_graph(two_node_with_edge_graph):
    """Test depth traversal on two node graph with one edge."""
    g = two_node_with_edge_graph
    assert g.depth_first_traversal('corn') == ['corn', 'beans']
    assert g.depth_first_traversal('beans') == ['beans']


def test_breadth_two_node_one_edge_graph(two_node_with_edge_graph):
    """Test breadth traversal on two node graph with one edge."""
    g = two_node_with_edge_graph
    assert g.breadth_first_traversal('corn') == ['corn', 'beans']
    assert g.breadth_first_traversal('beans') == ['beans']


def test_depth_two_node_two_edge_graph(two_node_two_edge_graph):
    """Test depth traversal on two node graph with two edges."""
    g = two_node_two_edge_graph
    assert g.depth_first_traversal(1) == [1, 2]
    assert g.depth_first_traversal(2) == [2, 1]


def test_breadth_two_node_two_edge_graph(two_node_two_edge_graph):
    """Test breadth traversal on two node graph with two edges."""
    g = two_node_two_edge_graph
    assert g.breadth_first_traversal(1) == [1, 2]
    assert g.breadth_first_traversal(2) == [2, 1]


def test_depth_four_node_cyclical_graph(four_node_cyclical_graph):
    """Test depth traversal on four node cyclical graph."""
    g = four_node_cyclical_graph
    assert g.depth_first_traversal(1) == [1, 2, 3, 4]
    assert g.depth_first_traversal(4) == [4, 1, 2, 3]


def test_breadth_four_node_cyclical_graph(four_node_cyclical_graph):
    """Test breadth traversal on four node cyclical graph."""
    g = four_node_cyclical_graph
    assert g.breadth_first_traversal(1) == [1, 2, 3, 4]
    assert g.breadth_first_traversal(3) == [3, 4, 1, 2]


def test_depth_three_node_cyclical_graph(three_node_cyclical_graph):
    """Test depth traversal on three node cyclical graph."""
    g = three_node_cyclical_graph
    assert g.depth_first_traversal(1) == [1, 2, 3]
    assert g.depth_first_traversal(3) == [3, 2, 1]


def test_breadth_three_node_cyclical_graph(three_node_cyclical_graph):
    """Test breadth traversal on three node cyclical graph."""
    g = three_node_cyclical_graph
    assert g.breadth_first_traversal(1) == [1, 2, 3]
    assert g.breadth_first_traversal(2) == [2, 1, 3]


def test_depth_seven_node_heapish_graph(seven_node_heapish_graph):
    """Test depth traversal on seven node heap like, semi cyclical graph."""
    g = seven_node_heapish_graph
    assert g.depth_first_traversal(3) == [3, 1, 2, 4, 5, 6, 7]
    assert g.depth_first_traversal(5) == [5, 6, 7]
    assert g.depth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]
    assert g.depth_first_traversal(7) == [7, 5, 6]
    assert g.depth_first_traversal(2) == [2, 3, 1, 5, 6, 7, 4]


def test_breadth_seven_node_heapish_graph(seven_node_heapish_graph):
    """Test breadth traversal on seven node heap like, semi cyclical graph."""
    g = seven_node_heapish_graph
    assert g.breadth_first_traversal(1) == [1, 2, 5, 3, 4, 6, 7]
    assert g.breadth_first_traversal(5) == [5, 6, 7]
    assert g.breadth_first_traversal(2) == [2, 3, 4, 1, 5, 6, 7]
    assert g.breadth_first_traversal(7) == [7, 5, 6]


def test_adj_no_edge_first_to_second_val(five_node_with_five_edges_graph):
    """Test if there is no edge from val 1 to val 2."""
    g = five_node_with_five_edges_graph
    with pytest.raises(AssertionError):
        g.adjacent(11.1, 2)
