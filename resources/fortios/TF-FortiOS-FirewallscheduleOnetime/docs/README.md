# TF::FortiOS::FirewallscheduleOnetime

Onetime schedule configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallscheduleOnetime",
    "Properties" : {
        "<a href="#color" title="Color">Color</a>" : <i>Double</i>,
        "<a href="#end" title="End">End</a>" : <i>String</i>,
        "<a href="#expirationdays" title="ExpirationDays">ExpirationDays</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#start" title="Start">Start</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallscheduleOnetime
Properties:
    <a href="#color" title="Color">Color</a>: <i>Double</i>
    <a href="#end" title="End">End</a>: <i>String</i>
    <a href="#expirationdays" title="ExpirationDays">ExpirationDays</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#start" title="Start">Start</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Color

Color of icon on the GUI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### End

Schedule end date and time, format hh:mm yyyy/mm/dd.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationDays

Write an event log message this many days before the schedule expires.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Onetime schedule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

Schedule start date and time, format hh:mm yyyy/mm/dd.

_Required_: Yes

_Type_: String

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
