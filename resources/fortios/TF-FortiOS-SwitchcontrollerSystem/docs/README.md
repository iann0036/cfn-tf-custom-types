# TF::FortiOS::SwitchcontrollerSystem

Configure system-wide switch controller settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerSystem",
    "Properties" : {
        "<a href="#datasyncinterval" title="DataSyncInterval">DataSyncInterval</a>" : <i>Double</i>,
        "<a href="#iotholdoff" title="IotHoldoff">IotHoldoff</a>" : <i>Double</i>,
        "<a href="#iotmacidle" title="IotMacIdle">IotMacIdle</a>" : <i>Double</i>,
        "<a href="#iotscaninterval" title="IotScanInterval">IotScanInterval</a>" : <i>Double</i>,
        "<a href="#iotweightthreshold" title="IotWeightThreshold">IotWeightThreshold</a>" : <i>Double</i>,
        "<a href="#nacperiodicinterval" title="NacPeriodicInterval">NacPeriodicInterval</a>" : <i>Double</i>,
        "<a href="#parallelprocess" title="ParallelProcess">ParallelProcess</a>" : <i>Double</i>,
        "<a href="#parallelprocessoverride" title="ParallelProcessOverride">ParallelProcessOverride</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerSystem
Properties:
    <a href="#datasyncinterval" title="DataSyncInterval">DataSyncInterval</a>: <i>Double</i>
    <a href="#iotholdoff" title="IotHoldoff">IotHoldoff</a>: <i>Double</i>
    <a href="#iotmacidle" title="IotMacIdle">IotMacIdle</a>: <i>Double</i>
    <a href="#iotscaninterval" title="IotScanInterval">IotScanInterval</a>: <i>Double</i>
    <a href="#iotweightthreshold" title="IotWeightThreshold">IotWeightThreshold</a>: <i>Double</i>
    <a href="#nacperiodicinterval" title="NacPeriodicInterval">NacPeriodicInterval</a>: <i>Double</i>
    <a href="#parallelprocess" title="ParallelProcess">ParallelProcess</a>: <i>Double</i>
    <a href="#parallelprocessoverride" title="ParallelProcessOverride">ParallelProcessOverride</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### DataSyncInterval

Time interval between collection of switch data (30 - 1800 sec, default = 60, 0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IotHoldoff

MAC entry's creation time. Time must be greater than this value for an entry to be created (default = 5 mins).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IotMacIdle

MAC entry's idle time. MAC entry is removed after this value (default = 1440 mins).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IotScanInterval

IoT scan interval (2 - 4294967295 mins, default = 60 mins, 0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IotWeightThreshold

MAC entry's confidence value. Value is re-queried when below this value (default = 1, 0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NacPeriodicInterval

Periodic time interval to run NAC engine (5 - 60 sec, default = 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParallelProcess

Maximum number of parallel processes (1 - 300, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParallelProcessOverride

Enable/disable parallel process override. Valid values: `disable`, `enable`.

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

