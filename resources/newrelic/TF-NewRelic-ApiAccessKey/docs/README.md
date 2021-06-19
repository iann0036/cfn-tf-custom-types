# TF::NewRelic::ApiAccessKey

Use this resource to programmatically create and manage the following types of keys:
- [User API keys](https://docs.newrelic.com/docs/apis/get-started/intro-apis/types-new-relic-api-keys#user-api-key)
- License (or ingest) keys, including:
    - General [license key](https://docs.newrelic.com/docs/accounts/install-new-relic/account-setup/license-key) used for APM
    - [Browser license key](https://docs.newrelic.com/docs/browser/new-relic-browser/configuration/copy-browser-monitoring-license-key-app-id)

Please visit the New Relic article ['Use NerdGraph to manage license keys and User API keys'](https://docs.newrelic.com/docs/apis/nerdgraph/examples/use-nerdgraph-manage-license-keys-user-keys)
for more information.

-> **IMPORTANT!**
Please be very careful when updating existing `newrelic_api_access_key` resources as only `newrelic_api_access_key.name`
and `newrelic_api_access_key.notes` are updatable. All other resource attributes will force a resource recreation which will
invalidate the previous API k...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::ApiAccessKey",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#ingesttype" title="IngestType">IngestType</a>" : <i>String</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::ApiAccessKey
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#ingesttype" title="IngestType">IngestType</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>Double</i>
</pre>

## Properties

#### AccountId

The New Relic account ID of the account you wish to create the API access key.
- `key_type` - (Required) What type of API key to create. Valid options are `INGEST` or `USER`, case-sensitive.
- `ingest_type` - (Optional) Required if `key_type = INGEST`. Valid options are `BROWSER` or `LICENSE`, case-sensitive.
- `user_id` - (Optional) Required if `key_type = USER`. The New Relic user ID yous wish to create the API access key for in an account.
- `name` - (Optional) The name of the key.
- `notes` - (Optional) Any notes about this ingest key.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngestType

Required if `key_type = INGEST`. Valid options are `BROWSER` or `LICENSE`, case-sensitive.
- `user_id` - (Optional) Required if `key_type = USER`. The New Relic user ID yous wish to create the API access key for in an account.
- `name` - (Optional) The name of the key.
- `notes` - (Optional) Any notes about this ingest key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

What type of API key to create. Valid options are `INGEST` or `USER`, case-sensitive.
- `ingest_type` - (Optional) Required if `key_type = INGEST`. Valid options are `BROWSER` or `LICENSE`, case-sensitive.
- `user_id` - (Optional) Required if `key_type = USER`. The New Relic user ID yous wish to create the API access key for in an account.
- `name` - (Optional) The name of the key.
- `notes` - (Optional) Any notes about this ingest key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the key.
- `notes` - (Optional) Any notes about this ingest key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

Any notes about this ingest key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

Required if `key_type = USER`. The New Relic user ID yous wish to create the API access key for in an account.
- `name` - (Optional) The name of the key.
- `notes` - (Optional) Any notes about this ingest key.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Key

Returns the <code>Key</code> value.

