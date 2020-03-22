# Terraform::TencentCloud::TcaplusApplication

Use this resource to create tcaplus application

~> **NOTE:** tcaplus now only supports the following regions:ap-shanghai,ap-hongkong,na-siliconvalley,ap-singapore,ap-seoul,ap-tokyo,eu-frankfurt

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::TcaplusApplication",
    "Properties" : {
        "<a href="#appname" title="AppName">AppName</a>" : <i>String</i>,
        "<a href="#idltype" title="IdlType">IdlType</a>" : <i>String</i>,
        "<a href="#oldpasswordexpirelast" title="OldPasswordExpireLast">OldPasswordExpireLast</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::TcaplusApplication
Properties:
    <a href="#appname" title="AppName">AppName</a>: <i>String</i>
    <a href="#idltype" title="IdlType">IdlType</a>: <i>String</i>
    <a href="#oldpasswordexpirelast" title="OldPasswordExpireLast">OldPasswordExpireLast</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### AppName

Name of the tcapplus application. length should between 1 and 30.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdlType

Idl type of the tcapplus application.Valid values are PROTO,TDR,MIX.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OldPasswordExpireLast

Old password expected expiration seconds after change password,must >= 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password of the tcapplus application. length should between 12 and 16,a-z and 0-9 and A-Z must contain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet id of the tcapplus application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC id of the tcapplus application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiAccessId

Returns the <code>ApiAccessId</code> value.

#### ApiAccessIp

Returns the <code>ApiAccessIp</code> value.

#### ApiAccessPort

Returns the <code>ApiAccessPort</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### NetworkType

Returns the <code>NetworkType</code> value.

#### OldPasswordExpireTime

Returns the <code>OldPasswordExpireTime</code> value.

#### PasswordStatus

Returns the <code>PasswordStatus</code> value.

