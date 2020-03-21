# Terraform::BIGIP::SysSnmpTraps

`bigip_sys_snmp_traps` provides details bout how to enable snmp_traps resource on BIG-IP

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::SysSnmpTraps",
    "Properties" : {
        "<a href="#authpasswordencrypted" title="AuthPasswordencrypted">AuthPasswordencrypted</a>" : <i>String</i>,
        "<a href="#authprotocol" title="AuthProtocol">AuthProtocol</a>" : <i>String</i>,
        "<a href="#community" title="Community">Community</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#engineid" title="EngineId">EngineId</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#privacypassword" title="PrivacyPassword">PrivacyPassword</a>" : <i>String</i>,
        "<a href="#privacypasswordencrypted" title="PrivacyPasswordEncrypted">PrivacyPasswordEncrypted</a>" : <i>String</i>,
        "<a href="#privacyprotocol" title="PrivacyProtocol">PrivacyProtocol</a>" : <i>String</i>,
        "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
        "<a href="#securityname" title="SecurityName">SecurityName</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::SysSnmpTraps
Properties:
    <a href="#authpasswordencrypted" title="AuthPasswordencrypted">AuthPasswordencrypted</a>: <i>String</i>
    <a href="#authprotocol" title="AuthProtocol">AuthProtocol</a>: <i>String</i>
    <a href="#community" title="Community">Community</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#engineid" title="EngineId">EngineId</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#privacypassword" title="PrivacyPassword">PrivacyPassword</a>: <i>String</i>
    <a href="#privacypasswordencrypted" title="PrivacyPasswordEncrypted">PrivacyPasswordEncrypted</a>: <i>String</i>
    <a href="#privacyprotocol" title="PrivacyProtocol">PrivacyProtocol</a>: <i>String</i>
    <a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
    <a href="#securityname" title="SecurityName">SecurityName</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### AuthPasswordencrypted

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Community

Specifies the community string used for this trap.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The port that the trap will be sent to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

The host the trap will be sent to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the snmp trap.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

User defined description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivacyPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivacyPasswordEncrypted

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivacyProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

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

