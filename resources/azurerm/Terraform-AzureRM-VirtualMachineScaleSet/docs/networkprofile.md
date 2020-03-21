# Terraform::AzureRM::VirtualMachineScaleSet NetworkProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceleratednetworking" title="AcceleratedNetworking">AcceleratedNetworking</a>" : <i>Boolean</i>,
    "<a href="#ipforwarding" title="IpForwarding">IpForwarding</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#dnssettings" title="DnsSettings">DnsSettings</a>" : <i>[ &lt;a href=&#34;networkprofile-dnssettings.md&#34;&gt;DnsSettings&lt;/a&gt;, ... ]</i>,
    "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ &lt;a href=&#34;networkprofile-ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acceleratednetworking" title="AcceleratedNetworking">AcceleratedNetworking</a>: <i>Boolean</i>
<a href="#ipforwarding" title="IpForwarding">IpForwarding</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#dnssettings" title="DnsSettings">DnsSettings</a>: <i>
      - &lt;a href=&#34;networkprofile-dnssettings.md&#34;&gt;DnsSettings&lt;/a&gt;</i>
<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - &lt;a href=&#34;networkprofile-ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### AcceleratedNetworking

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpForwarding

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSettings

_Required_: No
_Type_: List of &lt;a href=&#34;networkprofile-dnssettings.md&#34;&gt;DnsSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;networkprofile-ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

