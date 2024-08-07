import logging
from django.test import TestCase
from parameterized import parameterized
from .views import check_planning_permission

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnclosureModelTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        logger.info("All test cases passed successfully!")

    @parameterized.expand([
        # Adjacent to vehicular highway
        ('adjacent_vehicular_highway', 'up_to_1m', 'not_applicable', 'No permission needed'),
        ('adjacent_vehicular_highway', 'above_1m', 'not_applicable', 'Permission needed'),
        ('adjacent_vehicular_highway', 'up_to_2m', 'not_applicable', 'Permission needed'),
        ('adjacent_vehicular_highway', 'above_2m', 'not_applicable', 'Permission needed'),

        # Facing listed building
        ('facing_listed_building', 'not_applicable', 'not_applicable', 'Permission needed'),

        # Not applicable location, various heights
        ('not_applicable', 'up_to_1m', 'not_applicable', 'No permission needed'),
        ('not_applicable', 'above_1m', 'not_applicable', 'No permission needed'),
        ('not_applicable', 'up_to_2m', 'not_applicable', 'No permission needed'),
        ('not_applicable', 'above_2m', 'not_applicable', 'Permission needed'),

        # Location and height not applicable; no universal constraints
        ('not_applicable', 'not_applicable', 'not_applicable', 'No permission needed'),

        # Universal constraints
        ('not_applicable', 'not_applicable', 'listed_building', 'Permission needed'),
        ('not_applicable', 'not_applicable', 'AONB', 'Permission needed'),
        ('not_applicable', 'not_applicable', 'article_2_3', 'Permission needed'),
        ('not_applicable', 'not_applicable', 'article_2_4', 'Permission needed'),
        ('not_applicable', 'not_applicable', 'article_4', 'Permission needed'),
        ('not_applicable', 'not_applicable', 'works_affecting_TPO', 'Permission needed'),
    ])
    def test_check_planning_permission(self, location, height, constraint, expected):
        result = check_planning_permission(location, height, constraint)
        self.assertEqual(result, expected, f"Failed: Expected {expected}, but got {result}")
        logger.info(f"Passed: Location={location}, Height={height}, Constraint={constraint} -> {result}")

if __name__ == '__main__':
    logger.info("Starting test cases...")
    TestCase.main()
    logger.info("All test cases passed successfully!")