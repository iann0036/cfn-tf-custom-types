# TF::TencentCloud::TcaplusTable

Use this resource to create TcaplusDB table.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::TcaplusTable",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#idlid" title="IdlId">IdlId</a>" : <i>String</i>,
        "<a href="#reservedreadcu" title="ReservedReadCu">ReservedReadCu</a>" : <i>Double</i>,
        "<a href="#reservedvolume" title="ReservedVolume">ReservedVolume</a>" : <i>Double</i>,
        "<a href="#reservedwritecu" title="ReservedWriteCu">ReservedWriteCu</a>" : <i>Double</i>,
        "<a href="#tableidltype" title="TableIdlType">TableIdlType</a>" : <i>String</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
        "<a href="#tabletype" title="TableType">TableType</a>" : <i>String</i>,
        "<a href="#tablegroupid" title="TablegroupId">TablegroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::TcaplusTable
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#idlid" title="IdlId">IdlId</a>: <i>String</i>
    <a href="#reservedreadcu" title="ReservedReadCu">ReservedReadCu</a>: <i>Double</i>
    <a href="#reservedvolume" title="ReservedVolume">ReservedVolume</a>: <i>Double</i>
    <a href="#reservedwritecu" title="ReservedWriteCu">ReservedWriteCu</a>: <i>Double</i>
    <a href="#tableidltype" title="TableIdlType">TableIdlType</a>: <i>String</i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
    <a href="#tabletype" title="TableType">TableType</a>: <i>String</i>
    <a href="#tablegroupid" title="TablegroupId">TablegroupId</a>: <i>String</i>
</pre>

## Properties

#### ClusterId

ID of the TcaplusDB cluster to which the table belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the TcaplusDB table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdlId

ID of the IDL File.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedReadCu

Reserved read capacity units of the TcaplusDB table.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedVolume

Reserved storage capacity of the TcaplusDB table (unit: GB).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedWriteCu

Reserved write capacity units of the TcaplusDB table.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableIdlType

IDL type of the TcaplusDB table. Valid values: `PROTO` and `TDR`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

Name of the TcaplusDB table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableType

Type of the TcaplusDB table. Valid values are `GENERIC` and `LIST`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TablegroupId

ID of the table group to which the table belongs.

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Error

Returns the <code>Error</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

#### TableSize

Returns the <code>TableSize</code> value.

