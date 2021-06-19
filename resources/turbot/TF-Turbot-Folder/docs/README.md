# TF::Turbot::Folder

The `Turbot Folder` resource adds support for folders. Turbot folders define a top level hierarchy to arrange resources and their policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::Folder",
    "Properties" : {
        "<a href="#akas" title="Akas">Akas</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::Folder
Properties:
    <a href="#akas" title="Akas">Akas</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### Akas

Unique identifier of the resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Brief description of the purpose and details of the folder.
- `parent` - (Required) ID or `aka` of the parent resource.
- `title` - (Required) Short descriptive name for the folder. This appears as the folder name in the Turbot Console.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this folder.
- `akas` - (Optional) Unique identifier of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

ID or `aka` of the parent resource.
- `title` - (Required) Short descriptive name for the folder. This appears as the folder name in the Turbot Console.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this folder.
- `akas` - (Optional) Unique identifier of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Labels that can be used to manage, group, categorize, search, and save metadata for this folder.
- `akas` - (Optional) Unique identifier of the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Short descriptive name for the folder. This appears as the folder name in the Turbot Console.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this folder.
- `akas` - (Optional) Unique identifier of the resource.

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

