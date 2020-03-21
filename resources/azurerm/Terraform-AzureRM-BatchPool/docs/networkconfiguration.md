# Terraform::AzureRM::BatchPool NetworkConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#publicips" title="PublicIps">PublicIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>" : <i>[ <a href="networkconfiguration-endpointconfiguration.md">EndpointConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#publicips" title="PublicIps">PublicIps</a>: <i>
      - String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>: <i>
      - <a href="networkconfiguration-endpointconfiguration.md">EndpointConfiguration</a></i>
</pre>

## Properties

#### PublicIps

A list of public ip ids that will be allocated to nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ARM resource identifier of the virtual network subnet which the compute nodes of the pool will join. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfiguration

_Required_: No

_Type_: List of <a href="networkconfiguration-endpointconfiguration.md">EndpointConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

