# TF::OCI::AnalyticsAnalyticsInstance NetworkEndpointDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#networkendpointtype" title="NetworkEndpointType">NetworkEndpointType</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#vcnid" title="VcnId">VcnId</a>" : <i>String</i>,
    "<a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#whitelistedvcns" title="WhitelistedVcns">WhitelistedVcns</a>" : <i>[ <a href="whitelistedvcnsdefinition.md">WhitelistedVcnsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#networkendpointtype" title="NetworkEndpointType">NetworkEndpointType</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#vcnid" title="VcnId">VcnId</a>: <i>String</i>
<a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>: <i>
      - String</i>
<a href="#whitelistedvcns" title="WhitelistedVcns">WhitelistedVcns</a>: <i>
      - <a href="whitelistedvcnsdefinition.md">WhitelistedVcnsDefinition</a></i>
</pre>

## Properties

#### NetworkEndpointType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhitelistedIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhitelistedVcns

_Required_: No

_Type_: List of <a href="whitelistedvcnsdefinition.md">WhitelistedVcnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

