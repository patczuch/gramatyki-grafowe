import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from hypergraph.hypergraph import HyperGraph
from productions import P0


class Zad2(unittest.TestCase):
    def setUp(self):
        self.graph = HyperGraph()
        self.production = P0()

    def test_can_apply_correct_quadrilateral(self):
        # Wierzchołki wewnętrznego kwadratu
        n1 = self.graph.add_node(0.5, 1)
        n2 = self.graph.add_node(2, 1)
        n3 = self.graph.add_node(2, 2)
        n4 = self.graph.add_node(0.5, 2)

        # Krawędzie wewnętrznego kwadratu
        self.graph.add_edge(n1, n2, is_border=False)
        self.graph.add_edge(n2, n3, is_border=False)
        self.graph.add_edge(n3, n4, is_border=False)
        self.graph.add_edge(n4, n1, is_border=False)

        # Wierzchołki zewnętrznego ośmiokąta
        o1 = self.graph.add_node(0, 0)
        o2 = self.graph.add_node(3, 0)
        o3 = self.graph.add_node(3, 3)
        o4 = self.graph.add_node(0, 3)
        o5 = self.graph.add_node(4, 1)
        o6 = self.graph.add_node(4, 2)
        o7 = self.graph.add_node(-0.5, 1)
        o8 = self.graph.add_node(-0.5, 2)

        # Krawędzie zewnętrzne (graniczne)
        self.graph.add_edge(o1, o2, is_border=True)
        self.graph.add_edge(o2, o5, is_border=True)
        self.graph.add_edge(o5, o6, is_border=True)
        self.graph.add_edge(o6, o3, is_border=True)
        self.graph.add_edge(o3, o4, is_border=True)
        self.graph.add_edge(o1, o7, is_border=True)
        self.graph.add_edge(o7, o8, is_border=True)
        self.graph.add_edge(o8, o4, is_border=True)

        # Krawędzie łączące wewnętrzny kwadrat z zewnętrznym ośmiokątem
        self.graph.add_edge(n1, o1, is_border=False)
        self.graph.add_edge(n2, o2, is_border=False)
        self.graph.add_edge(n3, o3, is_border=False)
        self.graph.add_edge(n4, o4, is_border=False)

        self.graph.add_hyperedge([n1, n2, n3, n4], label="Q")
        self.graph.add_hyperedge([o1, o2, n1, n2], label="Q")
        self.graph.add_hyperedge([o3, o4, n3, n4], label="Q")

        output_dir = os.path.join(os.path.dirname(__file__), 'outputs')
        os.makedirs(output_dir, exist_ok=True)

        before_path = os.path.join(output_dir, 'test_zad2.png')
        self.graph.visualize(before_path)


        # can_apply, matched = self.production.can_apply(self.graph)
        #
        # self.assertTrue(can_apply, "Production P0 should be applicable to correct quadrilateral")
        # self.assertIsNotNone(matched, "Matched elements should not be None")
        # self.assertEqual(matched['hyperedge'], q)
        # self.assertEqual(len(matched['nodes']), 4)
        # self.assertEqual(len(matched['edges']), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
