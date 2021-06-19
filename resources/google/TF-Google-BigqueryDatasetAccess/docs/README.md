# TF::Google::BigqueryDatasetAccess

Gives dataset access for a single entity. This resource is intended to be used in cases where
it is not possible to compile a full list of access blocks to include in a
`google_bigquery_dataset` resource, to enable them to be added separately.

~> **Note:** If this resource is used alongside a `google_bigquery_dataset` resource, the
dataset resource must either have no defined `access` blocks or a `lifecycle` block with
`ignore_changes = [access]` so they don't fight over which accesses should be on the dataset.


To get more information about DatasetAccess, see:

* [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)
* How-to Guides
    * [Controlling access to datasets](https://cloud.google.com/bigquery/docs/dataset-access-controls)

~> **Warning:** You must specify the role field using the legacy format `OWNER` instead of `roles/bigquery.dataOwner`. 
The API does accept both formats but it will always return the legacy format which results in Terraform
showing permanen...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::BigqueryDatasetAccess",
    "Properties" : {
        "<a href="#datasetid" title="DatasetId">DatasetId</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#groupbyemail" title="GroupByEmail">GroupByEmail</a>" : <i>String</i>,
        "<a href="#iammember" title="IamMember">IamMember</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#specialgroup" title="SpecialGroup">SpecialGroup</a>" : <i>String</i>,
        "<a href="#userbyemail" title="UserByEmail">UserByEmail</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#view" title="View">View</a>" : <i>[ <a href="viewdefinition.md">ViewDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::BigqueryDatasetAccess
Properties:
    <a href="#datasetid" title="DatasetId">DatasetId</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#groupbyemail" title="GroupByEmail">GroupByEmail</a>: <i>String</i>
    <a href="#iammember" title="IamMember">IamMember</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#specialgroup" title="SpecialGroup">SpecialGroup</a>: <i>String</i>
    <a href="#userbyemail" title="UserByEmail">UserByEmail</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#view" title="View">View</a>: <i>
      - <a href="viewdefinition.md">ViewDefinition</a></i>
</pre>

## Properties

#### DatasetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupByEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamMember

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecialGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserByEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: List of <a href="viewdefinition.md">ViewDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiUpdatedMember

Returns the <code>ApiUpdatedMember</code> value.

#### Id

Returns the <code>Id</code> value.

