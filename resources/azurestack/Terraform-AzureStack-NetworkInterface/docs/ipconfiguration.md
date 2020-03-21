# Terraform::AzureStack::NetworkInterface IpConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationgatewaybackendaddresspoolsids" title="ApplicationGatewayBackendAddressPoolsIds">ApplicationGatewayBackendAddressPoolsIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#applicationsecuritygroupids" title="ApplicationSecurityGroupIds">ApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancerbackendaddresspoolsids" title="LoadBalancerBackendAddressPoolsIds">LoadBalancerBackendAddressPoolsIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancerinboundnatrulesids" title="LoadBalancerInboundNatRulesIds">LoadBalancerInboundNatRulesIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
    "<a href="#privateipaddressallocation" title="PrivateIpAddressAllocation">PrivateIpAddressAllocation</a>" : <i>String</i>,
    "<a href="#publicipaddressid" title="PublicIpAddressId">PublicIpAddressId</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#applicationgatewaybackendaddresspoolsids" title="ApplicationGatewayBackendAddressPoolsIds">ApplicationGatewayBackendAddressPoolsIds</a>: <i>
      - String</i>
<a href="#applicationsecuritygroupids" title="ApplicationSecurityGroupIds">ApplicationSecurityGroupIds</a>: <i>
      - String</i>
<a href="#loadbalancerbackendaddresspoolsids" title="LoadBalancerBackendAddressPoolsIds">LoadBalancerBackendAddressPoolsIds</a>: <i>
      - String</i>
<a href="#loadbalancerinboundnatrulesids" title="LoadBalancerInboundNatRulesIds">LoadBalancerInboundNatRulesIds</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
<a href="#privateipaddressallocation" title="PrivateIpAddressAllocation">PrivateIpAddressAllocation</a>: <i>String</i>
<a href="#publicipaddressid" title="PublicIpAddressId">PublicIpAddressId</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### ApplicationGatewayBackendAddressPoolsIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSecurityGroupIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerBackendAddressPoolsIds

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

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddressAllocation

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

