# TF::NewRelic::Workload

Use this resource to create, update, and delete a New Relic One workload.

A New Relic User API key is required to provision this resource.  Set the `api_key`
attribute in the `provider` block or the `NEW_RELIC_API_KEY` environment
variable with your User API key.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::Workload",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#entityguids" title="EntityGuids">EntityGuids</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scopeaccountids" title="ScopeAccountIds">ScopeAccountIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#entitysearchquery" title="EntitySearchQuery">EntitySearchQuery</a>" : <i>[ <a href="entitysearchquerydefinition.md">EntitySearchQueryDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::Workload
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#entityguids" title="EntityGuids">EntityGuids</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scopeaccountids" title="ScopeAccountIds">ScopeAccountIds</a>: <i>
      - Double</i>
    <a href="#entitysearchquery" title="EntitySearchQuery">EntitySearchQuery</a>: <i>
      - <a href="entitysearchquerydefinition.md">EntitySearchQueryDefinition</a></i>
</pre>

## Properties

#### AccountId

The New Relic account ID where you want to create the workload.
* `entity_guids` - (Optional) A list of entity GUIDs manually assigned to this workload.
* `entity_search_query` - (Optional) A list of search queries that define a dynamic workload.  See [Nested entity_search_query blocks](#nested-entity_search_query-blocks) below for details.
* `scope_account_ids` - (Optional) A list of account IDs that will be used to get entities from.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityGuids

A list of entity GUIDs manually assigned to this workload.
* `entity_search_query` - (Optional) A list of search queries that define a dynamic workload.  See [Nested entity_search_query blocks](#nested-entity_search_query-blocks) below for details.
* `scope_account_ids` - (Optional) A list of account IDs that will be used to get entities from.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The workload's name.
* `account_id` - (Required) The New Relic account ID where you want to create the workload.
* `entity_guids` - (Optional) A list of entity GUIDs manually assigned to this workload.
* `entity_search_query` - (Optional) A list of search queries that define a dynamic workload.  See [Nested entity_search_query blocks](#nested-entity_search_query-blocks) below for details.
* `scope_account_ids` - (Optional) A list of account IDs that will be used to get entities from.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeAccountIds

A list of account IDs that will be used to get entities from.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntitySearchQuery

_Required_: No

_Type_: List of <a href="entitysearchquerydefinition.md">EntitySearchQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompositeEntitySearchQuery

Returns the <code>CompositeEntitySearchQuery</code> value.

#### Guid

Returns the <code>Guid</code> value.

#### Id

Returns the <code>Id</code> value.

#### Permalink

Returns the <code>Permalink</code> value.

#### WorkloadId

Returns the <code>WorkloadId</code> value.

