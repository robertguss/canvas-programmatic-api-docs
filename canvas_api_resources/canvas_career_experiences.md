# Canvas Career Experiences

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Canvas Career Experiences API

API for managing user career experience and role preferences in Canvas.

**An ExperienceSummary object looks like:**

```js
{
  // The current active experience. One of: 'academic', 'career_learner',
  // 'career_learning_provider'.
  "current_app": "career_learner",
  // List of available experiences for the user. Can include: 'academic',
  // 'career_learner', 'career_learning_provider'.
  "available_apps": ["academic", "career_learner"]
}
```

### [Get current and available experiences](#method.career_experience.experience_summary) <a href="#method.career_experience.experience_summary" id="method.career_experience.experience_summary"></a>

[CareerExperienceController#experience\_summary](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

**`GET /api/v1/career/experience_summary`**

**Scope:** `url:GET|/api/v1/career/experience_summary`

Returns the current user’s active experience and available experiences they can switch to.

**Example Request:**

```bash
curl https://<canvas>/api/v1/career_experience/experience_summary \
  -H 'Authorization: Bearer <token>'
```

Returns an [ExperienceSummary](#experiencesummary) object.

### [Switch experience](#method.career_experience.switch_experience) <a href="#method.career_experience.switch_experience" id="method.career_experience.switch_experience"></a>

[CareerExperienceController#switch\_experience](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

**`POST /api/v1/career/switch_experience`**

**Scope:** `url:POST|/api/v1/career/switch_experience`

Switch the current user’s active experience to the specified one.

**Request Parameters:**

| Parameter    | Type              | Description                                                                                          |
| ------------ | ----------------- | ---------------------------------------------------------------------------------------------------- |
| `experience` | Required `string` | <p>The experience to switch to.</p><p>Allowed values: <code>academic</code>, <code>career</code></p> |

**Example Request:**

```bash
curl -X POST https://<canvas>/api/v1/career_experience/switch_experience \
  -H 'Authorization: Bearer <token>' \
  -d 'experience=academic'
```

### [Switch role](#method.career_experience.switch_role) <a href="#method.career_experience.switch_role" id="method.career_experience.switch_role"></a>

[CareerExperienceController#switch\_role](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

**`POST /api/v1/career/switch_role`**

**Scope:** `url:POST|/api/v1/career/switch_role`

Switch the current user’s role within the current experience.

**Request Parameters:**

| Parameter | Type              | Description                                                                                              |
| --------- | ----------------- | -------------------------------------------------------------------------------------------------------- |
| `role`    | Required `string` | <p>The role to switch to.</p><p>Allowed values: <code>learner</code>, <code>learning_provider</code></p> |

**Example Request:**

```bash
curl -X POST https://<canvas>/api/v1/career_experience/switch_role \
  -H 'Authorization: Bearer <token>' \
  -d 'role=learner'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
