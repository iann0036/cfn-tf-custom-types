# Terraform::AzureRM::BatchPool NetworkConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#publicips" title="PublicIps">PublicIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>" : <i>[ &lt;a href=&#34;networkconfiguration-endpointconfiguration.md&#34;&gt;EndpointConfiguration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#publicips" title="PublicIps">PublicIps</a>: <i>
      - String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>: <i>
      - &lt;a href=&#34;networkconfiguration-endpointconfiguration.md&#34;&gt;EndpointConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### PublicIps

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;networkconfiguration-endpointconfiguration.md&#34;&gt;EndpointConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

