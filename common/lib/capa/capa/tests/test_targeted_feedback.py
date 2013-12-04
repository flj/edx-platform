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
        problem.seed = 723
        the_html = problem.get_html()
        self.assertRegexpMatches(the_html, r"<div>.*\[.*'wrong-3'.*'wrong-1'.*'wrong-2'.*'correct-2'.*\].*</div>")

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
