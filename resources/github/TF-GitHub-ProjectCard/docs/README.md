# TF::GitHub::ProjectCard

This resource allows you to create and manage cards for GitHub projects.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::ProjectCard",
    "Properties" : {
        "<a href="#columnid" title="ColumnId">ColumnId</a>" : <i>String</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::ProjectCard
Properties:
    <a href="#columnid" title="ColumnId">ColumnId</a>: <i>String</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
</pre>

## Properties

#### ColumnId

The ID of the card.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

The note contents of the card. Markdown supported.

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

#### CardId

Returns the <code>CardId</code> value.

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

