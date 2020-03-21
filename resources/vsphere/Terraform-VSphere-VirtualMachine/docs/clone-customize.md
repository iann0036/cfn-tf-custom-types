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
    "<a href="#linuxoptions" title="LinuxOptions">LinuxOptions</a>" : <i>[ <a href="clone-customize-linuxoptions.md">LinuxOptions</a>, ... ]</i>,
    "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="clone-customize-networkinterface.md">NetworkInterface</a>, ... ]</i>,
    "<a href="#windowsoptions" title="WindowsOptions">WindowsOptions</a>" : <i>[ <a href="clone-customize-windowsoptions.md">WindowsOptions</a>, ... ]</i>
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
      - <a href="clone-customize-linuxoptions.md">LinuxOptions</a></i>
<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="clone-customize-networkinterface.md">NetworkInterface</a></i>
<a href="#windowsoptions" title="WindowsOptions">WindowsOptions</a>: <i>
      - <a href="clone-customize-windowsoptions.md">WindowsOptions</a></i>
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
_Type_: List of <a href="clone-customize-linuxoptions.md">LinuxOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No
_Type_: List of <a href="clone-customize-networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsOptions

_Required_: No
_Type_: List of <a href="clone-customize-windowsoptions.md">WindowsOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

