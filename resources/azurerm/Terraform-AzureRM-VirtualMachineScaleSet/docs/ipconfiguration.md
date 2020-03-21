# Terraform::AzureRM::VirtualMachineScaleSet IpConfiguration

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
    "<a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>" : <i>[ <a href="ipconfiguration-publicipaddressconfiguration.md">PublicIpAddressConfiguration</a>, ... ]</i>
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
      - <a href="ipconfiguration-publicipaddressconfiguration.md">PublicIpAddressConfiguration</a></i>
</pre>

## Properties

#### ApplicationGatewayBackendAddressPoolIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerBackendAddressPoolIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerInboundNatRulesIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressConfiguration

_Required_: No

_Type_: List of <a href="ipconfiguration-publicipaddressconfiguration.md">PublicIpAddressConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

