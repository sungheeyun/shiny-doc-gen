import unittest

from human_resource.constants import JobFamily, JobLevel


class TestEnums(unittest.TestCase):
    def test_job_family_enum(self) -> None:
        self.assertEqual(JobFamily.PM.name, "PM")
        self.assertEqual(JobFamily.CV_AS.name, "CV_AS")
        self.assertEqual(JobFamily.ML_AS.name, "ML_AS")
        self.assertEqual(JobFamily.OPT_AS.name, "OPT_AS")
        self.assertEqual(JobFamily.SWE.name, "SWE")

    def test_job_level_enum(self) -> None:
        self.assertEqual(JobLevel.JUNIOR.name, "JUNIOR")
        self.assertEqual(JobLevel.SENIOR.name, "SENIOR")


if __name__ == '__main__':
    unittest.main()
