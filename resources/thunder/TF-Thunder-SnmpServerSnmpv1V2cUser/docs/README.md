# TF::Thunder::SnmpServerSnmpv1V2cUser

CloudFormation equivalent of thunder_snmp_server_snmpv1_v2c_user

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerSnmpv1V2cUser",
    "Properties" : {
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#passwd" title="Passwd">Passwd</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#oidlist" title="OidList">OidList</a>" : <i>[ <a href="oidlistdefinition.md">OidListDefinition</a>, ... ]</i>,
        "<a href="#remote" title="Remote">Remote</a>" : <i>[ <a href="remotedefinition.md">RemoteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerSnmpv1V2cUser
Properties:
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#passwd" title="Passwd">Passwd</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#oidlist" title="OidList">OidList</a>: <i>
      - <a href="oidlistdefinition.md">OidListDefinition</a></i>
    <a href="#remote" title="Remote">Remote</a>: <i>
      - <a href="remotedefinition.md">RemoteDefinition</a></i>
</pre>

## Properties

#### Encrypted

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passwd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidList

_Required_: No

_Type_: List of <a href="oidlistdefinition.md">OidListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remote

_Required_: No

_Type_: List of <a href="remotedefinition.md">RemoteDefinition</a>

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

