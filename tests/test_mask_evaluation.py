import unittest
from examples.mask_evaluation import evaluate


class MaskEvaluationTests(unittest.TestCase):
    def test_counts_and_ratios(self):
        result = evaluate([[1,1],[0,0]], [[1,0],[1,0]], pixel_area_m2=2)
        self.assertEqual((result['tp'], result['fp'], result['fn'], result['tn']), (1,1,1,1))
        self.assertAlmostEqual(result['iou'], 1/3)
        self.assertEqual(result['precision'], 0.5)
        self.assertEqual(result['recall'], 0.5)
        self.assertEqual(result['reference_positive_area_m2'], 4)

    def test_excluded_false_positive(self):
        result = evaluate([[1,0]], [[1,1]], [[0,1]])
        self.assertEqual(result['excluded_cells'], 1)
        self.assertEqual(result['iou'], 1)

    def test_undefined_metrics(self):
        result = evaluate([[0]], [[0]])
        self.assertIsNone(result['iou'])
        self.assertIsNone(result['precision'])
        self.assertIsNone(result['recall'])
        self.assertIsNone(evaluate([[1]], [[1]], [[1]])['iou'])

    def test_validation(self):
        for args in [([[1]], [[1,0]]), ([[2]], [[1]]), ([[1]], [[1]], [[0]], -1), ([[1]], [[1]], [[0]], float('nan'))]:
            with self.assertRaises(ValueError):
                evaluate(*args)


if __name__ == '__main__':
    unittest.main()
