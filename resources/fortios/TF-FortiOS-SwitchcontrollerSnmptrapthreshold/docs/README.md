# TF::FortiOS::SwitchcontrollerSnmptrapthreshold

Configure FortiSwitch SNMP trap threshold values globally.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerSnmptrapthreshold",
    "Properties" : {
        "<a href="#traphighcputhreshold" title="TrapHighCpuThreshold">TrapHighCpuThreshold</a>" : <i>Double</i>,
        "<a href="#traplogfullthreshold" title="TrapLogFullThreshold">TrapLogFullThreshold</a>" : <i>Double</i>,
        "<a href="#traplowmemorythreshold" title="TrapLowMemoryThreshold">TrapLowMemoryThreshold</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerSnmptrapthreshold
Properties:
    <a href="#traphighcputhreshold" title="TrapHighCpuThreshold">TrapHighCpuThreshold</a>: <i>Double</i>
    <a href="#traplogfullthreshold" title="TrapLogFullThreshold">TrapLogFullThreshold</a>: <i>Double</i>
    <a href="#traplowmemorythreshold" title="TrapLowMemoryThreshold">TrapLowMemoryThreshold</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### TrapHighCpuThreshold

CPU usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapLogFullThreshold

Log disk usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapLowMemoryThreshold

Memory usage when trap is sent.

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

