class Book:
    def __init__(self, title, author, publisher, page_count):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.page_count = page_count

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Page Count: {self.page_count}"

class PeriodicalPublication(Book):
    def __init__(self, title, author, publisher, page_count, period):
        super().__init__(title, author, publisher, page_count)
        self.period = period

    def get_period(self):
        return f"Period: {self.period}"

    def __str__(self):
        return f"Periodical Publication: {super().__str__()}, {self.get_period()}"

class AudioPublication(Book):
    def __init__(self, title, author, publisher, page_count, narrator):
        super().__init__(title, author, publisher, page_count)
        self.narrator = narrator

    def get_narrator(self):
        return f"Narrator: {self.narrator}"

    def __str__(self):
        return f"Audio Publication: {super().__str__()}, {self.get_narrator()}"

class AcademicPublication(Book):
    predefined_papers = {"First", "Second", "Third"}

    def __init__(self, title, author, publisher, page_count, field):
        super().__init__(title, author, publisher, page_count)
        self.field = field
        self.papers = set()

    def get_field(self):
        return f"Field: {self.field}"

    def __str__(self):
        papers_str = ', '.join(self.get_papers()) if self.get_papers() else "No papers"
        return f"Academic Publication: {super().__str__()}, {self.get_field()}, Papers: {papers_str}"

    def remove_paper(self, paper):
        if paper in self.papers:
            self.papers.remove(paper)
            print(f"{paper} removed from the papers.")
        else:
            print(f"{paper} is not in the papers.")
    
    def control_and_add_paper(self, paper):
        if paper in AcademicPublication.predefined_papers:
            print(f"{paper} is already in the predefined_papers.")
        elif paper in self.papers:
            print(f"{paper} is already in the papers.")
        else:
            self.papers.add(paper)
            print(f"{paper} added to the papers.")

    def get_papers(self):
        return self.papers

# Examples
periodical_publication = PeriodicalPublication("Magazine Name", "Author Name", "Publisher", 50, "Monthly")
audio_publication = AudioPublication("Audiobook Name", "Narrator Author", "Audiobook Publishers", 200, "Narrator Person")
academic_publication = AcademicPublication("Academic Study", "Academic Author", "Science Publications", 300, "Computer Science")
academic_publication.control_and_add_paper("First")
academic_publication.control_and_add_paper("Second")
academic_publication.control_and_add_paper("Third")
academic_publication.control_and_add_paper("First")
academic_publication.remove_paper("Third Paper")
academic_publication.remove_paper("First")
# Print information by calling __str__ methods
print(academic_publication)
print(periodical_publication)
print(audio_publication)
