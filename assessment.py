"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

The first concept is encapsulation, which is where data is stored near to its functionality
The second concept is abstraction, which helps us use methods without needing to know the
information that method uses internally.
Lastly is polymorphism, which makes it easy to make new and different, interchangeable types.

2. What is a class?

Basically everthing is a class! It is a type of object. There are built in classes, like lists
and strings, and there we can create out own classes and give them attributes and methods that we 
define. 

3. What is an instance attribute?

An instance attribute is something that is specific to that instance of a class. It could be different
from that of another instance of the same class. 

4. What is a method?

A method is a function that is run on a class instance, and thats that instance as its first 
parameter.

5. What is an instance in object orientation?

Instance is used in python, where 'object' may be used in other languages, but it is an
individual occurrence of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is something that every instance of that class has, for example for a class Cat,
we might give every instance the attribute of species = 'cat'. 
An instance attribute can be different from instance to instance, like we could name the cat,
so one instance could have the attribute name = 'Alex' and another's name could be 'Felix'.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ Stores students first name, last name and address"""

    def __init__(self, f_name, l_name, addr):
        self.f_name = f_name
        self.l_name = l_name
        self.addr = addr

    def __repr__(self):
        return "{} {} lives at {}".format(self.f_name, self.l_name, self.addr)


class Question(object):
    """Stores question and its answer"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return "Question: {}\nAnswer: {}".format(self.question, self.answer)

    def ask_and_evaluate(self):
        """ Ask question and return True if the answer was correct else return False"""

        user_answer = raw_input(self.question + ' ')
        return user_answer == self.answer


class Exam(object):
    """Stores exam name with a list of Question objects"""

    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def __repr__(self):
        return "For the {} Exam, here are the questions:\n{}".format(self.name, self.questions)

    def add_question(self, question, answer):
        """Add new question with answer"""

        self.questions.append(Question(question, answer))

    def administer(self):
        """Ask questions and return score of how many were correct"""

        correct = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                correct += 1.0
        score = (correct / len(self.questions)) * 100
        return score


class StudentExam(object):
    """Stores an instance of Student with an instance of Exam and the score for the exam"""

    def __init__(self, student, exam, score=None):
        self.student = student
        self.exam = exam
        self.score = score

    def __repr__(self):
        return "{} {} scored a {} on her {} exam.".format(self.student.f_name, self.student.l_name,
                self.score, self.exam.name)

    def take_test(self):
        """Store score from administering the test"""

        self.score = self.exam.administer()
        print "You scored {}".format(self.score)


class Quizz(Exam):
    """Inherits from Exam but scores differently"""

    def __repr__(self):
        return "For the {} Quizz, here are the questions:\n{}".format(self.name, self.questions)

    def administer(self):
        score = super(Quizz, self).administer()
        if score >= 50:
            return 1
        else:
            return 0


class StudentQuizz(StudentExam):
    """Stores an instance of Student with an instance of Quizz and the score for the Quizz"""

    def __init__(self,  student, quizz, score=None):
        self.student = student
        self.quizz = quizz
        self.score = score

    def __repr__(self):
        return "{} {} scored a {} on her {} quizz.".format(self.student.f_name, self.student.l_name,
                self.score, self.quizz.name)

    def take_test(self):
        """Store score from administering the test"""

        self.score = self.quizz.administer()
        print "You scored {}".format(self.score)


def example():
    """Create StudentExam instance and administers the test"""

    # Create Exam instance
    exam = Exam('Midterm')
    # Add three questions
    exam.add_question('What is the method for adding an element to a set?', '.add()')
    exam.add_question('What does pwd stand for?', 'print working directory')
    exam.add_question('Python lists are mutable, iterable, and what?', 'ordered')
    # Create student instance
    student = Student('Benedict', 'Cumberbatch', '1526 Looneyville Blvd')
    # Instantiate StudentExam instance from exam and student
    new_exam = StudentExam(student, exam)
    new_exam.take_test()


