# Terraform::Panos::BgpDampeningProfile

This resource allows you to add/update/delete a BGP dampening profile.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::BgpDampeningProfile",
    "Properties" : {
        "<a href="#cutoff" title="Cutoff">Cutoff</a>" : <i>Double</i>,
        "<a href="#decayhalflifereachable" title="DecayHalfLifeReachable">DecayHalfLifeReachable</a>" : <i>Double</i>,
        "<a href="#decayhalflifeunreachable" title="DecayHalfLifeUnreachable">DecayHalfLifeUnreachable</a>" : <i>Double</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#maxholdtime" title="MaxHoldTime">MaxHoldTime</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reuse" title="Reuse">Reuse</a>" : <i>Double</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::BgpDampeningProfile
Properties:
    <a href="#cutoff" title="Cutoff">Cutoff</a>: <i>Double</i>
    <a href="#decayhalflifereachable" title="DecayHalfLifeReachable">DecayHalfLifeReachable</a>: <i>Double</i>
    <a href="#decayhalflifeunreachable" title="DecayHalfLifeUnreachable">DecayHalfLifeUnreachable</a>: <i>Double</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#maxholdtime" title="MaxHoldTime">MaxHoldTime</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reuse" title="Reuse">Reuse</a>: <i>Double</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### Cutoff

Cutoff threshold value (default: `1.25`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecayHalfLifeReachable

Decay half-life while
reachable, in seconds (default: `300`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecayHalfLifeUnreachable

Decay half-life while
unreachable, in seconds (default: `900`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable or not (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHoldTime

Maximum hold-down time, in
seconds (default: `900`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reuse

Reuse threshold value (default: `0.5`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to add this BGP
dampening profile to.

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

