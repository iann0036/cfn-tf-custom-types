# Terraform::AzureRM::LinuxVirtualMachineScaleSet PublicIpAddress

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>" : <i>String</i>,
    "<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#publicipprefixid" title="PublicIpPrefixId">PublicIpPrefixId</a>" : <i>String</i>,
    "<a href="#iptag" title="IpTag">IpTag</a>" : <i>[ &lt;a href=&#34;publicipaddress-iptag.md&#34;&gt;IpTag&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>: <i>String</i>
<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#publicipprefixid" title="PublicIpPrefixId">PublicIpPrefixId</a>: <i>String</i>
<a href="#iptag" title="IpTag">IpTag</a>: <i>
      - &lt;a href=&#34;publicipaddress-iptag.md&#34;&gt;IpTag&lt;/a&gt;</i>
</pre>

## Properties

#### DomainNameLabel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeoutInMinutes

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpPrefixId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpTag

_Required_: No
_Type_: List of &lt;a href=&#34;publicipaddress-iptag.md&#34;&gt;IpTag&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

