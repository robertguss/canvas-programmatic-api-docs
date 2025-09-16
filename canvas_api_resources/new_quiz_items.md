# New Quiz Items

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## New Quiz Items API

API for accessing and building items inside a New Quiz. To interact with the quiz itself, see the [New Quizzes API](new_quizzes).

Glossary:

Quiz Items can be among several types as described here. For now, all types can be retrieved (GET), but some types are restricted to only that functionality.

QuestionItem: question items are the various question types allowed for Quizzes. These question types can be created, updated, retrieved, and deleted with the API. See the Appendix for more details.

StimulusItem: stimulus items are quiz items that define a stimulus that can have associated questions attached to it. For now, stimulus items can only be retrieved with the API. They must be created and updated via the UI.

BankItem: bank items are quiz questions or other items that are part of an item bank. For now, bank items can only be retrieved with the API. They must be created and updated via the UI.

BankEntry: bank entry items allow for a random selection of items from an associated bank to be included in the quiz. For now, bank items can only be retrieved with the API. They must be created and updated via the UI.

**A QuizItem object looks like:**

```js
// Individual items within a quiz, whether they're questions, stimuli, banked
// content, or question banks.
{
  // the ID of the quiz item
  "id": "35",
  // the position of the item within the quiz. The first item in a quiz is given
  // position 1.
  "position": 2,
  // the number of points available to score on this item
  "points_possible": 10.0,
  // the type of the item. One of 'Item', 'Stimulus', 'BankEntry', or 'Bank'.
  "entry_type": "Item",
  // whether the current user can edit the item -- used internally, no need to set
  "entry_editable": true,
  // the ID of the stimulus that this item is associated with. null if not
  // associated with any stimuli.
  "stimulus_quiz_entry_id": "3",
  // status of the item. one of 'mutable' or 'immutable'.  Used internally, no
  // need to set
  "status": "mutable",
  // additional properties for the item (currently only populated by items with a
  // BankItem entry)
  "properties": null,
  // the specific data associated with the quiz item.  These items can be either a
  // QuestionItem, StimulusItem, BankEntryItem, or BankItem, depending on
  // entry_type, and are defined
  // separately
  "entry": null
}
```

**A QuestionItem object looks like:**

```js
{
  // the question title
  "title": "Linear Algebra 1-104",
  // the question content (can include html for rich content)
  "item_body": "<p>What is 3 + 6?</p>",
  // type of calculator the user will have access to during the question ('none',
  // basic' or 'scientific')
  "calculator_type": "none",
  // correct, incorrect, and general feedback for the question (see
  // QuestionFeedback)
  "feedback": null,
  // can be thought of as the question type. One of 'multi-answer', 'matching',
  // 'categorization',
  // 'file-upload', 'formula', 'ordering', 'rich-fill-blank', 'hot-spot',
  // 'choice', 'numeric', 'true-false',
  // 'essay', or 'fill-blank' (deprecated). See Appendix: Question Types for more
  // info about each type.
  "interaction_type_slug": "essay",
  // an object that contains the question data. See Appendix: Question Types for
  // more info about this field.
  "interaction_data": null,
  // an object that contains additional properties for some question types. See
  // Appendix: Question Types for more info about this field.
  "properties": null,
  // describes how to score the question. See Appendix: Question Types for more
  // info about this field.
  "scoring_data": null,
  // feedback provided for each answer (rich content, only available on 'choice'
  // question types)
  "answer_feedback": {"5595b4c2-7dd6-447f-b8f1-9b6d0e0c287a":"\u003cp\u003eClose, but in this case...\u003c\/p\u003e"},
  // the algorithm used to score the question. See Appendix: Question Types for
  // more info about this field.
  "scoring_algorithm": "AllOrNothing"
}
```

**A StimulusItem object looks like:**

```js
{
  // stimulus title
  "title": "Consider the following image",
  // stimulus content (rich content)
  "body": "<img src=... />",
  // additional stimulus instructions
  "instructions": "Some instructions...",
  // optional URL; not visible to students
  "source_url": "https://example.com",
  // where the stimulus appears relative to questions ('top' or 'left')
  "orientation": "left",
  // if the stimulus is treated as a passage (text - no question block)
  "passage": false
}
```

**A BankEntryItem object looks like:**

```js
{
  // the type of the item. Either 'Item' or 'Stimulus'.
  "entry_type": "Item",
  // whether the banked item is archived
  "archived": false,
  // the item (either a QuestionItem or StimulusItem, depending on entry_type)
  "entry": null
}
```

**A BankItem object looks like:**

```js
{
  // the title of the bank
  "title": "Linear Algebra 1-1",
  // whether the bank is archived
  "archived": false,
  // the number of items in the bank, including stimuli
  "entry_count": 20,
  // the number of items in the bank, excluding stimuli
  "item_entry_count": 18
}
```

**An ItemProperties object looks like:**

```js
{
  // for items with a BankItem entry - the number of items to randomly select from
  // the bank. null if all items should be included.
  "sample_num": 5
}
```

**A QuestionFeedback object looks like:**

```js
{
  // general feedback to show regardless of answer (rich content)
  "neutral": "<p>That was a hard one.</p>",
  // feedback to show if the question is answered correctly (rich content)
  "correct": "<p>Nice work!</p>",
  // feedback to show if the question is answered incorrectly (rich content)
  "incorrect": "<p>Remember to start by...</p>"
}
```

### [Get a quiz item](#method.new_quizzes/quiz_items_api.show) <a href="#method.new_quizzes-quiz_items_api.show" id="method.new_quizzes-quiz_items_api.show"></a>

**`GET /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id`**

**Scope:** `url:GET|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id`

Get details about a single item in a new quiz.

**Request Parameters:**

| Parameter       | Type               | Description                                        |
| --------------- | ------------------ | -------------------------------------------------- |
| `course_id`     | Required `integer` | no description                                     |
| `assignment_id` | Required `integer` | The id of the assignment associated with the quiz. |
| `item_id`       | Required `integer` | The id of the item associated with the quiz.       |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12/items/123' \
      -H 'Authorization: Bearer <token>'
```

Returns a [QuizItem](#quizitem) object.

### [List quiz items](#method.new_quizzes/quiz_items_api.index) <a href="#method.new_quizzes-quiz_items_api.index" id="method.new_quizzes-quiz_items_api.index"></a>

**`GET /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items`**

**Scope:** `url:GET|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items`

Get a list of items in a new quiz.

**Request Parameters:**

| Parameter       | Type               | Description    |
| --------------- | ------------------ | -------------- |
| `course_id`     | Required `integer` | no description |
| `assignment_id` | Required `integer` | no description |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/1/items' \
     -H 'Authorization Bearer <token>'
```

Returns a list of [QuizItem](#quizitem) objects.

### [Create a quiz item](#method.new_quizzes/quiz_items_api.create) <a href="#method.new_quizzes-quiz_items_api.create" id="method.new_quizzes-quiz_items_api.create"></a>

**`POST /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items`**

**Scope:** `url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items`

Create a quiz item in a new quiz. Only `QuestionItem` types can be created.

**Request Parameters:**

| Parameter                            | Type               | Description                                                                                                                                                                                                                                                                            |
| ------------------------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `course_id`                          | Required `integer` | no description                                                                                                                                                                                                                                                                         |
| `assignment_id`                      | Required `integer` | The id of the assignment associated with the quiz.                                                                                                                                                                                                                                     |
| `item[position]`                     | `integer`          | The position of the item within the quiz.                                                                                                                                                                                                                                              |
| `item[points_possible]`              | `number`           | The number of points available to score on this item. Must be positive.                                                                                                                                                                                                                |
| `item[entry_type]`                   | Required `string`  | <p>The type of the item.</p><p>Allowed values: <code>Item</code></p>                                                                                                                                                                                                                   |
| `item[entry][title]`                 | `string`           | The question title.                                                                                                                                                                                                                                                                    |
| `item[entry][item_body]`             | Required `string`  | The question stem (rich content).                                                                                                                                                                                                                                                      |
| `item[entry][calculator_type]`       | `string`           | <p>Type of calculator the user will have access to during the question.</p><p>Allowed values: <code>none</code>, <code>basic</code>, <code>scientific</code></p>                                                                                                                       |
| `item[entry][feedback][neutral]`     | `string`           | General feedback to show regardless of answer (rich content).                                                                                                                                                                                                                          |
| `item[entry][feedback][correct]`     | `string`           | Feedback to show if the question is answered correctly (rich content).                                                                                                                                                                                                                 |
| `item[entry][feedback][incorrect]`   | `string`           | Feedback to show if the question is answered incorrectly (rich content).                                                                                                                                                                                                               |
| `item[entry][interaction_type_slug]` | Required `string`  | The type of question. One of ‘multi-answer’, ‘matching’, ‘categorization’, ‘file-upload’, ‘formula’, ‘ordering’, ‘rich-fill-blank’, ‘hot-spot’, ‘choice’, ‘numeric’, ‘true-false’, or ‘essay’. See [Appendix: Question Types](#Question+Types-appendix) for more info about each type. |
| `item[entry][interaction_data]`      | Required `Object`  | An object that contains the question data. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                                                    |
| `item[entry][properties]`            | `Object`           | An object that contains additional properties for some question types. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                        |
| `item[entry][scoring_data]`          | Required `Object`  | An object that describes how to score the question. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                                           |
| `item[entry][answer_feedback]`       | `Object`           | Feedback provided for each answer (rich content, only available on ‘choice’ question types).                                                                                                                                                                                           |
| `item[entry][scoring_algorithm]`     | Required `string`  | The algorithm used to score the question. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                                                     |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12/items' \
     -X POST \
     -H 'Authorization Bearer <token>' \
     -d 'item[position]=1' \
     -d 'item[points_possible]=25.0' \
     -d 'item[properties]={}' \
     -d 'item[entry_type]=Item' \
     -d 'item[entry][title]=Question 1' \
     -d 'item[entry][feedback][correct]=good job!' \
     -d 'item[entry][calculator_type]=none' \
     -d 'item[entry][interaction_data][word_limit_enabled]=true' \
     -d 'item[entry][item_body]=<p>What is 3 ^ 6?</p>' \
     -d 'item[entry][interaction_type_slug]=essay' \
     -d 'item[entry][scoring_data][value]=' \
     -d 'item[entry][scoring_algorithm]=None'
```

Returns a [QuizItem](#quizitem) object.

### [Update a quiz item](#method.new_quizzes/quiz_items_api.update) <a href="#method.new_quizzes-quiz_items_api.update" id="method.new_quizzes-quiz_items_api.update"></a>

**`PATCH /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id`**

**Scope:** `url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id`

Update a single quiz item in a new quiz. Only `QuestionItem` types can be updated.

**Request Parameters:**

| Parameter                            | Type               | Description                                                                                                                                                                                                                                                                            |
| ------------------------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `course_id`                          | Required `integer` | no description                                                                                                                                                                                                                                                                         |
| `assignment_id`                      | Required `integer` | The id of the assignment associated with the quiz.                                                                                                                                                                                                                                     |
| `item_id`                            | Required `integer` | The id of the item associated with the quiz.                                                                                                                                                                                                                                           |
| `item[position]`                     | `integer`          | The position of the item within the quiz.                                                                                                                                                                                                                                              |
| `item[points_possible]`              | `number`           | The number of points available to score on this item. Must be positive.                                                                                                                                                                                                                |
| `item[entry_type]`                   | `string`           | <p>The type of the item.</p><p>Allowed values: <code>Item</code></p>                                                                                                                                                                                                                   |
| `item[entry][title]`                 | `string`           | The question title.                                                                                                                                                                                                                                                                    |
| `item[entry][item_body]`             | `string`           | The question stem (rich content).                                                                                                                                                                                                                                                      |
| `item[entry][calculator_type]`       | `string`           | <p>Type of calculator the user will have access to during the question.</p><p>Allowed values: <code>none</code>, <code>basic</code>, <code>scientific</code></p>                                                                                                                       |
| `item[entry][feedback][neutral]`     | `string`           | General feedback to show regardless of answer (rich content).                                                                                                                                                                                                                          |
| `item[entry][feedback][correct]`     | `string`           | Feedback to show if the question is answered correctly (rich content).                                                                                                                                                                                                                 |
| `item[entry][feedback][incorrect]`   | `string`           | Feedback to show if the question is answered incorrectly (rich content).                                                                                                                                                                                                               |
| `item[entry][interaction_type_slug]` | `string`           | The type of question. One of ‘multi-answer’, ‘matching’, ‘categorization’, ‘file-upload’, ‘formula’, ‘ordering’, ‘rich-fill-blank’, ‘hot-spot’, ‘choice’, ‘numeric’, ‘true-false’, or ‘essay’. See [Appendix: Question Types](#Question+Types-appendix) for more info about each type. |
| `item[entry][interaction_data]`      | `Object`           | An object that contains the question data. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                                                    |
| `item[entry][properties]`            | `Object`           | An object that contains additional properties for some question types. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                        |
| `item[entry][scoring_data]`          | `Object`           | An object that describes how to score the question. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                                           |
| `item[entry][answer_feedback]`       | `Object`           | Feedback provided for each answer (rich content, only available on ‘choice’ question types).                                                                                                                                                                                           |
| `item[entry][scoring_algorithm]`     | `string`           | The algorithm used to score the question. See [Appendix: Question Types](#Question+Types-appendix) for more info about this field.                                                                                                                                                     |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12/items/145' \
     -X PATCH \
     -H 'Authorization Bearer <token>' \
     -d 'item[points_possible]=25.0' \
     -d 'item[entry][title]=Question 1' \
     -d 'item[entry][calculator_type]=scientific'
```

Returns a [QuizItem](#quizitem) object.

### [Delete a quiz item](#method.new_quizzes/quiz_items_api.destroy) <a href="#method.new_quizzes-quiz_items_api.destroy" id="method.new_quizzes-quiz_items_api.destroy"></a>

**`DELETE /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id`**

**Scope:** `url:DELETE|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id`

Delete a single quiz item in a new quiz.

**Request Parameters:**

| Parameter       | Type               | Description                                        |
| --------------- | ------------------ | -------------------------------------------------- |
| `course_id`     | Required `integer` | no description                                     |
| `assignment_id` | Required `integer` | The id of the assignment associated with the quiz. |
| `item_id`       | Required `integer` | The id of the item associated with the quiz.       |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12/items/123' \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Returns a [QuizItem](#quizitem) object.

### [Get items media\_upload\_url](#method.new_quizzes/quiz_items_api.media_upload_url) <a href="#method.new_quizzes-quiz_items_api.media_upload_url" id="method.new_quizzes-quiz_items_api.media_upload_url"></a>

**`GET /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/media_upload_url`**

**Scope:** `url:GET|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/media_upload_url`

Get a url for uploading media for use in hot-spot question types. See the hot-spot question type in the [Appendix: Question Types](#Question+Types-appendix) for more details about using this endpoint.

**Request Parameters:**

| Parameter       | Type               | Description    |
| --------------- | ------------------ | -------------- |
| `course_id`     | Required `integer` | no description |
| `assignment_id` | Required `integer` | no description |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/1/items/media_upload_url' \
     -H 'Authorization Bearer <token>'
```

**Example Response:**

```js
{ "url": "http://s3_upload_url" }
```

### Appendixes

#### Appendix: Question Types <a href="#questiontypes-appendix" id="questiontypes-appendix"></a>

The quiz items API retrieves and manages the quiz items associated with a quiz such as question types, stimulus items, and item bank entries. This supplemental data describes the specific quiz item data for question types.

Some data creation for quiz items must include UUID values. These UUIDs must be generated properly when creating question types that require them. An online generator, such as [https://www.uuidgenerator.net/](https://www.uuidgenerator.net/), can be used to generate one or more UUIDs. A Version 4 UUID is recommended.

A complete example of a JSON request body for a `choice` question type is provided below. More details about each of the 13 question types are provided afterwards.

Example request body for `choice` question:

```
// Set `Content-Type` request header to `application/json`
{
    "item": {
        "entry_type": "Item",
        "points_possible": 10,
        "position": 1,
        "entry": {
            "interaction_type_slug": "choice",
            "title": "Science 1-13",
            "item_body": "<p>Which part of the cell contains the majority of the cell's DNA?</p>",
            "calculator_type": "none",
            "interaction_data": {
                "choices": [
                    {
                        "id": "96e68487-086e-4a0b-9a70-0ad623c83aa3",
                        "position": 1,
                        "itemBody": "<p>nucleus</p>"
                    },
                    {
                        "id": "1bd82f75-b070-477d-bea6-b954ef766fbf",
                        "position": 2,
                        "itemBody": "<p>mitochondria</p>"
                    },
                    {
                        "id": "2f035bad-5ad3-488b-b8de-034ac4123138",
                        "position": 3,
                        "itemBody": "<p>cell membrane</p>"
                    },
                    {
                        "id": "db5fd86c-2132-4e6f-be54-a3b61aab2eec",
                        "position": 4,
                        "itemBody": "<p>cytoplasm</p>"
                    }
                ]
            },
            "properties": {
                "shuffleRules": {
                    "choices": {
                        "toLock": [],
                        "shuffled": true
                    }
                },
                "varyPointsByAnswer": false
            },
            "scoring_data": {
                "value": "96e68487-086e-4a0b-9a70-0ad623c83aa3"
            },
            "scoring_algorithm": "Equivalence",
            "feedback": {
                "correct": "<p>Nice job!</p>",
                "incorrect": "<p>Study textbook pg. 105 for more information about the cell.</p>"
            },
            "answer_feedback": {
                "1bd82f75-b070-477d-bea6-b954ef766fbf": "<p>A small amount of DNA (mitochondrial DNA) can be found here, but most DNA is located in the cell's nucleus.</p>"
            }
        }
    }
}
```

Details about each question type:

| Question Type                                   | Interaction Type Slug | Interaction Data | Properties    | Scoring Algorithm                 | Answer Feedback |
| ----------------------------------------------- | --------------------- | ---------------- | ------------- | --------------------------------- | --------------- |
| [True/False](#true-false)                       | true-false            | Yes              | No            | Equivalence                       | No              |
| [Categorization](#categorization)               | categorization        | Yes              | Yes           | Categorization                    | No              |
| [Matching](#matching)                           | matching              | Yes              | Yes           | DeepEquals or PartialDeep         | No              |
| [File Upload](#file-upload)                     | file-upload           | Yes              | Yes           | None                              | No              |
| [Formula](#formula)                             | formula               | No               | No            | Numeric                           | No              |
| [Ordering](#ordering)                           | ordering              | Yes              | Yes           | DeepEquals                        | No              |
| [Fill in the Blank (current)](#rich-fill-blank) | rich-fill-blank       | Yes              | Yes           | MultipleMethods                   | No              |
| [Hot Spot](#hot-spot)                           | hot-spot              | Yes              | No            | HotSpot                           | No              |
| [Multiple Choice](#choice)                      | choice                | Yes              | Yes           | Equivalence or VaryPointsByAnswer | Yes             |
| [Multiple Answer](#multi-answer)                | multi-answer          | Yes              | Yes           | AllOrNothing or PartialScore      | No              |
| [Numeric](#numeric)                             | numeric               | No               | No            | Numeric                           | No              |
| [Essay](#essay)                                 | essay                 | Yes              | No            | None                              | No              |
| [Fill in the Blank (deprecated)](#fill-blank)   | fill-blank            | Yes              | Yes (sort of) | MultipleMethods                   | No              |

**True/False**

**Interaction Data**

```
"interaction_data": {
    // The value of the true choice
    "true_choice": "True",
    // The value of the false choice
    "false_choice": "False"
}
```

**Scoring Data**

```
"scoring_data": {
    // The correct answer value
    "value": true
 }
```

**Categorization**

**Interaction Data**

Categorization Interaction Data includes categories, distractors, and a category order for the categories

```
"interaction_data": {
  // All the categories
  "categories": {
      // UUID generated or set for a category.  Also the id value
      "6c33f1dd-1d28-413f-bba1-80fcdc96f36e": {
          // the UUID id of this category 
          "id": "6c33f1dd-1d28-413f-bba1-80fcdc96f36e",
          // the text provided for this category   
          "item_body": "fish"
      },
      "730a9fc7-1960-4318-a615-aa45a48890f8": {
          "id": "730a9fc7-1960-4318-a615-aa45a48890f8",
          "item_body": "dogs"
      },
      "e02d9e14-eedc-4ec4-b7f9-d4ad73880e1e": {
          "id": "e02d9e14-eedc-4ec4-b7f9-d4ad73880e1e",
          "item_body": "cats"
      }
  },
  // The distractors section contains all the answers for the cateogries -- correct AND incorrect.
  // Category and correct answers are combined in the scoring_data section.
  // The UUIDs are generated and used also for the id.
  "distractors": {
      // the UUID id of this category
      "1cb5ec30-3c40-4450-92f2-d1d82699df77": {
          // same UUID 
          "id": "1cb5ec30-3c40-4450-92f2-d1d82699df77",
          // the text provided for a right OR wrong answer.  
          "item_body": "trout"
      },
      "60c98d76-7eea-4d05-92cf-9f9fa4383a41": {
          "id": "60c98d76-7eea-4d05-92cf-9f9fa4383a41",
          "item_body": "perch"
      },
      // this particular answer is a wrong answer but mixed in with the rest of the answers in this section
      "6fa85876-cb98-4576-b88d-4ed9452598b4": {
          "id": "6fa85876-cb98-4576-b88d-4ed9452598b4",
          "item_body": "hereford"
      },
      "cbbc431b-de52-455b-b69d-6e3e63b4e8d1": {
          "id": "cbbc431b-de52-455b-b69d-6e3e63b4e8d1",
          "item_body": "siamese"
      },
      "d3e17af4-ac1c-46dc-ba90-ebe855f6523a": {
          "id": "d3e17af4-ac1c-46dc-ba90-ebe855f6523a",
          "item_body": "labrador retriever"
      },
      "eaf77e74-d018-4382-9871-2afb8c036358": {
          "id": "eaf77e74-d018-4382-9871-2afb8c036358",
          "item_body": "shih tzu"
      },
      "fb6219ca-3a3e-4640-8ce3-01a7be49768e": {
          "id": "fb6219ca-3a3e-4640-8ce3-01a7be49768e",
          "item_body": "persian"
      }
  },
  // list of category UUIDs in the order the categories are shown on UI
  "category_order": [
      "730a9fc7-1960-4318-a615-aa45a48890f8",
      "e02d9e14-eedc-4ec4-b7f9-d4ad73880e1e",
      "6c33f1dd-1d28-413f-bba1-80fcdc96f36e"
  ]
}
```

**Properties**

```
// potential shuffle rules for questions
"shuffle_rules": {
    // questions could be shuffled but the value is currently always false
    "questions": {
        // shuffled boolean value
        "shuffled": false
    }
}
```

**Scoring Data**

```
"scoring_data": {
  // A category and its correct answers provided as UUID values
  "value": [
      {
          // the UUID of a category
          "id": "730a9fc7-1960-4318-a615-aa45a48890f8",
          "scoring_data": {
              // the UUIDs of all the correct answers
              "value": [
                  "d3e17af4-ac1c-46dc-ba90-ebe855f6523a",
                  "eaf77e74-d018-4382-9871-2afb8c036358"
              ]
          },
          // The algorithm used for category answer scoring.  No partial credit.
          "scoring_algorithm": "AllOrNothing"
      },
      {
          "id": "e02d9e14-eedc-4ec4-b7f9-d4ad73880e1e",
          "scoring_data": {
              "value": [
                  "fb6219ca-3a3e-4640-8ce3-01a7be49768e",
                  "cbbc431b-de52-455b-b69d-6e3e63b4e8d1"
              ]
          },
          "scoring_algorithm": "AllOrNothing"
      },
      {
          "id": "6c33f1dd-1d28-413f-bba1-80fcdc96f36e",
          "scoring_data": {
              "value": [
                  "60c98d76-7eea-4d05-92cf-9f9fa4383a41",
                  "1cb5ec30-3c40-4450-92f2-d1d82699df77"
              ]
          },
          "scoring_algorithm": "AllOrNothing"
      }
  ],
  "score_method": "all_or_nothing"
}
```

**Multiple Answer**

Multiple Answer question types provide two or more selections with one or more correct answers.

**Interaction Data**

```
"interaction_data": {
    // List of potential choices
    "choices": [
        {
            // a unique UUID to identify this choice
            "id": "86c4f713-94fe-4adf-9c2c-972d68f6e739",
            // the position in the UI for this choice
            "position": 1,
            // the text provided for this choice
            "item_body": "<p>q</p>"
        },
        {
            "id": "74519fce-1eae-49e9-9d33-7d796ba932b9",
            "position": 2,
            "item_body": "<p>u</p>"
        },
        {
            "id": "bfc8853b-f755-4284-8650-21f322406f07",
            "position": 3,
            "item_body": "<p>i</p>"
        },
        {
            "id": "121f36af-1c2f-487f-9fdf-6af172c81881",
            "position": 4,
            "item_body": "<p>t</p>"
        }
    ]
}
```

**Properties**

```
"properties": {
    "shuffle_rules": {
        "choices": {
            // list of choices that are locked in place in position based on position going from 0-n
            "to_lock": [
                0,
                2
            ],
            // shuffle the choices if true
            "shuffled": true
        }
    }
}
```

**Scoring Data**

```
"scoring_data": {
    // the list of UUID choices that are the correct answers
    "value": [
        "86c4f713-94fe-4adf-9c2c-972d68f6e739",
        "74519fce-1eae-49e9-9d33-7d796ba932b9"
    ]
}
```

**Matching**

**Interaction Data**

```
"interaction_data": {
    // List of string answers
    "answers": [
        "bb",
        "cc",
        "ee",
        "aa",
        "dd",
        "ff"
    ],
    "questions": [
        {
            // unique id
            "id": "10586",
            // question body string
            "item_body": "a"
        },
        {
            "id": "55422",
            "item_body": "b"
        },
        {
            "id": "69036",
            "item_body": "c"
        },
        {
            "id": "38821",
            "item_body": "d"
        },
        {
            "id": "cea4d0a4-fb00-4134-a78f-9bf5e96baac7",
            "item_body": "e"
        }
    ]
}
```

**Properties**

```
"properties": {
    "shuffle_rules": {
        "questions": {
            // Shuffle the questions if true
            "shuffled": true
        }
    }
}
```

**Scoring Data**

```
"scoring_data": {
    // set of question ids matched to correct answer
    "value": {
        "10586": "aa",
        "38821": "dd",
        "55422": "bb",
        "69036": "cc",
        "cea4d0a4-fb00-4134-a78f-9bf5e96baac7": "ee"
    },
    "edit_data": {
        // List of matches
        "matches": [
            {
                // Answer body text matched to question id value and question text
                "answer_body": "aa",
                "question_id": "10586",
                "question_body": "a"
            },
            {
                "answer_body": "bb",
                "question_id": "55422",
                "question_body": "b"
            },
            {
                "answer_body": "cc",
                "question_id": "69036",
                "question_body": "c"
            },
            {
                "answer_body": "dd",
                "question_id": "38821",
                "question_body": "d"
            },
            {
                "answer_body": "ee",
                "question_id": "cea4d0a4-fb00-4134-a78f-9bf5e96baac7",
                "question_body": "e"
            }
        ],
        // List of distractors that are wrong answers
        "distractors": [
            "ff"
        ]
    }
}
```

**File Upload**

**Interaction Data**

```
"interaction_data": {
    // Number of files allowed for upload
    "files_count": "3",
    // The number of files to update is retricted to the count if true
    "restrict_count": true
}
```

**Properties**

```
"properties": {
    // Comma separated list of allow file suffixes for upload
    "allowed_types": ".png,.jpg",
    // Restrict the types allowed for upload if true
    "restrict_types": true
}
```

**Scoring Data**

Scoring data is essentially nil with this data structure

```
"scoring_data": {
    "value": ""
}
```

**Formula**

**Interaction Data**

```
"interaction_data": {}
```

**Properties**

```
"properties": {}
```

**Scoring Data**

```
"scoring_data": {
    "value": {
        // Formula used to perform calculation
        "formula": "2 + y",
        // Type of formula calculation
        "numeric": {
            // Type of match for answer
            "type": "marginOfError",
            // Amount of margin of error
            "margin": "0",
            // Type of margin (absolute or percent)
            "margin_type": "absolute"
        },
        "variables": [
            {
                // Max value of potential generated value
                "max": "100",
                // Min value of potential generated value
                "min": "-100",
                // Name of the variable used
                "name": "y",
                // Precision in number of decimals
                "precision": 0
            }
        ],
        // Number of generated answers
        "answer_count": "3",
        // List of generated solutions
        "generated_solutions": [
            {
                "inputs": [
                    {
                        // Variable name given the value
                        "name": "y",
                        // Value
                        "value": "-95"
                    }
                ],
                // Answer of generated solution
                "output": "-93"
            },
            {
                "inputs": [
                    {
                        "name": "y",
                        "value": "-25"
                    }
                ],
                "output": "-23"
            },
            {
                "inputs": [
                    {
                        "name": "y",
                        "value": "86"
                    }
                ],
                "output": "88"
            },
        ]
    }
}
```

**Ordering**

**Interaction Data**

```
"interaction_data": {
    // Ordering choices in correct order
    "choices": {
        // Generated Version 4 UUID as a key and id value
        "4bc7fc95-00b5-4d2b-80c1-9e4177d6a122": {
            // id for this choice that is Version 4 UUID same as key for this entry
            "id": "4bc7fc95-00b5-4d2b-80c1-9e4177d6a122",
            // The string body of the selection.  Can be rich text
            "item_body": "<p>ava</p>"
        },
        "5b6d6d9d-a3d8-4153-9435-59ede6021d77": {
            "id": "5b6d6d9d-a3d8-4153-9435-59ede6021d77",
            "item_body": "<p>blake</p>"
        },
        "bd36e96c-ef4b-4325-84f4-efbc4711b041": {
            "id": "bd36e96c-ef4b-4325-84f4-efbc4711b041",
            "item_body": "<p>skylar</p>"
        },
        "db265c86-6c74-45ac-b3e3-9ab6257968f2": {
            "id": "db265c86-6c74-45ac-b3e3-9ab6257968f2",
            "item_body": "<p>robin</p>"
        },
        "ee899604-5b73-4c78-84f1-36f4ec065f6c": {
            "id": "ee899604-5b73-4c78-84f1-36f4ec065f6c",
            "item_body": "<p>joy</p>"
        },
        "ffd8e44c-10c5-45e8-9f83-075957e23da6": {
            "id": "ffd8e44c-10c5-45e8-9f83-075957e23da6",
            "item_body": "<p>ray</p>"
        }
    }
}
```

**Properties**

```
"properties": {
    // String providing a label at the top of the list to order
    "top_label": "youngest",
    // String providing a label at the bottom of the list to order
    "bottom_label": "oldest",
    // shuffle rules is a null only value
    "shuffle_rules": null,
    // boolean for determining if labels are to be provided
    "include_labels": true,
    // boolean for determining if list should be in a paragraph (true) or list (false) format
    "display_answers_paragraph": false
}
```

**Scoring Data**

```
"scoring_data": {
    // List of choice UUIDs in order for scoring purposes
    "value": [
        "bd36e96c-ef4b-4325-84f4-efbc4711b041",
        "4bc7fc95-00b5-4d2b-80c1-9e4177d6a122",
        "ee899604-5b73-4c78-84f1-36f4ec065f6c",
        "5b6d6d9d-a3d8-4153-9435-59ede6021d77",
        "db265c86-6c74-45ac-b3e3-9ab6257968f2",
        "ffd8e44c-10c5-45e8-9f83-075957e23da6"
    ]
}
```

**Rich Fill In The Blank**

**Interaction Data**

```
"interaction_data": {
    "blanks": [
        {
            // Generated Version 4 UUID identifying the fill in the blank entry
            "id": "5f7d7773-7638-4192-98f2-7d49d616e995",
            // type of entry (openEntry, dropdown, wordbank)
            "answer_type": "openEntry"
        },
        {
            "id": "53edba05-1e4c-4222-87e9-4cb50cde550a",
            "answer_type": "openEntry"
        },
        {
            "id": "0ca4868f-6bee-49a9-8629-3fbc7b130f7b",
            "answer_type": "openEntry"
        },
        {
            "id": "28a7b201-6008-4c1d-8563-d0a77178a3b2",
            "answer_type": "openEntry"
        },
        {
            // Generated Version 4 UUID indicating a blank to fill
            "id": "5e79bac7-a266-4a8c-b97f-f4c53b635fdc",
            "choices": [
                {
                    // Generated Version 4 UUID for this choice
                    "id": "a671d351-11f5-4945-bae8-d294a5a52b3e",
                    // Indicates the position in the dropdown list
                    "position": 1,
                    // Choice string provided to quiz taker
                    "item_body": "pink"
                },
                {
                    "id": "8f3b2038-7ea6-4952-8d50-62740d0353a4",
                    "position": 2,
                    "item_body": "yellow"
                },
                {
                    "id": "1034e755-f34a-488d-a164-e2571935ec7a",
                    "position": 3,
                    "item_body": "green"
                }
            ],
            // Type of answer of openEntry, dropdown, and wordbank
            "answer_type": "dropdown"
        },
        {
            // Generated Version 4 UUID id for fill in the blank item
            "id": "849243d8-6387-461e-84d1-e9d96e2e15e1",
            // choices is null for wordbanks
            "choices": null,
            // Type of answer of openEntry, dropdown, and wordbank
            "answer_type": "wordbank"
        },
        {
            "id": "ff77852b-a784-4ac0-9cc9-d5ee05ecfb83",
            "answer_type": "openEntry"
        }
    ],
    //List of wordbank choices, including correct choice
    "word_bank_choices": [
        {
            // Generated Version 4 UUID id for wordbank choice
            "id": "91c28098-d081-4ca1-b5a5-5ae8049d182f",
            // Choice string presented to quiz taker
            "item_body": "hate"
        },
        {
            "id": "04efdca1-0135-468e-a6aa-c2136987de4b",
            "item_body": "love"
        },
        {
            "id": "eefcf042-eb33-4330-9780-33547c778ad5",
            "item_body": "kinda like"
        }
    ],
    // Boolean value true is word bank choices should be reused.
    "reuse_word_bank_choices": true
}
```

**Properties**

```
"properties": {
    "shuffle_rules": {
        // blanks indicate places where quiz taker must answer in some way, listed from 0-n 
        "blanks": {
            "children": {
                "0": {
                    "children": null
                },
                "1": {
                    "children": null
                },
                "2": {
                    "children": null
                },
                "3": {
                    "children": null
                },
                "4": {
                    "children": {
                        "choices": {
                            // dropdown or wordbank entries will have shuffled answers as indicated here with true
                            "shuffled": true
                        }
                    }
                },
                "5": {
                    "children": {
                        "choices": {
                            "shuffled": true
                        }
                    }
                },
                "6": {
                    "children": null
                }
            }
        }
    }
}
```

**Scoring Data**

```
"scoring_data": {
    "value": [
        {
            // id matching a blank id in interaction_data
            "id": "5f7d7773-7638-4192-98f2-7d49d616e995",
            "scoring_data": {
                // correct answer
                "value": "Roses",
                // what is seen by teacher creating question
                "blank_text": "Roses",
                // decide if case should be ignored
                "ignore_case": true,
                // Levenshtein distance for close enough (how many character places)
                "edit_distance": 1
            },
            // Scoring algorithm for this blank (TextCloseEnough, TextContainsAnswer, TextInChoices,
            // Equivalence, TextEquivalence, TextRegex)
            "scoring_algorithm": "TextCloseEnough"
        },
        {
            "id": "53edba05-1e4c-4222-87e9-4cb50cde550a",
            "scoring_data": {
                "value": "red",
                "blank_text": "red"
            },
            "scoring_algorithm": "TextContainsAnswer"
        },
        {
            "id": "0ca4868f-6bee-49a9-8629-3fbc7b130f7b",
            "scoring_data": {
                "value": "blue",
                "blank_text": "blue"
            },
            "scoring_algorithm": "TextContainsAnswer"
        },
        {
            "id": "28a7b201-6008-4c1d-8563-d0a77178a3b2",
            "scoring_data": {
                // correct value is any of the items in the list
                "value": [
                    "Tulips",
                    "Peonies"
                ],
                "blank_text": "Tulips"
            },
            "scoring_algorithm": "TextInChoices"
        },
        {
            "id": "5e79bac7-a266-4a8c-b97f-f4c53b635fdc",
            "scoring_data": {
                // wordbank correct answer in dropdown list
                "value": "a671d351-11f5-4945-bae8-d294a5a52b3e",
                "blank_text": "pink"
            },
            "scoring_algorithm": "Equivalence"
        },
        {
            "id": "849243d8-6387-461e-84d1-e9d96e2e15e1",
            "scoring_data": {
                // correct answer
                "value": "love",
                // correct item from wordbank
                "choice_id": "04efdca1-0135-468e-a6aa-c2136987de4b",
                "blank_text": "love"
            },
            "scoring_algorithm": "TextEquivalence"
        },
        {
            "id": "ff77852b-a784-4ac0-9cc9-d5ee05ecfb83",
            "scoring_data": {
                // correct answer matches regex value
                "value": "[a-z][a-z][a-z]",
                "blank_text": "you"
            },
            "scoring_algorithm": "TextRegex"
        }
    ],
    // specific text with back ticks indicating which items translate into blanks to fill in
    "working_item_body": "<p>`Roses` are `red`, violets are `blue`</p>\n<p>`Tulips` are `pink`, and I `love` `you`.</p>"
}
```

**Hot Spot**

To create a hotspot question, first upload the image to the url obtained with the media\_upload\_url endpoint. Then create the question item, including the image's url in the item's `interaction_data`. The requests look like this:

1. `GET /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/media_upload_url`. This returns a presigned url for uploading the image.
2.  `PUT <media_upload_url>` with the image included in the request as a data attribute. For example, in cURL:

    ```
    curl --X PUT 'http://quiz.minio.docker/dev-uploads/item_media/1e6f97fc-f56c-4b29-96ac-08474b9bf969/6e5ad29e-119d-4a08-8504-daf088928612?X-Amz-Signature=2c8f37219...' \
    --header 'Content-Type: image/png' \
    --data '@/Documents/"panda".png'
    ```
3.  `POST /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items`, including the _unsigned_ media\_upload\_url in the request's interaction\_data param, like this:

    ```
    {
       "interaction_data": {
           // note: the query params present on the signed url are not included here
           "image_url": "http://quiz.minio.docker/dev-uploads/item_media/1e6f97fc-f56c-4b29-96ac-08474b9bf969/6e5ad29e-119d-4a08-8504-daf088928612"
       }
    }
    ```

**Interaction Data**

```
"interaction_data": {
    // unsigned image_url obtained with media_upload_url endpoint
    "image_url": "http://quiz.minio.docker/dev-uploads/item_media/1e6f97fc-f56c-4b29-96ac-08474b9bf969/6e5ad29e-119d-4a08-8504-daf088928612"
}
```

**Properties**

```
"properties": {}
```

**Scoring Data**

```
"scoring_data": {
    "value": {
        // Type of Hotspot selection (oval, square, polygon)
        "type": "oval",
        // List of coordinates (based on proportion of size) 
        // oval: first set is the center coordinates.  The second set is the width and height
        // square: first set of coordinates is the top left corner, and the second set 
        // is the bottom right corner
        // polygon: coordinates are the vertices of the closed polygon
        "coordinates": [
            {
                "x": 0.103960396039604,
                "y": 0.176706827309237
            },
            {
                "x": 0.9356435643564357,
                "y": 0.5502008032128514
            }
        ]
    }
}
```

**Multiple Choice**

**Interaction Data**

```
"interaction_data": {
    "choices": [
        {
            // Generated UUID for a choice
            "id": "f1feae62-566d-4d85-9afb-182d757030c9",
            // Position in the list on the UI
            "position": 1,
            // Choice string provided to quiz taker
            "item_body": "<p>a</p>"
        },
        {
            "id": "22d2bd84-5d5a-4640-8acf-484d799a735a",
            "position": 2,
            "item_body": "<p>v</p>"
        },
        {
            "id": "74a22711-85a6-4b46-8fb3-ea22947e869a",
            "position": 3,
            "item_body": "<p>x</p>"
        },
        {
            "id": "3ae2c63d-b990-40f0-aa70-e6bb854d0de2",
            "position": 4,
            "item_body": "<p>z</p>"
        },
        {
            "id": "8193a348-d336-4b00-b60e-dece48739ce4",
            "position": 5,
            "item_body": "<p>w</p>"
        }
    ]
}
```

**Properties**

```
"properties": {
    "shuffle_rules": {
        "choices": {
            // Lock items in position (array from 0 -> number of choices -1)
            "to_lock": [
                2
            ],
            // shuffle choices if true
            "shuffled": true
        }
    },
    // provide separate points for each choice if true
    "vary_points_by_answer": true
}
```

**Scoring Data**

Scoring data when Vary Points by Answer is true

```
"scoring_data": {
    // UUID for correct choice
    "value": "f1feae62-566d-4d85-9afb-182d757030c9",
    // Point values for each selected choice based on UUID
    "values": [
        {
            "value": "f1feae62-566d-4d85-9afb-182d757030c9",
            "points": 2
        },
        {
            "value": "22d2bd84-5d5a-4640-8acf-484d799a735a",
            "points": 1
        },
        {
            "value": "74a22711-85a6-4b46-8fb3-ea22947e869a",
            "points": 0
        },
        {
            "value": "3ae2c63d-b990-40f0-aa70-e6bb854d0de2",
            "points": 0
        },
        {
            "value": "8193a348-d336-4b00-b60e-dece48739ce4",
            "points": 0
        }
    ]
}
```

Scoring data when Vary Points by Answer is false

```
"scoring_data": {
    // UUID of correct choice
    "value": "8c3e244e-a0cb-49e6-a03f-0e94cac0929c"
}
```

**Answer Feedback**

```
"answer_feedback": {
    // Specific feedback for choices based on the UUID of the choice
    "8c3e244e-a0cb-49e6-a03f-0e94cac0929c": "<p>this is the best answer</p>",
    "a14d72c8-b92f-4254-abf6-555fce9c65d9": "<p>close</p>"
}
```

**Numeric**

**Interaction Data**

```
"interaction_data": {}
```

**Properties**

```
"properties": {}
```

**Scoring Data**

```
"scoring_data": {
// Answer values can be one or more responses with specific types
    "value": [
        {
            // id of the first possible answer
            "id": "1",
            // type of response (see others in list)
            "type": "exactResponse",
            // exact answer value
            "value": "200"
        },
        {
            "id": "edccc4e8-da26-4f2c-bb13-b7c07e3ffec0",
            "type": "marginOfError",
            "value": "200",
            // margin value along with margin_type
            "margin": "3",
            // margin_type is one of percent or absolute
            "margin_type": "percent"
        },
        {
            "id": "20da191a-b763-48ba-8ecf-c7dcda6f9ce7",
            // end of range
            "end": "210",
            "type": "withinARange",
            // start of range
            "start": "190"
        },
        {
            "id": "c4bd3847-44e6-49a6-b179-38ec21562f7b",
            "type": "preciseResponse",
            // correct answer
            "value": "200.0001",
            // precision needed in response along with precision_type
            "precision": "4",
            // precision type one of decimals or significantDigits
            "precision_type": "decimals"
        }
    ]
}
```

**Essay**

**Interaction Data**

```
"interaction_data": {
    // provide RCE for quiz taker
    "rce": true,
    // always null
    "essay": null,
    // provide word count if true
    "word_count": true,
    // allow for file upload if true (always false now)
    "file_upload": false,
    // provide spell check if true
    "spell_check": true,
    // if word limit enabled set to true, max and min must be set to word count values
    "word_limit_max": "1000",
    "word_limit_min": "0",
    "word_limit_enabled": true
}
```

**Properties**

```
"properties": {}
```

**Scoring Data**

```
"scoring_data": {
    // this value is set to the grading notes for this essay question
    "value": "Ensure use of complete sentences."
}
```

**Fill In The Blank (deprecated; only create rich-fill-blank questions)**

This data is similar to rich fill in the blank. It is deprecated, so this is only provided for reference. All data types are not represented here.

**Interaction Data**

```
"interaction_data": {
    "blanks": [
        {
            // Generated UUID for a blank
            "id": "b437ff00-8fb7-4267-9549-e8a72e428c2b",
            // Answer Type for the blank
            "answer_type": "openEntry"
        }
    ],
    // prompt that is a no-op for blanks or scoring
    "prompt": "<p>What is happening?</p>",
    // Sentence parsed here into types
    "stem_items": [
        {
            "id": "658e826e-4870-4bde-8941-aec87e21e5fe",
            "type": "text",
            "value": " ",
            "position": 1
        },
        {
            "id": "cdd8f185-4d24-404b-acc8-a1e7c52399c3",
            "type": "blank",
            "blank_id": "b437ff00-8fb7-4267-9549-e8a72e428c2b",
            "position": 2
        },
        {
            "id": "8da9ab45-beee-4646-8d1f-b1eadb2631f6",
            "type": "text",
            "value": " was here",
            "position": 3
        }
    ]
}
```

**Properties**

```
"properties": {
    "shuffle_rules": {
        // List of blanks from 0-n
        "blanks": {
            "children": {
                "0": {
                    "children": null
                }
            }
        }
    }
}
```

**Scoring Data**

```
"scoring_data": {
    "value": [
        {
            // Blank UUID
            "id": "b437ff00-8fb7-4267-9549-e8a72e428c2b",
            "scoring_data": {
                // actual value
                "value": "Robin",
                "blank_text": "Robin"
            },
            // Scoring algorithm
            "scoring_algorithm": "TextContainsAnswer"
        }
    ]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
