# TF::FortiOS::SystemStandalonecluster

Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes. Applies to FortiOS Version `>= 6.4.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemStandalonecluster",
    "Properties" : {
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>String</i>,
        "<a href="#groupmemberid" title="GroupMemberId">GroupMemberId</a>" : <i>Double</i>,
        "<a href="#layer2connection" title="Layer2Connection">Layer2Connection</a>" : <i>String</i>,
        "<a href="#psksecret" title="Psksecret">Psksecret</a>" : <i>String</i>,
        "<a href="#sessionsyncdev" title="SessionSyncDev">SessionSyncDev</a>" : <i>String</i>,
        "<a href="#standalonegroupid" title="StandaloneGroupId">StandaloneGroupId</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemStandalonecluster
Properties:
    <a href="#encryption" title="Encryption">Encryption</a>: <i>String</i>
    <a href="#groupmemberid" title="GroupMemberId">GroupMemberId</a>: <i>Double</i>
    <a href="#layer2connection" title="Layer2Connection">Layer2Connection</a>: <i>String</i>
    <a href="#psksecret" title="Psksecret">Psksecret</a>: <i>String</i>
    <a href="#sessionsyncdev" title="SessionSyncDev">SessionSyncDev</a>: <i>String</i>
    <a href="#standalonegroupid" title="StandaloneGroupId">StandaloneGroupId</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Encryption

Enable/disable encryption when synchronizing sessions. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMemberId

Cluster member ID (0 - 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer2Connection

Indicate whether layer 2 connections are present among FGSP members. Valid values: `available`, `unavailable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Psksecret

Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionSyncDev

Offload session-sync process to kernel and sync sessions using connected interface(s) directly.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandaloneGroupId

Cluster group ID (0 - 255). Must be the same for all members.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

