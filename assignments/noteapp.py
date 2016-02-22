class NotesApplication (object):

    def __init__(self,author):
        #note_list = []
        self.author = author
        self.note_name = []

    def create(self,note_content):
        self.note_name.append(note_content) 

    def list(self):
        if self.note_name == []:
            print ('No Note Created')
        else:
            for i in self.note_name:
                print ('NOTE ID: {}'.format(self.note_name.index(i)))
                print (i)
                print ('By {}'.format(self.author))

    def get(self,note_id):
        self.note_id = note_id
        if self.note_name == []:
            print ('No note created')
        elif note_id < 0 or note_id > len (self.note.note_name) - 1:
            print ('{} is out of range'.format(note_id))
        else:
            print (self.note_name[note_id])
        
    def search(self,search_text):
        self.search_text = search_text
        self.list = []
        if self.note_name == []:
            print ('NO note created')
        else:
            for i in self.note_name:
                if search_text in i:
                    self.list.append(self.note_name.index(i))
            if len(self.list) > 0:
                print ('showing results for {}'.format(search_text))
                for j in self.list:
                    print ('NOTE ID: ',j)
                    print(self.note_name[j])
                    print('By {}'.format(self.author))
            else:
                print ('no results found for search "{}"'.format(search_text))


            
    def delete(self,note_id):
        self.note_name.pop(note_id)       
        if self.note_name == []:
            print ('NO note created')
        elif note_id < 0 or note_id > len (self.note_id) - 1:
            print ('{} out of range of note index'.format(note_id))
        else:
            return len(self.note_name)


    def edit (self,note_id,note_content):
        if self.note_name == []:
            print ('NO note created')
        elif note_id < 0 or note_id > len (self.note_name) - 1:
            print ('{} out of range of note index'.format(note_id))        
        else:
            self.note_name[note_id]=note_content
            return self.note_name[note_id]

      


