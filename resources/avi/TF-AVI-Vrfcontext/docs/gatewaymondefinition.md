# TF::AVI::Vrfcontext GatewayMonDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gatewaymonitorfailthreshold" title="GatewayMonitorFailThreshold">GatewayMonitorFailThreshold</a>" : <i>Double</i>,
    "<a href="#gatewaymonitorinterval" title="GatewayMonitorInterval">GatewayMonitorInterval</a>" : <i>Double</i>,
    "<a href="#gatewaymonitorsuccessthreshold" title="GatewayMonitorSuccessThreshold">GatewayMonitorSuccessThreshold</a>" : <i>Double</i>,
    "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>[ <a href="gatewayipdefinition.md">GatewayIpDefinition</a>, ... ]</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#gatewaymonitorfailthreshold" title="GatewayMonitorFailThreshold">GatewayMonitorFailThreshold</a>: <i>Double</i>
<a href="#gatewaymonitorinterval" title="GatewayMonitorInterval">GatewayMonitorInterval</a>: <i>Double</i>
<a href="#gatewaymonitorsuccessthreshold" title="GatewayMonitorSuccessThreshold">GatewayMonitorSuccessThreshold</a>: <i>Double</i>
<a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>
      - <a href="gatewayipdefinition.md">GatewayIpDefinition</a></i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
</pre>

## Properties

#### GatewayMonitorFailThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayMonitorInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayMonitorSuccessThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

_Required_: No

_Type_: List of <a href="gatewayipdefinition.md">GatewayIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

