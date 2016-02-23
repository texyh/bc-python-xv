import unittest
import sys
from noteapp import NotesApplication

from manager import capture


class NotesApplicationTestSuite(unittest.TestCase):


    def test_NotesApplication_instance(self):
        test = NotesApplication("test")
        self.assertIsInstance(test, NotesApplication, msg="The object should be an instance of the 'NotesApplication' class")


    def test_object_type(self):
        test = NotesApplication("test")
        self.assertTrue((type(test) is NotesApplication), msg="The object should be a type of 'NotesApplication'")


    def test_create_one_note(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        self.assertEqual(["emeka is a boy"], test.note_name, msg="The class should have a create method adds its argument to a property called notes")


    def test_create_two_notes(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        test.create("chidi is fresh")
        self.assertEqual(["emeka is a boy", "chidi is fresh"], test.note_name, 
                          msg="The create method should add multiple notes to the same 'notes' property")


    def test_list_empty_note_list(self):
        test = NotesApplication("test")
        with capture(test.list) as output:
            self.assertEqual("", output,
                              msg="The note_list should be empty until you create a list with the create method")


    def test_list_one_note_in_notes(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        listoutput = "Note ID: 0\nemeka is a boy\nBy Author test\n"
        with capture(test.list) as output:
            self.assertEqual(listoutput, output, msg="The list method should print according to the specified format")


    def test_list_five_notes_in_notes(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        test.create("chidi is fresh")
        test.create("i am fresh too")
        listoutput = ("Note ID: 0\nemeka is a boy\nBy Author test\n"
                     "Note ID: 1\nchidi is fresh\nBy Author test\n"
                     "Note ID: 2\ni am fresh too\nBy Author test\n"
                    )
        with capture(test.list) as output:
            self.assertEqual(listoutput, output, msg="The list method should print according to the specified format")


    def test_list_notes_of_digits(self):
        test = NotesApplication("test")
        test.create(1)
        test.create(2)
        test.create(3)
        appOutput = ("Note ID: 0\n1\nBy Author test\n"
                     "Note ID: 1\n2\nBy Author test\n"
                     "Note ID: 2\n3\nBy Author test\n"
                    )
        with capture(test.list) as output:
            self.assertEqual(appOutput, output, msg="List method doesn't handle a note list of only digits well")


    def test_get_note_from_begining(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        res = test.get(0)
        self.assertEqual("emeka is a boy", res, msg="get() method does not return the right value at 0 index")


    def test_get_note_from_end(self):
        test = NotesApplication("test")
        test.create("emeka is boy")
        test.create(1)
        test.create(2)
        test.create("chidi is fresh")
        res  = test.get(3)
        self.assertEqual("chidi is fresh",res , msg="get() method does not return the right value at the last index")


    def test_get_with_nonexistent_index(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        test.create(1)
        test.create(4)
        appOutput = "The index you entered does not exist\n"
        with capture(test.get, 8) as output:
            self.assertEqual(appOutput, output, msg="get() method does not handle entry of invalid indices appropriately")


    def test_get_note_from_empty_notes(self):
        test = NotesApplication("test")
        appOutput = "No note created"
        with capture(test.get, 0) as output:
            self.assertEqual(appOutput, output, msg="get() method is supposed to warn user that the note list is empty")


    def test_search_finds_matches(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        appOutput = ("showing results for emeka"
                     "Note ID: 0\nemeka is a boy\nBy Author test\n")
        with capture(test.search, "emeka") as output:
            self.assertEqual(appOutput, output, msg="search() method does not find matches")


    def test_search_handles_non_matches(self):
        test = NotesApplication("Erika")
        test.create("emeka is a boy")


    def test_search_finds_multiple_matches(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        test.create("chidi is fresh")
        test.create("bad boy")
        appOutput = ("showing results for is"
                     "Note ID: 0\nemeka is a boy\nBy Author test\n"
                     "Note ID: 1\nchidi is fresh\nBy Author test\n"
                    )
        with capture(test.search, "is") as output:
            self.assertEqual(appOutput, output, msg="search() method does not find multiple matches")


    def test_for_delete_note(self):
        test = NotesApplication('test')
        test.create('emeka is a boy')
        lenght = len(self.note_name)
        res = (test.delete(0))
        self.assertEqual(res,lenght)


    def test_for_delete_2(self):
        test = NotesApplication('test')
        res = (test.delete(0))
        appOutput = "No note created\n"
        with capture(res, 0) as output:
            self.assertEqual(appOutput, output, msg="delete() method is supposed to warn user that the note list is empty")


    def test_edit_note(self):
        test = NotesApplication("test")
        test.create("emeka is a boy")
        test.create("ada is a girl")
        test.create("Real studio")
        appOutput = ("Note ID: 0\nemeka is boy\nBy Author Erika\n"
                     "Note ID: 1\nchidi is fresh\nBy Author Erika\n"
                     "Note ID: 2\nReal studio\nBy Author Erika\n"
                    )
        test.edit(1, "chidi is fresh")
        with capture(test.list) as output:
            self.assertEqual(appOutput, output, msg="edit() method does not edit note specified by index")


if __name__ == "__main__":
    unittest.main()