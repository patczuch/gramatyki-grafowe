import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from hypergraph.hypergraph import HyperGraph
from productions import P0, P1, p2, P3, p4, P5, p6, P7, P9, P10, P11, P12
from productions.p4.p4 import P4
from productions.p2.p2 import P2


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

        Q0 = self.graph.add_hyperedge([n1, n2, n3, n4], label="Q")
        Q1 = self.graph.add_hyperedge([o1, o2, n2, n1], label="Q")
        Q2 = self.graph.add_hyperedge([o4, o3, n3, n4], label="Q")
        S1 = self.graph.add_hyperedge([o1, n1, o7, o8, n4, o4], label="S")
        S2 = self.graph.add_hyperedge([o2, o5, o6, o3, n3, n2], label="S")

        output_dir = os.path.join(os.path.dirname(__file__), 'outputs')
        os.makedirs(output_dir, exist_ok=True)

        before_path = os.path.join(output_dir, '0.png')
        self.graph.visualize(before_path)

        P9().apply(self.graph, {'hyperedge': S2, 'nodes': [], 'edges': []})

        before_path = os.path.join(output_dir, '1.png')
        self.graph.visualize(before_path)

        P0().apply(self.graph, {'hyperedge': Q2, 'nodes': [], 'edges': []})

        before_path = os.path.join(output_dir, '2.png')
        self.graph.visualize(before_path)

        can_apply, matched = P10().can_apply(self.graph)
        P10().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '3.png')
        self.graph.visualize(before_path)

        can_apply, matched = P4().can_apply(self.graph)
        P4().apply(self.graph, matched)
        can_apply, matched = P4().can_apply(self.graph)
        P4().apply(self.graph, matched)
        can_apply, matched = P4().can_apply(self.graph)
        P4().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '4.png')
        self.graph.visualize(before_path)

        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)
        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)
        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '5.png')
        self.graph.visualize(before_path)

        can_apply, matched = P11().can_apply(self.graph)
        P11().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '6.png')
        self.graph.visualize(before_path)

        can_apply, matched = P1().can_apply(self.graph)
        P1().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '7.png')
        self.graph.visualize(before_path)

        can_apply, matched = P4().can_apply(self.graph)
        P4().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '8.png')
        self.graph.visualize(before_path)

        can_apply, matched = P2().can_apply(self.graph)
        P2().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '9.png')
        self.graph.visualize(before_path)

        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)
        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '10.png')
        self.graph.visualize(before_path)

        can_apply, matched = P5().can_apply(self.graph)
        P5().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '11.png')
        self.graph.visualize(before_path)

        can_apply, matched = P0().can_apply(self.graph)
        P0().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '12.png')
        self.graph.visualize(before_path)

        can_apply, matched = P1().can_apply(self.graph)
        P1().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '13.png')
        self.graph.visualize(before_path)

        can_apply, matched = P2().can_apply(self.graph)
        P2().apply(self.graph, matched)
        can_apply, matched = P2().can_apply(self.graph)
        P2().apply(self.graph, matched)
        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)
        can_apply, matched = P3().can_apply(self.graph)
        P3().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '14.png')
        self.graph.visualize(before_path)

        can_apply, matched = P5().can_apply(self.graph)
        res = P5().apply(self.graph, matched)

        before_path = os.path.join(output_dir, '15.png')
        self.graph.visualize(before_path)

        for i in range(5):

            P0().apply(self.graph, {'hyperedge': res["new_hyperedges"][2], 'nodes': [], 'edges': []})

            can_apply, matched = P1().can_apply(self.graph)
            P1().apply(self.graph, matched)

            can_apply, matched = P3().can_apply(self.graph)
            P3().apply(self.graph, matched)
            can_apply, matched = P3().can_apply(self.graph)
            P3().apply(self.graph, matched)
            can_apply, matched = P3().can_apply(self.graph)
            P3().apply(self.graph, matched)
            can_apply, matched = P3().can_apply(self.graph)
            P3().apply(self.graph, matched)

            can_apply, matched = P5().can_apply(self.graph)
            res = P5().apply(self.graph, matched)

            before_path = os.path.join(output_dir, str(i + 16) + '.png')
            self.graph.visualize(before_path, False)



        # can_apply, matched = self.production.can_apply(self.graph)
        #
        # self.assertTrue(can_apply, "Production P0 should be applicable to correct quadrilateral")
        # self.assertIsNotNone(matched, "Matched elements should not be None")
        # self.assertEqual(matched['hyperedge'], q)
        # self.assertEqual(len(matched['nodes']), 4)
        # self.assertEqual(len(matched['edges']), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
