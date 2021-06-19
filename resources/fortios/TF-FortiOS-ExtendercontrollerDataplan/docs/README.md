# TF::FortiOS::ExtendercontrollerDataplan

FortiExtender dataplan configuration. Applies to FortiOS Version `>= 6.4.2`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ExtendercontrollerDataplan",
    "Properties" : {
        "<a href="#apn" title="Apn">Apn</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#billingdate" title="BillingDate">BillingDate</a>" : <i>Double</i>,
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
        "<a href="#carrier" title="Carrier">Carrier</a>" : <i>String</i>,
        "<a href="#iccid" title="Iccid">Iccid</a>" : <i>String</i>,
        "<a href="#modemid" title="ModemId">ModemId</a>" : <i>String</i>,
        "<a href="#monthlyfee" title="MonthlyFee">MonthlyFee</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overage" title="Overage">Overage</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#pdn" title="Pdn">Pdn</a>" : <i>String</i>,
        "<a href="#preferredsubnet" title="PreferredSubnet">PreferredSubnet</a>" : <i>Double</i>,
        "<a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>" : <i>String</i>,
        "<a href="#signalperiod" title="SignalPeriod">SignalPeriod</a>" : <i>Double</i>,
        "<a href="#signalthreshold" title="SignalThreshold">SignalThreshold</a>" : <i>Double</i>,
        "<a href="#slot" title="Slot">Slot</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ExtendercontrollerDataplan
Properties:
    <a href="#apn" title="Apn">Apn</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#billingdate" title="BillingDate">BillingDate</a>: <i>Double</i>
    <a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
    <a href="#carrier" title="Carrier">Carrier</a>: <i>String</i>
    <a href="#iccid" title="Iccid">Iccid</a>: <i>String</i>
    <a href="#modemid" title="ModemId">ModemId</a>: <i>String</i>
    <a href="#monthlyfee" title="MonthlyFee">MonthlyFee</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overage" title="Overage">Overage</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#pdn" title="Pdn">Pdn</a>: <i>String</i>
    <a href="#preferredsubnet" title="PreferredSubnet">PreferredSubnet</a>: <i>Double</i>
    <a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>: <i>String</i>
    <a href="#signalperiod" title="SignalPeriod">SignalPeriod</a>: <i>Double</i>
    <a href="#signalthreshold" title="SignalThreshold">SignalThreshold</a>: <i>Double</i>
    <a href="#slot" title="Slot">Slot</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Apn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

Authentication type. Valid values: `none`, `pap`, `chap`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingDate

Billing day of the month (1 - 31).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

Capacity in MB (0 - 102400000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Carrier

Carrier configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iccid

ICCID configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModemId

Dataplan's modem specifics, if any. Valid values: `modem1`, `modem2`, `all`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlyFee

Monthly fee of dataplan (0 - 100000, in local currency).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

FortiExtender dataplan name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overage

Enable/disable dataplan overage detection. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredSubnet

Preferred subnet mask (8 - 32).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetwork

Enable/disable dataplan private network support. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignalPeriod

Signal period (600 to 18000 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignalThreshold

Signal threshold. Specify the range between 50 - 100, where 50/100 means -50/-100 dBm.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot

SIM slot configuration. Valid values: `sim1`, `sim2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type preferences configuration. Valid values: `carrier`, `slot`, `iccid`, `generic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username.

_Required_: No

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

