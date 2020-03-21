# Terraform::HuaweiCloud::AsConfigurationV1 Eip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#iptype" title="IpType">IpType</a>" : <i>String</i>,
    "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>[ &lt;a href=&#34;eip-bandwidth.md&#34;&gt;Bandwidth&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#iptype" title="IpType">IpType</a>: <i>String</i>
<a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>
      - &lt;a href=&#34;eip-bandwidth.md&#34;&gt;Bandwidth&lt;/a&gt;</i>
</pre>

## Properties

#### IpType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

_Required_: No
_Type_: List of &lt;a href=&#34;eip-bandwidth.md&#34;&gt;Bandwidth&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

