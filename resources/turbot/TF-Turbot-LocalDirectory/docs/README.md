# TF::Turbot::LocalDirectory

The `Turbot Local Directory` resource adds support for local directories. It is used to create and delete directory settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::LocalDirectory",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::LocalDirectory
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### Description

Brief description of the purpose and details of the directory.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

ID or `aka` of the parent resource.
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through a local directory. For example, email id of the user.
- `title` - (Required) Short descriptive name for the directory.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileIdTemplate

A template to generate profile id for users authenticated through a local directory. For example, email id of the user.
- `title` - (Required) Short descriptive name for the directory.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Short descriptive name for the directory.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

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

#### DirectoryType

Returns the <code>DirectoryType</code> value.

#### Id

Returns the <code>Id</code> value.

#### ParentAkas

Returns the <code>ParentAkas</code> value.

#### Status

Returns the <code>Status</code> value.

