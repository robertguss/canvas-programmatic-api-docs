# Shared Brand Configs

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Shared Brand Configs API

This is how you can share Themes with other people in your account or so you can come back to them later without having to apply them to your account

**A SharedBrandConfig object looks like:**

```js
{
  // The shared_brand_config identifier.
  "id": 987,
  // The id of the account it should be shared within.
  "account_id": "",
  // The md5 (since BrandConfigs are identified by MD5 and not numeric id) of the
  // BrandConfig to share.
  "brand_config_md5": "1d31002c95842f8fe16da7dfcc0d1f39",
  // The name to share this theme as
  "name": "Crimson and Gold Verson 1",
  // When this was created
  "created_at": "2012-07-13T10:55:20-06:00",
  // When this was last updated
  "updated_at": "2012-07-13T10:55:20-06:00"
}
```

### [Share a BrandConfig (Theme)](#method.shared_brand_configs.create) <a href="#method.shared_brand_configs.create" id="method.shared_brand_configs.create"></a>

[SharedBrandConfigsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/shared_brand_configs_controller.rb)

**`POST /api/v1/accounts/:account_id/shared_brand_configs`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/shared_brand_configs`

Create a SharedBrandConfig, which will give the given brand\_config a name and make it available to other users of this account.

**Request Parameters:**

| Parameter                               | Type              | Description                                |
| --------------------------------------- | ----------------- | ------------------------------------------ |
| `shared_brand_config[name]`             | Required `string` | Name to share this BrandConfig (theme) as. |
| `shared_brand_config[brand_config_md5]` | Required `string` | MD5 of brand\_config to share              |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/<account_id>/shared_brand_configs' \
     -X POST \
     -F 'shared_brand_config[name]=Crimson and Gold Theme' \
     -F 'shared_brand_config[brand_config_md5]=a1f113321fa024e7a14cb0948597a2a4' \
     -H "Authorization: Bearer <token>"
```

Returns a [SharedBrandConfig](#sharedbrandconfig) object.

### [Update a shared theme](#method.shared_brand_configs.update) <a href="#method.shared_brand_configs.update" id="method.shared_brand_configs.update"></a>

[SharedBrandConfigsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/shared_brand_configs_controller.rb)

**`PUT /api/v1/accounts/:account_id/shared_brand_configs/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/shared_brand_configs/:id`

Update the specified shared\_brand\_config with a new name or to point to a new brand\_config. Uses same parameters as create.

**Example Request:**

```bash
curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/shared_brand_configs/<shared_brand_config_id>' \
     -H "Authorization: Bearer <token>" \
     -F 'shared_brand_config[name]=New Name' \
     -F 'shared_brand_config[brand_config_md5]=a1f113321fa024e7a14cb0948597a2a4'
```

Returns a [SharedBrandConfig](#sharedbrandconfig) object.

### [Un-share a BrandConfig (Theme)](#method.shared_brand_configs.destroy) <a href="#method.shared_brand_configs.destroy" id="method.shared_brand_configs.destroy"></a>

[SharedBrandConfigsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/shared_brand_configs_controller.rb)

**`DELETE /api/v1/shared_brand_configs/:id`**

**Scope:** `url:DELETE|/api/v1/shared_brand_configs/:id`

Delete a SharedBrandConfig, which will unshare it so you nor anyone else in your account will see it as an option to pick from.

**Example Request:**

```bash
curl -X DELETE https://<canvas>/api/v1/shared_brand_configs/<id> \
     -H 'Authorization: Bearer <token>'
```

Returns a [SharedBrandConfig](#sharedbrandconfig) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
