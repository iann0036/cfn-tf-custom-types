# TF::AVI::Networkservice RoutingServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertisebackendnetworks" title="AdvertiseBackendNetworks">AdvertiseBackendNetworks</a>" : <i>Boolean</i>,
    "<a href="#enableautogateway" title="EnableAutoGateway">EnableAutoGateway</a>" : <i>Boolean</i>,
    "<a href="#enablerouting" title="EnableRouting">EnableRouting</a>" : <i>Boolean</i>,
    "<a href="#enableviponallinterfaces" title="EnableVipOnAllInterfaces">EnableVipOnAllInterfaces</a>" : <i>Boolean</i>,
    "<a href="#enablevmac" title="EnableVmac">EnableVmac</a>" : <i>Boolean</i>,
    "<a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>" : <i>Boolean</i>,
    "<a href="#natpolicyref" title="NatPolicyRef">NatPolicyRef</a>" : <i>String</i>,
    "<a href="#routingbylinuxipstack" title="RoutingByLinuxIpstack">RoutingByLinuxIpstack</a>" : <i>Boolean</i>,
    "<a href="#floatingintfip" title="FloatingIntfIp">FloatingIntfIp</a>" : <i>[ <a href="floatingintfipdefinition.md">FloatingIntfIpDefinition</a>, ... ]</i>,
    "<a href="#floatingintfipse2" title="FloatingIntfIpSe2">FloatingIntfIpSe2</a>" : <i>[ <a href="floatingintfipse2definition.md">FloatingIntfIpSe2Definition</a>, ... ]</i>,
    "<a href="#flowtableprofile" title="FlowtableProfile">FlowtableProfile</a>" : <i>[ <a href="flowtableprofiledefinition.md">FlowtableProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#advertisebackendnetworks" title="AdvertiseBackendNetworks">AdvertiseBackendNetworks</a>: <i>Boolean</i>
<a href="#enableautogateway" title="EnableAutoGateway">EnableAutoGateway</a>: <i>Boolean</i>
<a href="#enablerouting" title="EnableRouting">EnableRouting</a>: <i>Boolean</i>
<a href="#enableviponallinterfaces" title="EnableVipOnAllInterfaces">EnableVipOnAllInterfaces</a>: <i>Boolean</i>
<a href="#enablevmac" title="EnableVmac">EnableVmac</a>: <i>Boolean</i>
<a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>: <i>Boolean</i>
<a href="#natpolicyref" title="NatPolicyRef">NatPolicyRef</a>: <i>String</i>
<a href="#routingbylinuxipstack" title="RoutingByLinuxIpstack">RoutingByLinuxIpstack</a>: <i>Boolean</i>
<a href="#floatingintfip" title="FloatingIntfIp">FloatingIntfIp</a>: <i>
      - <a href="floatingintfipdefinition.md">FloatingIntfIpDefinition</a></i>
<a href="#floatingintfipse2" title="FloatingIntfIpSe2">FloatingIntfIpSe2</a>: <i>
      - <a href="floatingintfipse2definition.md">FloatingIntfIpSe2Definition</a></i>
<a href="#flowtableprofile" title="FlowtableProfile">FlowtableProfile</a>: <i>
      - <a href="flowtableprofiledefinition.md">FlowtableProfileDefinition</a></i>
</pre>

## Properties

#### AdvertiseBackendNetworks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRouting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVipOnAllInterfaces

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVmac

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestart

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatPolicyRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingByLinuxIpstack

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIntfIp

_Required_: No

_Type_: List of <a href="floatingintfipdefinition.md">FloatingIntfIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIntfIpSe2

_Required_: No

_Type_: List of <a href="floatingintfipse2definition.md">FloatingIntfIpSe2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowtableProfile

_Required_: No

_Type_: List of <a href="flowtableprofiledefinition.md">FlowtableProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

