# TF::Databricks::DbfsFile

CloudFormation equivalent of databricks_dbfs_file

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::DbfsFile",
    "Properties" : {
        "<a href="#contentbase64" title="ContentBase64">ContentBase64</a>" : <i>String</i>,
        "<a href="#md5" title="Md5">Md5</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::DbfsFile
Properties:
    <a href="#contentbase64" title="ContentBase64">ContentBase64</a>: <i>String</i>
    <a href="#md5" title="Md5">Md5</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### ContentBase64

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

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

#### DbfsPath

Returns the <code>DbfsPath</code> value.

#### FileSize

Returns the <code>FileSize</code> value.

#### Id

Returns the <code>Id</code> value.

