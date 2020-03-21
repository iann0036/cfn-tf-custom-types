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
    "<a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>" : <i>[ &lt;a href=&#34;ingresssecurityrules-icmpoptions.md&#34;&gt;IcmpOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>" : <i>[ &lt;a href=&#34;ingresssecurityrules-tcpoptions.md&#34;&gt;TcpOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#udpoptions" title="UdpOptions">UdpOptions</a>" : <i>[ &lt;a href=&#34;ingresssecurityrules-udpoptions.md&#34;&gt;UdpOptions&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;ingresssecurityrules-icmpoptions.md&#34;&gt;IcmpOptions&lt;/a&gt;</i>
<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>: <i>
      - &lt;a href=&#34;ingresssecurityrules-tcpoptions.md&#34;&gt;TcpOptions&lt;/a&gt;</i>
<a href="#udpoptions" title="UdpOptions">UdpOptions</a>: <i>
      - &lt;a href=&#34;ingresssecurityrules-udpoptions.md&#34;&gt;UdpOptions&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;ingresssecurityrules-icmpoptions.md&#34;&gt;IcmpOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpOptions

_Required_: No
_Type_: List of &lt;a href=&#34;ingresssecurityrules-tcpoptions.md&#34;&gt;TcpOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpOptions

_Required_: No
_Type_: List of &lt;a href=&#34;ingresssecurityrules-udpoptions.md&#34;&gt;UdpOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

