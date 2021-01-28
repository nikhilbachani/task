# To test the solution, navigate to the main mysite directory using a Terminal
# Then run: python manage.py shell

# Sample data:
# Question 1: What's up?    Choices: Not much, The sky
# Question 2: What's new?    Choices: Not much, The dress

# Test 1: Question text must be unique i.e., no two questions can have the same text.
# Try adding the question "What's new?" to the Question table
# Should report "IntegrityError: UNIQUE constraint failed: polls_question.question_text"
from polls.models import Question
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

# Test 2: Choice text within a question must be unique i.e., for a given question no two choices can have the same text.
# Try adding the choice "Not much" to the Question "What's up?"
# Should report "UNIQUE constraint failed: polls_choice.question_id, polls_choice.choice_text"
from polls.models import Question
Question.objects.all()
q = Question.objects.get(question_text__endswith='up?')
q.question_text
q.choice_set.create(choice_text="Not much", votes=0)
