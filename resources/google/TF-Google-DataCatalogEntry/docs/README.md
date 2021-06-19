# TF::Google::DataCatalogEntry

Entry Metadata. A Data Catalog Entry resource represents another resource in Google Cloud Platform
(such as a BigQuery dataset or a Pub/Sub topic) or outside of Google Cloud Platform. Clients can use
the linkedResource field in the Entry resource to refer to the original resource ID of the source system.

An Entry resource contains resource details, such as its schema. An Entry can also be used to attach
flexible metadata, such as a Tag.


To get more information about Entry, see:

* [API documentation](https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/data-catalog/docs)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=data_catalog_entry_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-ima...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::DataCatalogEntry",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#entrygroup" title="EntryGroup">EntryGroup</a>" : <i>String</i>,
        "<a href="#entryid" title="EntryId">EntryId</a>" : <i>String</i>,
        "<a href="#linkedresource" title="LinkedResource">LinkedResource</a>" : <i>String</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userspecifiedsystem" title="UserSpecifiedSystem">UserSpecifiedSystem</a>" : <i>String</i>,
        "<a href="#userspecifiedtype" title="UserSpecifiedType">UserSpecifiedType</a>" : <i>String</i>,
        "<a href="#gcsfilesetspec" title="GcsFilesetSpec">GcsFilesetSpec</a>" : <i>[ <a href="gcsfilesetspecdefinition.md">GcsFilesetSpecDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::DataCatalogEntry
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#entrygroup" title="EntryGroup">EntryGroup</a>: <i>String</i>
    <a href="#entryid" title="EntryId">EntryId</a>: <i>String</i>
    <a href="#linkedresource" title="LinkedResource">LinkedResource</a>: <i>String</i>
    <a href="#schema" title="Schema">Schema</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userspecifiedsystem" title="UserSpecifiedSystem">UserSpecifiedSystem</a>: <i>String</i>
    <a href="#userspecifiedtype" title="UserSpecifiedType">UserSpecifiedType</a>: <i>String</i>
    <a href="#gcsfilesetspec" title="GcsFilesetSpec">GcsFilesetSpec</a>: <i>
      - <a href="gcsfilesetspecdefinition.md">GcsFilesetSpecDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryGroup

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkedResource

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSpecifiedSystem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSpecifiedType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsFilesetSpec

_Required_: No

_Type_: List of <a href="gcsfilesetspecdefinition.md">GcsFilesetSpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BigqueryDateShardedSpec

Returns the <code>BigqueryDateShardedSpec</code> value.

#### BigqueryTableSpec

Returns the <code>BigqueryTableSpec</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntegratedSystem

Returns the <code>IntegratedSystem</code> value.

#### Name

Returns the <code>Name</code> value.

