# Peer Reviews

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Peer Reviews API

**A PeerReview object looks like:**

```js
{
  // The assessors user id
  "assessor_id": 23,
  // The id for the asset associated with this Peer Review
  "asset_id": 13,
  // The type of the asset
  "asset_type": "Submission",
  // The id of the Peer Review
  "id": 1,
  // The user id for the owner of the asset
  "user_id": 7,
  // The state of the Peer Review, either 'assigned' or 'completed'
  "workflow_state": "assigned",
  // the User object for the owner of the asset if the user include parameter is
  // provided (see user API) (optional)
  "user": "User",
  // The User object for the assessor if the user include parameter is provided
  // (see user API) (optional)
  "assessor": "User",
  // The submission comments associated with this Peer Review if the
  // submission_comment include parameter is provided (see submissions API)
  // (optional)
  "submission_comments": "SubmissionComment"
}
```

### [Get all Peer Reviews](#method.peer_reviews_api.index) <a href="#method.peer_reviews_api.index" id="method.peer_reviews_api.index"></a>

[PeerReviewsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/peer_reviews`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/peer_reviews`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/peer_reviews`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/peer_reviews`

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

Get a list of all Peer Reviews for this assignment

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                    |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `include[]` | `string` | <p>Associations to include with the peer review.</p><p>Allowed values: <code>submission_comments</code>, <code>user</code></p> |

Returns a list of [PeerReview](#peerreview) objects.

### [Create Peer Review](#method.peer_reviews_api.create) <a href="#method.peer_reviews_api.create" id="method.peer_reviews_api.create"></a>

[PeerReviewsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`**

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

Create a peer review for the assignment

**Request Parameters:**

| Parameter | Type               | Description                                       |
| --------- | ------------------ | ------------------------------------------------- |
| `user_id` | Required `integer` | user\_id to assign as reviewer on this assignment |

Returns a [PeerReview](#peerreview) object.

### [Delete Peer Review](#method.peer_reviews_api.destroy) <a href="#method.peer_reviews_api.destroy" id="method.peer_reviews_api.destroy"></a>

[PeerReviewsApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**`DELETE /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`**

**Scope:** `url:DELETE|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

Delete a peer review for the assignment

**Request Parameters:**

| Parameter | Type               | Description                                       |
| --------- | ------------------ | ------------------------------------------------- |
| `user_id` | Required `integer` | user\_id to delete as reviewer on this assignment |

Returns a [PeerReview](#peerreview) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
