# TF::AzureRM::VirtualMachineScaleSet IpConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationgatewaybackendaddresspoolids" title="ApplicationGatewayBackendAddressPoolIds">ApplicationGatewayBackendAddressPoolIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#applicationsecuritygroupids" title="ApplicationSecurityGroupIds">ApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancerbackendaddresspoolids" title="LoadBalancerBackendAddressPoolIds">LoadBalancerBackendAddressPoolIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancerinboundnatrulesids" title="LoadBalancerInboundNatRulesIds">LoadBalancerInboundNatRulesIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>" : <i>[ <a href="publicipaddressconfigurationdefinition.md">PublicIpAddressConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicationgatewaybackendaddresspoolids" title="ApplicationGatewayBackendAddressPoolIds">ApplicationGatewayBackendAddressPoolIds</a>: <i>
      - String</i>
<a href="#applicationsecuritygroupids" title="ApplicationSecurityGroupIds">ApplicationSecurityGroupIds</a>: <i>
      - String</i>
<a href="#loadbalancerbackendaddresspoolids" title="LoadBalancerBackendAddressPoolIds">LoadBalancerBackendAddressPoolIds</a>: <i>
      - String</i>
<a href="#loadbalancerinboundnatrulesids" title="LoadBalancerInboundNatRulesIds">LoadBalancerInboundNatRulesIds</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>: <i>
      - <a href="publicipaddressconfigurationdefinition.md">PublicIpAddressConfigurationDefinition</a></i>
</pre>

## Properties

#### ApplicationGatewayBackendAddressPoolIds

Specifies an array of references to backend address pools of application gateways. A scale set can reference backend address pools of multiple application gateways. Multiple scale sets can use the same application gateway.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSecurityGroupIds

Specifies up to `20` application security group IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerBackendAddressPoolIds

Specifies an array of references to backend address pools of load balancers. A scale set can reference backend address pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerInboundNatRulesIds

Specifies an array of references to inbound NAT pools for load balancers. A scale set can reference inbound nat pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies name of the IP configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

Specifies if this ip_configuration is the primary one.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Specifies the identifier of the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressConfiguration

_Required_: No

_Type_: List of <a href="publicipaddressconfigurationdefinition.md">PublicIpAddressConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

