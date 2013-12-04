"""
Tests the logic of the "targeted-feedback" attribute for MultipleChoice questions,
i.e. those with the <multiplechoiceresponse> element
"""

import unittest
import textwrap
from . import test_system, new_loncapa_problem


class CapaTargetedFeedbackTest(unittest.TestCase):
    '''
    Testing class
    '''

    def setUp(self):
        super(CapaTargetedFeedbackTest, self).setUp()
        self.system = test_system()

    # def test_no_answer_pool_4_choices(self):

    def test_answer_pool_4_choices_1_multiplechoiceresponse_seed1(self):
        xml_str = textwrap.dedent("""
            <problem>
            <p>What is the correct answer?</p>
            <multiplechoiceresponse targeted-feedback="alwaysShowCorrectChoiceExplanations">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="feedback1">wrong-1</choice>
                <choice correct="false" explanation-id="feedback2">wrong-2</choice>
                <choice correct="true" explanation-id="feedbackC">correct-1</choice>
                <choice correct="false" explanation-id="feedback3">wrong-3</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <targetedfeedbackset>
                <targetedfeedback explanation-id="feedback1">
                <div class="detailed-targeted-feedback" >
                    <p>Targeted Feedback</p>
                    <p>This is the 1st WRONG solution</p>
                </div>
                </targetedfeedback>

                <targetedfeedback explanation-id="feedback2">
                <div class="detailed-targeted-feedback" >
                    <p>Targeted Feedback</p>
                    <p>This is the 2nd WRONG solution</p>
                </div>
                </targetedfeedback>

                <targetedfeedback explanation-id="feedback3">
                <div class="detailed-targeted-feedback" >
                    <p>Targeted Feedback</p>
                    <p>This is the 3rd WRONG solution</p>
                </div>
                </targetedfeedback>

                <targetedfeedback explanation-id="feedbackC">
                <div class="detailed-targeted-feedback-correct">
                    <p>Targeted Feedback</p>
                    <p>Feedback on your correct solution...</p>
                </div>
                </targetedfeedback>

            </targetedfeedbackset>

            <solution explanation-id="feedbackC">
            <div class="detailed-solution" >
                <p>Explanation</p>
                <p>This is the solution explanation</p>
                <p>Not much to explain here, sorry!</p>
            </div>
            </solution>
        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        problem.seed = 723
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-3'.*'wrong-1'.*'wrong-2'.*'correct-2'.*\].*</div>")

        # problem = new_loncapa_problem(xml_str, seed=56)
        # problem = new_loncapa_problem(xml_str)
        # problem.seed = 56
        # problem.done = True
        # problem.student_answers = {'1_2_1': 'choice_3'}

        # the_html = problem.get_html()

        # # print "\n\n"
        # # print the_html
        # # print "\n\n"

        # # ipdb.set_trace()

        # self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-4'.*'wrong-3'.*'wrong-2'.*'correct-2'.*\].*</div>")
        # self.assertRegexpMatches(the_html, r"3rd WRONG")
        # self.assertRegexpMatches(the_html, r"2nd solution")
        # self.assertNotRegexpMatches(the_html, r"1st solution")

        # problem = new_loncapa_problem(xml_str)
        # rnd = Random()
        # ix = rnd.randint(0, 20)
        # problem.seed = ix
        # the_html = problem.get_html()

        # print the_html
        # self.assertEqual(1, 2)
        # self.assertRegexpMatches(the_html, r"<div>.*\[.*'A'.*'B'.*'C'.*\].*</div>.*")






    def test_answer_pool_4_choices_1_multiplechoiceresponse_seed2(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="4">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        problem.seed = 9
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'correct-1'.*'wrong-2'.*'wrong-1'.*'wrong-4'.*\].*</div>")

    def test_no_answer_pool_4_choices_1_multiplechoiceresponse(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse>
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-1'.*'wrong-2'.*'correct-1'.*'wrong-3'.*'wrong-4'.*'correct-2'.*\].*</div>")

    def test_0_answer_pool_4_choices_1_multiplechoiceresponse(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="0">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-1'.*'wrong-2'.*'correct-1'.*'wrong-3'.*'wrong-4'.*'correct-2'.*\].*</div>")

    def test_invalid_answer_pool_4_choices_1_multiplechoiceresponse(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="2.3">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-1'.*'wrong-2'.*'correct-1'.*'wrong-3'.*'wrong-4'.*'correct-2'.*\].*</div>")

    def test_answer_pool_5_choices_1_multiplechoiceresponse_seed1(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="5">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        problem.seed = 723
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-2'.*'wrong-1'.*'correct-2'.*'wrong-3'.*'wrong-4'.*\].*</div>")

    def test_answer_pool_2_multiplechoiceresponses_seed1(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="4">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="3">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        problem.seed = 723
        the_html = problem.get_html()

        str1 = r"<div>.*\[.*'wrong-3'.*'wrong-1'.*'wrong-2'.*'correct-2'.*\].*</div>"
        str2 = r"<div>.*\[.*'wrong-4'.*'wrong-2'.*'correct-2'.*\].*</div>"

        self.assertRegexpMatches(the_html, str1)
        self.assertRegexpMatches(the_html, str2)

        without_new_lines = the_html.replace("\n", "")

        self.assertRegexpMatches(without_new_lines, str1 + r".*" + str2)

    def test_answer_pool_2_multiplechoiceresponses_seed2(self):
        xml_str = textwrap.dedent("""
            <problem>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="3">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

            <p>What is the correct answer?</p>
            <multiplechoiceresponse answer-pool="4">
              <choicegroup type="MultipleChoice">
                <choice correct="false" explanation-id="solution1w">wrong-1</choice>
                <choice correct="false" explanation-id="solution2w">wrong-2</choice>
                <choice correct="true" explanation-id="solution1">correct-1</choice>
                <choice correct="false" explanation-id="solution3w">wrong-3</choice>
                <choice correct="false" explanation-id="solution4w">wrong-4</choice>
                <choice correct="true" explanation-id="solution2">correct-2</choice>
              </choicegroup>
            </multiplechoiceresponse>

            <solutionset>
                <solution explanation-id="solution1">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 1st solution</p>
                    <p>Not much to explain here, sorry!</p>
                </div>
                </solution>

                <solution explanation-id="solution2">
                <div class="detailed-solution" >
                    <p>Explanation</p>
                    <p>xThis is the 2nd solution</p>
                </div>
                </solution>
            </solutionset>

        </problem>

        """)

        problem = new_loncapa_problem(xml_str)
        problem.seed = 9
        the_html = problem.get_html()

        str1 = r"<div>.*\[.*'wrong-1'.*'wrong-2'.*'correct-1'.*\].*</div>"
        str2 = r"<div>.*\[.*'wrong-4'.*'wrong-3'.*'correct-1'.*'wrong-1'.*\].*</div>"

        self.assertRegexpMatches(the_html, str1)
        self.assertRegexpMatches(the_html, str2)

        without_new_lines = the_html.replace("\n", "")

        self.assertRegexpMatches(without_new_lines, str1 + r".*" + str2)
