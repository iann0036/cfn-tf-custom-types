# Terraform::TencentCloud::TcaplusIdl

Use this resource to create tcaplus idl file

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::TcaplusIdl",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#filecontent" title="FileContent">FileContent</a>" : <i>String</i>,
        "<a href="#fileexttype" title="FileExtType">FileExtType</a>" : <i>String</i>,
        "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
        "<a href="#filetype" title="FileType">FileType</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::TcaplusIdl
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#filecontent" title="FileContent">FileContent</a>: <i>String</i>
    <a href="#fileexttype" title="FileExtType">FileExtType</a>: <i>String</i>
    <a href="#filename" title="FileName">FileName</a>: <i>String</i>
    <a href="#filetype" title="FileType">FileType</a>: <i>String</i>
</pre>

## Properties

#### AppId

Application id of the idl belongs..

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileContent

Idl file content.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileExtType

File ext type of this idl file. if `file_type` is PROTO  `file_ext_type` must be 'proto',if `file_type` is TDR  `file_ext_type` must be 'xml',if `file_type` is MIX  `file_ext_type` must be 'xml' or 'proto'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileName

Name of this idl file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileType

Type of this idl file, Valid values are PROTO,TDR,MIX.

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

#### TableInfos

Returns the <code>TableInfos</code> value.

