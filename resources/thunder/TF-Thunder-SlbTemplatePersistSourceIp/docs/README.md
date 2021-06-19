# TF::Thunder::SlbTemplatePersistSourceIp

`thunder_slb_template_persist_source_ip` Provides details about thunder slb template persist source ip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplatePersistSourceIp",
    "Properties" : {
        "<a href="#donthonorconnrules" title="DontHonorConnRules">DontHonorConnRules</a>" : <i>Double</i>,
        "<a href="#enforcehigherpriority" title="EnforceHigherPriority">EnforceHigherPriority</a>" : <i>Double</i>,
        "<a href="#hashpersist" title="HashPersist">HashPersist</a>" : <i>Double</i>,
        "<a href="#incldstip" title="InclDstIp">InclDstIp</a>" : <i>Double</i>,
        "<a href="#inclsport" title="InclSport">InclSport</a>" : <i>Double</i>,
        "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#netmask6" title="Netmask6">Netmask6</a>" : <i>Double</i>,
        "<a href="#primaryport" title="PrimaryPort">PrimaryPort</a>" : <i>Double</i>,
        "<a href="#scanallmembers" title="ScanAllMembers">ScanAllMembers</a>" : <i>Double</i>,
        "<a href="#server" title="Server">Server</a>" : <i>Double</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>Double</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplatePersistSourceIp
Properties:
    <a href="#donthonorconnrules" title="DontHonorConnRules">DontHonorConnRules</a>: <i>Double</i>
    <a href="#enforcehigherpriority" title="EnforceHigherPriority">EnforceHigherPriority</a>: <i>Double</i>
    <a href="#hashpersist" title="HashPersist">HashPersist</a>: <i>Double</i>
    <a href="#incldstip" title="InclDstIp">InclDstIp</a>: <i>Double</i>
    <a href="#inclsport" title="InclSport">InclSport</a>: <i>Double</i>
    <a href="#matchtype" title="MatchType">MatchType</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#netmask6" title="Netmask6">Netmask6</a>: <i>Double</i>
    <a href="#primaryport" title="PrimaryPort">PrimaryPort</a>: <i>Double</i>
    <a href="#scanallmembers" title="ScanAllMembers">ScanAllMembers</a>: <i>Double</i>
    <a href="#server" title="Server">Server</a>: <i>Double</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>Double</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### DontHonorConnRules

Do not observe connection rate rules.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceHigherPriority

Enforce to use high priority node if available.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashPersist

Use hash value of source IP address.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InclDstIp

Include destination IP on the persist.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InclSport

Include source port on the persist.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchType

Persistence type.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Source IP persistence template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

IP subnet mask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask6

IPV6 subnet mask.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryPort

Primary port to create the persist session.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanAllMembers

Persist with SCAN of all members.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

Persist to the same server, default is port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Persist within the same service group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Persistence timeout (in minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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

#### Id

Returns the <code>Id</code> value.

