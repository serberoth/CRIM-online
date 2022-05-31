from crim.models.person import CRIMPerson
from crim.models.definition import CRIMDefinition
# from crim.models.person import CRIMPerson
from django.test import TestCase
from mixer.backend.django import mixer

class PersonTestCase(TestCase):
    def setUp(self):
        self.dummyPerson = mixer.blend(CRIMPerson)

    # testing CRIMperson's methods (except save)

    def test_sorted_name(self):
        self.assertEqual(self.dummyPerson.name_sort, self.dummyPerson.sorted_name())

    def test_get_absolute_url(self):
        self.assertEqual(self.dummyPerson.get_absolute_url(), '/people/' + self.dummyPerson.person_id + '/')

    def test_self_string(self):
        self.assertEqual(str(self.dummyPerson), self.dummyPerson.name_sort)

class DefinitionTestCase(TestCase):
    def setUp(self):
        self.dummyDefinition = mixer.blend(CRIMDefinition)

    # testing CRIMDefinition methods

    def test_self_string(self):
        # self.assertEqual(self.dummyDefinition.pk, str(self.dummyDefinition))
        print(str(self.dummyDefinition))
