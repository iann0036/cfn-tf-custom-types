# Terraform::Docker::Network IpamConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#auxaddress" title="AuxAddress">AuxAddress</a>" : <i>[ &lt;a href=&#34;ipamconfig-auxaddress.md&#34;&gt;AuxAddress&lt;/a&gt;, ... ]</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#iprange" title="IpRange">IpRange</a>" : <i>String</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#auxaddress" title="AuxAddress">AuxAddress</a>: <i>
      - &lt;a href=&#34;ipamconfig-auxaddress.md&#34;&gt;AuxAddress&lt;/a&gt;</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#iprange" title="IpRange">IpRange</a>: <i>String</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
</pre>

## Properties

#### AuxAddress

_Required_: No
_Type_: List of &lt;a href=&#34;ipamconfig-auxaddress.md&#34;&gt;AuxAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

