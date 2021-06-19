# TF::CheckPoint::PutFile

This resource allows you to add a new file to a Check Point machine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::PutFile",
    "Properties" : {
        "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
        "<a href="#override" title="Override">Override</a>" : <i>Boolean</i>,
        "<a href="#textcontent" title="TextContent">TextContent</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::PutFile
Properties:
    <a href="#filename" title="FileName">FileName</a>: <i>String</i>
    <a href="#override" title="Override">Override</a>: <i>Boolean</i>
    <a href="#textcontent" title="TextContent">TextContent</a>: <i>String</i>
</pre>

## Properties

#### FileName

Filename include the desired path. The file will be created in the user home directory if the full path wasn't provided.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

If the file already exists, indicates whether to overwrite it.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextContent

Content to add to the new file.

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

