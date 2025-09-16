# Quiz Statistics

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Statistics API

API for accessing quiz submission statistics. The statistics provided by this interface are an aggregate of what is known as Student and Item Analysis for a quiz.

These statistics are extracted (and composed) from _graded_ (manually or, when viable, automatically) submissions for a quiz and provide an insight into how the participant students had responded to each question, as well as insights into the reception of each question answer individually.

Some of these statistics are exclusive to Multiple Choice and True/False types of questions, others to other question types. See {Appendix: Question Specific Statistics} for a reference of these statistics.

**A QuizStatistics object looks like:**

```js
{
  // The ID of the quiz statistics report.
  "id": 1,
  // The ID of the Quiz the statistics report is for. 
  // NOTE: AVAILABLE ONLY IN NON-JSON-API REQUESTS.
  "quiz_id": 2,
  // Whether there are any students that have made mutliple submissions for this
  // quiz.
  "multiple_attempts_exist": true,
  // In the presence of multiple attempts, this field describes whether the
  // statistics describe all the submission attempts and not only the latest ones.
  "includes_all_versions": true,
  // The time at which the statistics were generated, which is usually after the
  // occurrence of a quiz event, like a student submitting it.
  "generated_at": "2013-01-23T23:59:00-07:00",
  // The API HTTP/HTTPS URL to this quiz statistics.
  "url": "http://canvas.example.edu/api/v1/courses/1/quizzes/2/statistics",
  // The HTTP/HTTPS URL to the page where the statistics can be seen visually.
  "html_url": "http://canvas.example.edu/courses/1/quizzes/2/statistics",
  // Question-specific statistics for each question and its answers.
  "question_statistics": null,
  // Question-specific statistics for each question and its answers.
  "submission_statistics": null,
  // JSON-API construct that contains links to media related to this quiz
  // statistics object. 
  // NOTE: AVAILABLE ONLY IN JSON-API REQUESTS.
  "links": null
}
```

**A QuizStatisticsLinks object looks like:**

```js
// Links to media related to QuizStatistics.
{
  // HTTP/HTTPS API URL to the quiz this statistics describe.
  "quiz": "http://canvas.example.edu/api/v1/courses/1/quizzes/2"
}
```

**A QuizStatisticsQuestionStatistics object looks like:**

```js
// Statistics for submissions made to a specific quiz question.
{
  // Number of students who have provided an answer to this question. Blank or
  // empty responses are not counted.
  "responses": 3,
  // Statistics related to each individual pre-defined answer.
  "answers": null
}
```

**A QuizStatisticsAnswerStatistics object looks like:**

```js
// Statistics for a specific pre-defined answer in a Multiple-Choice or
// True/False quiz question.
{
  // ID of the answer.
  "id": 3866,
  // The text attached to the answer.
  "text": "Blue.",
  // An integer to determine correctness of the answer. Incorrect answers should
  // be 0, correct answers should 100
  "weight": 100,
  // Number of students who have chosen this answer.
  "responses": 2
}
```

**A QuizStatisticsAnswerPointBiserial object looks like:**

```js
// A point-biserial construct for a single pre-defined answer in a
// Multiple-Choice or True/False question.
{
  // ID of the answer the point biserial is for.
  "answer_id": 3866,
  // The point biserial value for this answer. Value ranges between -1 and 1.
  "point_biserial": -0.802955068546966,
  // Convenience attribute that denotes whether this is the correct answer as
  // opposed to being a distractor. This is mutually exclusive with the
  // `distractor` value
  "correct": true,
  // Convenience attribute that denotes whether this is a distractor answer and
  // not the correct one. This is mutually exclusive with the `correct` value
  "distractor": false
}
```

**A QuizStatisticsSubmissionStatistics object looks like:**

```js
// Generic statistics for all submissions for a quiz.
{
  // The number of students who have taken the quiz.
  "unique_count": 3,
  // The mean of the student submission scores.
  "score_average": 4.33333333333333,
  // The highest submission score.
  "score_high": 6,
  // The lowest submission score.
  "score_low": 3,
  // Standard deviation of the submission scores.
  "score_stdev": 1.24721912892465,
  // A percentile distribution of the student scores, each key is the percentile
  // (ranges between 0 and 100%) while the value is the number of students who
  // received that score.
  "scores": {"50":1,"34":5,"100":1},
  // The mean of the number of questions answered correctly by each student.
  "correct_count_average": 3.66666666666667,
  // The mean of the number of questions answered incorrectly by each student.
  "incorrect_count_average": 5,
  // The average time spent by students while taking the quiz.
  "duration_average": 42.333333333
}
```

### [Fetching the latest quiz statistics](#method.quizzes/quiz_statistics.index) <a href="#method.quizzes-quiz_statistics.index" id="method.quizzes-quiz_statistics.index"></a>

[Quizzes::QuizStatisticsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_statistics_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/statistics`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/statistics`

This endpoint provides statistics for all quiz versions, or for a specific quiz version, in which case the output is guaranteed to represent the _latest_ and most current version of the quiz.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

| Parameter      | Type      | Description                                                            |
| -------------- | --------- | ---------------------------------------------------------------------- |
| `all_versions` | `boolean` | Whether the statistics report should include all submissions attempts. |

**Example Response:**

```js
{
  "quiz_statistics": [ QuizStatistics ]
}
```

### Appendixes

#### Appendix: Question Specific Statistics <a href="#questionspecificstatistics-appendix" id="questionspecificstatistics-appendix"></a>

Based on the question type it represents, the `question_statistics` document may include extra metrics. You can find these metrics below.

**Multiple Choice**

```
{
  // Number of students who have picked any choice.
  "responses": 4,

  "answers": [
    {
      // Unique ID of this answer.
      "id": "3866",

       // The readable answer text.
      "text": "Red",

       // Number of students who picked this answer.
      "responses": 3,

       // Whether this answer is a correct one.
      "correct": true
    },

    // An incorrect choice:
    {
      "id": "2040",
      "text": "Green",
      "correct": false,
      "responses": 1
    },

    // The "No Answer" - students who didn't make any choice:
    {
      "id": "none",
      "text": "No Answer",
      "responses": 2,
      "correct": false
    }
  ],

  // Number of students who have answered this question.
  "answered_student_count": 0,

  // Number of students who rank in the top bracket (the top 27%)
  // among the submitters which have also answered this question.
  "top_student_count": 0,

  // Number of students who rank in the middle bracket (the middle 46%)
  // among the submitters which have also answered this question.
  "middle_student_count": 0,

  // Number of students who rank in the bottom bracket (the bottom 27%)
  // among the submitters which have also answered this question
  "bottom_student_count": 0,

  // Number of students who have answered this question correctly.
  "correct_student_count": 0,

  // Number of students who have answered this question incorrectly.
  "incorrect_student_count": 0,

  // Ratio of students who have answered this question correctly.
  "correct_student_ratio": 0,

  // Ratio of students who have answered this question incorrectly.
  "incorrect_student_ratio": 0,

  // Number of students who rank in the top bracket (the top 27%) among
  // the submitters which have also provided a correct answer to this question.
  "correct_top_student_count": 0,

  // Number of students who rank in the middle bracket (the middle 46%) among
  // the submitters which have also provided a correct answer to this question.
  "correct_middle_student_count": 0,

  // Number of students who rank in the bottom bracket (the bottom 27%) among
  // the submitters which have also provided a correct answer to this question.
  "correct_bottom_student_count": 0,

  // Variance of *all* the scores.
  "variance": 0,

  // Standard deviation of *all* the scores.
  "stdev": 0,

  // Denotes the ratio of students who have answered this question correctly,
  // which should give an indication of how difficult the question is.
  "difficulty_index": 0,

  // The reliability, or internal consistency, coefficient of all the scores
  // as measured by the Cronbach's alpha algorithm. Value ranges between 0 and
  // 1.
  //
  // Note: This metric becomes available only in quizzes with more than fifteen
  // submissions.
  "alpha": null,

  // A point biserial correlation coefficient for each of the question's
  // answers. This metric helps measure the efficiency of an individual
  // question: the calculation looks at the difference between high-scorers
  // who chose this answer and low-scorers who also chose this answer.
  //
  // See the reference above for a description of each field.
  "point_biserials": [
    {
      "answer_id": 3866,
      "point_biserial": null,
      "correct": true,
      "distractor": false
    },
    {
      "answer_id": 2040,
      "point_biserial": null,
      "correct": false,
      "distractor": true
    },
    {
      "answer_id": 7387,
      "point_biserial": null,
      "correct": false,
      "distractor": true
    },
    {
      "answer_id": 4082,
      "point_biserial": null,
      "correct": false,
      "distractor": true
    }
  ]
}
```

**Fill in Multiple Blanks**

```
{
  // Number of students who have filled at least one blank.
  "responses": 2,

  // Number of students who have filled every blank.
  "answered": 2,

  // Number of students who filled all blanks correctly.
  "correct": 1,

  // Number of students who filled one or more blanks correctly.
  "partially_correct": 0,

  // Number of students who didn't fill any blank correctly.
  "incorrect": 1,

  // Each entry in the answer set represents a blank and responses to
  // its pre-defined answers:
  "answer_sets": [
    {
      "id": "70dda5dfb8053dc6d1c492574bce9bfd", // md5sum of the blank
      "text": "color", // the blank_id
      "answers": [
        // Students who filled in this blank with this correct answer:
        {
          "id": "9711",
          "text": "Red",
          "responses": 3,
          "correct": true
        },
        // Students who filled in this blank with this other correct answer:
        {
          "id": "2700",
          "text": "Blue",
          "responses": 0,
          "correct": true
        },
        // Students who filled in this blank with something else:
        {
          "id": "other",
          "text": "Other",
          "responses": 1,
          "correct": false
        },
        // Students who left this blank empty:
        {
          "id": "none",
          "text": "No Answer",
          "responses": 1,
          "correct": false
        }
      ]
    }
  ]
}
```

**Multiple Answers**

```
{
  // Number of students who have picked any choice.
  "responses": 3,

  // Number of students who have picked all the right choices.
  "correct": 1,

  // Number of students who have picked at least one of the right choices,
  // but may have also picked a wrong one.
  "partially_correct": 2,

  "answers": [
    {
      // Unique ID of this answer choice.
      "id": "5514",

      // Displayable choice text.
      "text": "A",

      // Number of students who picked this choice.
      "responses": 3,

      // Whether this choice is part of the answer.
      "correct": true
    },
    // Here's the second part of the correct answer:
    {
      "id": "4261",
      "text": "B",
      "responses": 1,
      "correct": true
    },

    // And here's a distractor:
    {
      "id": "3322",
      "text": "C",
      "responses": 2,
      "correct": false
    },

    // "Missing" answers:
    //
    // This is an auto-generated answer to account for all students who
    // left this question unanswered.
    {
      "id": "none",
      "text": "No Answer",
      "responses": 0,
      "correct": false
    }
  ]
}
```

**Multiple Dropdowns**

Multiple Dropdown question statistics look just like the statistics for [Fill In Multiple Blanks](#fimb-question-stats).

**Essay**

```
{
   // The number of students whose responses were graded by the teacher so
   // far.
   "graded": 5,

   // The number of students who got graded with a full score.
   "full_credit": 4,

   // Number of students who wrote any kind of answer.
   "resposes": 5,

   // A set of maps of scores and the number of students who received
   // each score.
   "point_distribution": [
     { "score": 0, "count": 1 },
     { "score": 1, "count": 1 },
     { "score": 3, "count": 3 }
   ]
}
```

**Matching**

```
{
  // Number of students who have matched at least one answer.
  "responses": 2,

  // Number of students who have matched all answers.
  "answered": 2,

  // Number of students who have matched all answers correctly with their
  // right-hand sides.
  "correct": 1,

  // Number of students who have matched one or more answers correctly
  // with their right-hand sides.
  "partially_correct": 0,

  // Number of students who have not matched any answer with their correct
  // right-hand side.
  "incorrect": 1,

  // Each entry in the answer set represents the left-hand side of the match
  // along with all the possible matches on the right-side
  "answer_sets": [
    {
      // id of the answer
      "id": "1",
      // the left-hand side of the match
      "text": "What does the color red look like?",
      // the available matches
      "answers": [
        // Students who chose this match for this answer set:
        {
          // match_id
          "id": "9711",
          // right-hand side of the match
          "text": "Red",
          "responses": 3,
          "correct": true
        },
        // Students who chose an incorrect match:
        {
          "id": "2700",
          "text": "Blue",
          "responses": 0,
          "correct": false
        },
        // Students who did not make any match:
        {
          "id": "none",
          "text": "No Answer",
          "responses": 1,
          "correct": false
        }
      ]
    }
  ]
}
```

**File Upload**

File Upload question statistics look just like the statistics for [Essays](#essay-question-stats).

**Formula**

Formula question statistics look just like the statistics for [Essays](#essay-question-stats).

**Numerical**

```
{
  // Number of students who have provided any kind of answer.
  "responses": 2,

  // Number of students who have provided a correct answer.
  "correct": 1,

  // Number of students who have provided a correct answer and received full
  // credit or higher.
  "full_credit": 2,

  // Number of students who have provided an answer which was not correct.
  "incorrect": 1,

  "answers": [
    {
      // Unique ID of this answer.
      "id": "9711",

      // This metric contains a formatted version of the correct answer
      // ready for display.
      "text": "15.00",

      // Number of students who provided this answer.
      "responses": 3,

      // Whether this answer is a correct one.
      "correct": true,

      // Lower and upper boundaries of the answer range. This is consistent
      // regardless of the answer type (e.g., exact vs range).
      //
      // In the case of exact answers, the range will be the exact value
      // minus plus the defined margin.
      "value": [ 13.5, 16.5 ],

      // Margin of error tolerance. This is always zero for range answers.
      "margin": 1.5
    },

    // "Other" answers:
    //
    // This is an auto-generated answer that will be present if any student
    // provides a number for an answer that is incorrect (doesn't map to
    // any of the pre-defined answers.)
    {
      "id": "other",
      "text": "Other",
      "responses": 0,
      "correct": false
    },

    // "Missing" answers:
    //
    // This is an auto-generated answer to account for all students who
    // left this question unanswered.
    {
      "id": "none",
      "text": "No Answer",
      "responses": 0,
      "correct": false
    }
  ]
}
```

#### Short Answer (aka Fill in The Blank) <a href="#short-answer-aka-fill-in-the-blank" id="short-answer-aka-fill-in-the-blank"></a>

```
{
  // Number of students who have written anything.
  "responses": 2,

  // Number of students who have written a correct answer.
  "correct": 2,

  "answers": [
    {
      // Unique ID of this answer.
      "id": "4684",

       // The readable answer text.
      "text": "Something",

       // Number of students who picked this answer.
      "responses": 3,

       // Whether this answer is a correct one.
      "correct": true
    },

    // Another correct answer:
    {
      "id": "1797",
      "text": "Very cool.",
      "responses": 0,
      "correct": true
    },

    // "Other" answers:
    //
    // This is an auto-generated answer that will be present if any student
    // does write an answer, but is incorrect.
    {
      "id": "other",
      "text": "Other",
      "responses": 0,
      "correct": false
    },

    // "Missing" answers:
    //
    // This is an auto-generated answer to account for all students who
    // left this question unanswered.
    {
      "id": "none",
      "text": "No Answer",
      "responses": 0,
      "correct": false
    }
  ]
}
```

**True/False**

True/False question statistics look just like the statistics for [Multiple-Choice](#multiple-choice-question-stats).

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
