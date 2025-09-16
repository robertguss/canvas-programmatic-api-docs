# Proficiency Ratings

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Proficiency Ratings API

API for customizing proficiency ratings

**A ProficiencyRating object looks like:**

```js
{
  // The description of the rating
  "description": "Exceeds Mastery",
  // A non-negative number of points for the rating
  "points": 4,
  // Indicates the rating where mastery is first achieved
  "mastery": false,
  // The hex color code of the rating
  "color": "02672D"
}
```

**A Proficiency object looks like:**

```js
{
  // An array of proficiency ratings. See the ProficiencyRating specification
  // above.
  "ratings": []
}
```

### [Create/update proficiency ratings](#method.outcome_proficiency_api.create) <a href="#method.outcome_proficiency_api.create" id="method.outcome_proficiency_api.create"></a>

[OutcomeProficiencyApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_proficiency_api_controller.rb)

**`POST /api/v1/accounts/:account_id/outcome_proficiency`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_proficiency`

**`POST /api/v1/courses/:course_id/outcome_proficiency`**

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_proficiency`

Create or update account-level proficiency ratings. These ratings will apply to all sub-accounts, unless they have their own account-level proficiency ratings defined.

**Request Parameters:**

| Parameter                | Type      | Description                                                                                                                |
| ------------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| `ratings[][description]` | `string`  | The description of the rating level.                                                                                       |
| `ratings[][points]`      | `integer` | The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value.       |
| `ratings[][mastery]`     | `integer` | Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery. |
| `ratings[][color]`       | `integer` | The color associated with the rating level. Should be a hex color code like ‘00FFFF’.                                      |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency' \
     -X POST \
     -F 'ratings[][description]=Exceeds Mastery' \
     -F 'ratings[][points]=4' \
     -F 'ratings[][color]=02672D' \
     -F 'ratings[][mastery]=false' \
     -F 'ratings[][description]=Mastery' \
     -F 'ratings[][points]=3' \
     -F 'ratings[][color]=03893D' \
     -F 'ratings[][mastery]=true' \
     -F 'ratings[][description]=Near Mastery' \
     -F 'ratings[][points]=2' \
     -F 'ratings[][color]=FAB901' \
     -F 'ratings[][mastery]=false' \
     -F 'ratings[][description]=Below Mastery' \
     -F 'ratings[][points]=1' \
     -F 'ratings[][color]=FD5D10' \
     -F 'ratings[][mastery]=false' \
     -F 'ratings[][description]=Well Below Mastery' \
     -F 'ratings[][points]=0' \
     -F 'ratings[][color]=E62429' \
     -F 'ratings[][mastery]=false' \
     -H "Authorization: Bearer <token>"
```

Returns a [Proficiency](#proficiency) object.

### [Get proficiency ratings](#method.outcome_proficiency_api.show) <a href="#method.outcome_proficiency_api.show" id="method.outcome_proficiency_api.show"></a>

[OutcomeProficiencyApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_proficiency_api_controller.rb)

**`GET /api/v1/accounts/:account_id/outcome_proficiency`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_proficiency`

**`GET /api/v1/courses/:course_id/outcome_proficiency`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_proficiency`

Get account-level proficiency ratings. If not defined for this account, it will return proficiency ratings for the nearest super-account with ratings defined. Will return 404 if none found.

```
Examples:
  curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
      -H 'Authorization: Bearer <token>'
```

Returns a [Proficiency](#proficiency) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
