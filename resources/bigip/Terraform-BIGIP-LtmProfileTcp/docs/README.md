# Terraform::BIGIP::LtmProfileTcp

`bigip_ltm_profile_tcp` Configures a custom profile_tcp for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileTcp",
    "Properties" : {
        "<a href="#closewaittimeout" title="CloseWaitTimeout">CloseWaitTimeout</a>" : <i>Double</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#deferredaccept" title="DeferredAccept">DeferredAccept</a>" : <i>String</i>,
        "<a href="#fastopen" title="FastOpen">FastOpen</a>" : <i>String</i>,
        "<a href="#finwait2timeout" title="Finwait2timeout">Finwait2timeout</a>" : <i>Double</i>,
        "<a href="#finwaittimeout" title="FinwaitTimeout">FinwaitTimeout</a>" : <i>Double</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileTcp
Properties:
    <a href="#closewaittimeout" title="CloseWaitTimeout">CloseWaitTimeout</a>: <i>Double</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#deferredaccept" title="DeferredAccept">DeferredAccept</a>: <i>String</i>
    <a href="#fastopen" title="FastOpen">FastOpen</a>: <i>String</i>
    <a href="#finwait2timeout" title="Finwait2timeout">Finwait2timeout</a>: <i>Double</i>
    <a href="#finwaittimeout" title="FinwaitTimeout">FinwaitTimeout</a>: <i>Double</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
</pre>

## Properties

#### CloseWaitTimeout

Specifies the number of seconds that a connection remains in a LAST-ACK state before quitting. A value of 0 represents a term of forever (or until the maxrtx of the FIN state). The default value is 5 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeferredAccept

Specifies, when enabled, that the system defers allocation of the connection chain context until the client response is received. This option is useful for dealing with 3-way handshake DOS attacks. The default value is disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastOpen

When enabled, permits TCP Fast Open, allowing properly equipped TCP clients to send data with the SYN packet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Finwait2timeout

Specifies the number of seconds that a connection is in the FIN-WAIT-2 state before quitting. The default value is 300 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FinwaitTimeout

Specifies the number of seconds that a connection is in the FIN-WAIT-1 or closing state before quitting. The default value is 5 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state). You can also specify immediate or indefinite.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Specifies the number of seconds that a connection is idle before the connection is eligible for deletion. The default value is 300 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveInterval

Specifies the keep alive probe interval, in seconds. The default value is 1800 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partition

Displays the administrative partition within which this profile resides.

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

