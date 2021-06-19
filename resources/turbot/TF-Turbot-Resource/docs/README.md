# TF::Turbot::Resource

The `turbot_resource` defines a resource in Turbot. Typically it is used to define the top level for a set of discoverable resources (e.g. an AWS account).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::Resource",
    "Properties" : {
        "<a href="#akas" title="Akas">Akas</a>" : <i>[ String, ... ]</i>,
        "<a href="#data" title="Data">Data</a>" : <i>String</i>,
        "<a href="#fulldata" title="FullData">FullData</a>" : <i>String</i>,
        "<a href="#fullmetadata" title="FullMetadata">FullMetadata</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::Resource
Properties:
    <a href="#akas" title="Akas">Akas</a>: <i>
      - String</i>
    <a href="#data" title="Data">Data</a>: <i>String</i>
    <a href="#fulldata" title="FullData">FullData</a>: <i>String</i>
    <a href="#fullmetadata" title="FullMetadata">FullMetadata</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Akas

Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

JSON representation of resource properties to be managed by Terraform. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are ignored by Terraform.
- `metadata` - (Optional) JSON representation of resource metadata properties to be managed by Terraform. NOTE: If additional metadata properties are set on the resource by other means, they are ignored by Terraform.
- `full_data` - (Optional) JSON representation of all resource properties to be set on the resource. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are removed.
- `full_metadata` - (Optional) JSON representation of all resource metadata properties to be set on the resource. NOTE: If additional metadata properties are set on the resource by other means, they are removed.
- `akas` - (Optional) Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullData

JSON representation of all resource properties to be set on the resource. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are removed.
- `full_metadata` - (Optional) JSON representation of all resource metadata properties to be set on the resource. NOTE: If additional metadata properties are set on the resource by other means, they are removed.
- `akas` - (Optional) Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullMetadata

JSON representation of all resource metadata properties to be set on the resource. NOTE: If additional metadata properties are set on the resource by other means, they are removed.
- `akas` - (Optional) Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

JSON representation of resource metadata properties to be managed by Terraform. NOTE: If additional metadata properties are set on the resource by other means, they are ignored by Terraform.
- `full_data` - (Optional) JSON representation of all resource properties to be set on the resource. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are removed.
- `full_metadata` - (Optional) JSON representation of all resource metadata properties to be set on the resource. NOTE: If additional metadata properties are set on the resource by other means, they are removed.
- `akas` - (Optional) Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

The identifier of the parent resource under which this resource will be created.
- `type` - (Required) Defines the type of the resource to be created.
- `data` - (Optional) JSON representation of resource properties to be managed by Terraform. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are ignored by Terraform.
- `metadata` - (Optional) JSON representation of resource metadata properties to be managed by Terraform. NOTE: If additional metadata properties are set on the resource by other means, they are ignored by Terraform.
- `full_data` - (Optional) JSON representation of all resource properties to be set on the resource. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are removed.
- `full_metadata` - (Optional) JSON representation of all resource metadata properties to be set on the resource. NOTE: If additional metadata properties are set on the resource by other means, they are removed.
- `akas` - (Optional) Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

User defined label for grouping resources.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Defines the type of the resource to be created.
- `data` - (Optional) JSON representation of resource properties to be managed by Terraform. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are ignored by Terraform.
- `metadata` - (Optional) JSON representation of resource metadata properties to be managed by Terraform. NOTE: If additional metadata properties are set on the resource by other means, they are ignored by Terraform.
- `full_data` - (Optional) JSON representation of all resource properties to be set on the resource. The data must be valid for the resource type schema. NOTE: If additional properties are set on the resource by other means, they are removed.
- `full_metadata` - (Optional) JSON representation of all resource metadata properties to be set on the resource. NOTE: If additional metadata properties are set on the resource by other means, they are removed.
- `akas` - (Optional) Unique identifier of the resource.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

_Type_: String

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

#### ParentAkas

Returns the <code>ParentAkas</code> value.

