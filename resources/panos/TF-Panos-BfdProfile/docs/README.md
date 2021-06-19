# TF::Panos::BfdProfile

This resource allows you to add/update/delete BFD profiles.

~> **Note:** This resource is only applicable for PAN-OS 7.1+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::BfdProfile",
    "Properties" : {
        "<a href="#detectionmultiplier" title="DetectionMultiplier">DetectionMultiplier</a>" : <i>Double</i>,
        "<a href="#holdtime" title="HoldTime">HoldTime</a>" : <i>Double</i>,
        "<a href="#minimumrxinterval" title="MinimumRxInterval">MinimumRxInterval</a>" : <i>Double</i>,
        "<a href="#minimumrxttl" title="MinimumRxTtl">MinimumRxTtl</a>" : <i>Double</i>,
        "<a href="#minimumtxinterval" title="MinimumTxInterval">MinimumTxInterval</a>" : <i>Double</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::BfdProfile
Properties:
    <a href="#detectionmultiplier" title="DetectionMultiplier">DetectionMultiplier</a>: <i>Double</i>
    <a href="#holdtime" title="HoldTime">HoldTime</a>: <i>Double</i>
    <a href="#minimumrxinterval" title="MinimumRxInterval">MinimumRxInterval</a>: <i>Double</i>
    <a href="#minimumrxttl" title="MinimumRxTtl">MinimumRxTtl</a>: <i>Double</i>
    <a href="#minimumtxinterval" title="MinimumTxInterval">MinimumTxInterval</a>: <i>Double</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### DetectionMultiplier

Multiplier sent to remote
system.  Default is `3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldTime

Delay transmission and reception of control
packets in ms.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumRxInterval

Required minimum RX interval in
ms.  Default is `1000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumRxTtl

Minimum accepted ttl on received BFD
packet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumTxInterval

Desired minimum TX interval in
ms.  Default is `1000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

BFD operation mode.  Valid values are `active` (default)
or `passive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The BBFD profile's name.

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

