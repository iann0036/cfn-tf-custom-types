# Terraform::OCI::CoreSecurityList IngressSecurityRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#stateless" title="Stateless">Stateless</a>" : <i>Boolean</i>,
    "<a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>" : <i>[ <a href="ingresssecurityrules-icmpoptions.md">IcmpOptions</a>, ... ]</i>,
    "<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>" : <i>[ <a href="ingresssecurityrules-tcpoptions.md">TcpOptions</a>, ... ]</i>,
    "<a href="#udpoptions" title="UdpOptions">UdpOptions</a>" : <i>[ <a href="ingresssecurityrules-udpoptions.md">UdpOptions</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#stateless" title="Stateless">Stateless</a>: <i>Boolean</i>
<a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>: <i>
      - <a href="ingresssecurityrules-icmpoptions.md">IcmpOptions</a></i>
<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>: <i>
      - <a href="ingresssecurityrules-tcpoptions.md">TcpOptions</a></i>
<a href="#udpoptions" title="UdpOptions">UdpOptions</a>: <i>
      - <a href="ingresssecurityrules-udpoptions.md">UdpOptions</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateless

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpOptions

_Required_: No

_Type_: List of <a href="ingresssecurityrules-icmpoptions.md">IcmpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpOptions

_Required_: No

_Type_: List of <a href="ingresssecurityrules-tcpoptions.md">TcpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpOptions

_Required_: No

_Type_: List of <a href="ingresssecurityrules-udpoptions.md">UdpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

