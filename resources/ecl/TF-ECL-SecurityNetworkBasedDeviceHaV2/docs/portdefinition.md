# TF::ECL::SecurityNetworkBasedDeviceHaV2 PortDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#enable" title="Enable">Enable</a>" : <i>String</i>,
    "<a href="#enableping" title="EnablePing">EnablePing</a>" : <i>String</i>,
    "<a href="#host1ipaddress" title="Host1IpAddress">Host1IpAddress</a>" : <i>String</i>,
    "<a href="#host1ipaddressprefix" title="Host1IpAddressPrefix">Host1IpAddressPrefix</a>" : <i>Double</i>,
    "<a href="#host2ipaddress" title="Host2IpAddress">Host2IpAddress</a>" : <i>String</i>,
    "<a href="#host2ipaddressprefix" title="Host2IpAddressPrefix">Host2IpAddressPrefix</a>" : <i>Double</i>,
    "<a href="#mtu" title="Mtu">Mtu</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#preempt" title="Preempt">Preempt</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#vrrpgrpid" title="VrrpGrpId">VrrpGrpId</a>" : <i>String</i>,
    "<a href="#vrrpid" title="VrrpId">VrrpId</a>" : <i>String</i>,
    "<a href="#vrrpipaddress" title="VrrpIpAddress">VrrpIpAddress</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#enable" title="Enable">Enable</a>: <i>String</i>
<a href="#enableping" title="EnablePing">EnablePing</a>: <i>String</i>
<a href="#host1ipaddress" title="Host1IpAddress">Host1IpAddress</a>: <i>String</i>
<a href="#host1ipaddressprefix" title="Host1IpAddressPrefix">Host1IpAddressPrefix</a>: <i>Double</i>
<a href="#host2ipaddress" title="Host2IpAddress">Host2IpAddress</a>: <i>String</i>
<a href="#host2ipaddressprefix" title="Host2IpAddressPrefix">Host2IpAddressPrefix</a>: <i>Double</i>
<a href="#mtu" title="Mtu">Mtu</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#preempt" title="Preempt">Preempt</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#vrrpgrpid" title="VrrpGrpId">VrrpGrpId</a>: <i>String</i>
<a href="#vrrpid" title="VrrpId">VrrpId</a>: <i>String</i>
<a href="#vrrpipaddress" title="VrrpIpAddress">VrrpIpAddress</a>: <i>String</i>
</pre>

## Properties

#### Comment

Comments for the port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Set "true" to enable the port "false" to disable the port.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePing

Set "true" to enable ping response, "false" to disable ping response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host1IpAddress

IP Address of the port for HA Host 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host1IpAddressPrefix

IP Address prefix of the port for HA Host 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host2IpAddress

IP Address of the port for HA Host 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host2IpAddressPrefix

IP Address prefix of the port for HA Host 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

MTU value in the configuration of the port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

Network ID to which the port is associated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preempt

"true" to enable preempt option, "false" to disable preempt option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

UUID	Subnet IDto which the port is associated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrrpGrpId

VRRP Group ID. This value must be in the range of "1" to "100".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrrpId

VRRP ID. This value must be in the range of "1" to "100".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrrpIpAddress

VRRP IP Address of this port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

