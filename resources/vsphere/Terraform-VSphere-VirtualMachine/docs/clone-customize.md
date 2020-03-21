# Terraform::VSphere::VirtualMachine Clone Customize

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsserverlist" title="DnsServerList">DnsServerList</a>" : <i>[ String, ... ]</i>,
    "<a href="#dnssuffixlist" title="DnsSuffixList">DnsSuffixList</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipv4gateway" title="Ipv4Gateway">Ipv4Gateway</a>" : <i>String</i>,
    "<a href="#ipv6gateway" title="Ipv6Gateway">Ipv6Gateway</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#windowssyspreptext" title="WindowsSysprepText">WindowsSysprepText</a>" : <i>String</i>,
    "<a href="#linuxoptions" title="LinuxOptions">LinuxOptions</a>" : <i>[ &lt;a href=&#34;clone-customize-linuxoptions.md&#34;&gt;LinuxOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ &lt;a href=&#34;clone-customize-networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;, ... ]</i>,
    "<a href="#windowsoptions" title="WindowsOptions">WindowsOptions</a>" : <i>[ &lt;a href=&#34;clone-customize-windowsoptions.md&#34;&gt;WindowsOptions&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsserverlist" title="DnsServerList">DnsServerList</a>: <i>
      - String</i>
<a href="#dnssuffixlist" title="DnsSuffixList">DnsSuffixList</a>: <i>
      - String</i>
<a href="#ipv4gateway" title="Ipv4Gateway">Ipv4Gateway</a>: <i>String</i>
<a href="#ipv6gateway" title="Ipv6Gateway">Ipv6Gateway</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#windowssyspreptext" title="WindowsSysprepText">WindowsSysprepText</a>: <i>String</i>
<a href="#linuxoptions" title="LinuxOptions">LinuxOptions</a>: <i>
      - &lt;a href=&#34;clone-customize-linuxoptions.md&#34;&gt;LinuxOptions&lt;/a&gt;</i>
<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - &lt;a href=&#34;clone-customize-networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;</i>
<a href="#windowsoptions" title="WindowsOptions">WindowsOptions</a>: <i>
      - &lt;a href=&#34;clone-customize-windowsoptions.md&#34;&gt;WindowsOptions&lt;/a&gt;</i>
</pre>

## Properties

#### DnsServerList

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSuffixList

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Gateway

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Gateway

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsSysprepText

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxOptions

_Required_: No
_Type_: List of &lt;a href=&#34;clone-customize-linuxoptions.md&#34;&gt;LinuxOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No
_Type_: List of &lt;a href=&#34;clone-customize-networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsOptions

_Required_: No
_Type_: List of &lt;a href=&#34;clone-customize-windowsoptions.md&#34;&gt;WindowsOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

