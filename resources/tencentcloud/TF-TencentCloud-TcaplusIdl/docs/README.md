# TF::TencentCloud::TcaplusIdl

Use this resource to create TcaplusDB IDL file.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::TcaplusIdl",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#filecontent" title="FileContent">FileContent</a>" : <i>String</i>,
        "<a href="#fileexttype" title="FileExtType">FileExtType</a>" : <i>String</i>,
        "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
        "<a href="#filetype" title="FileType">FileType</a>" : <i>String</i>,
        "<a href="#tablegroupid" title="TablegroupId">TablegroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::TcaplusIdl
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#filecontent" title="FileContent">FileContent</a>: <i>String</i>
    <a href="#fileexttype" title="FileExtType">FileExtType</a>: <i>String</i>
    <a href="#filename" title="FileName">FileName</a>: <i>String</i>
    <a href="#filetype" title="FileType">FileType</a>: <i>String</i>
    <a href="#tablegroupid" title="TablegroupId">TablegroupId</a>: <i>String</i>
</pre>

## Properties

#### ClusterId

ID of the TcaplusDB cluster to which the table group belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileContent

IDL file content of the TcaplusDB table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileExtType

File ext type of the IDL file. If `file_type` is `PROTO`, `file_ext_type` must be 'proto'; If `file_type` is `TDR`, `file_ext_type` must be 'xml'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileName

Name of the IDL file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileType

Type of the IDL file. Valid values are PROTO and TDR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TablegroupId

ID of the table group to which the IDL file belongs.

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

#### TableInfos

Returns the <code>TableInfos</code> value.

