# Terraform::AzureRM::LinuxVirtualMachineScaleSet IpConfiguration PublicIpAddress

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>" : <i>String</i>,
    "<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#publicipprefixid" title="PublicIpPrefixId">PublicIpPrefixId</a>" : <i>String</i>,
    "<a href="#iptag" title="IpTag">IpTag</a>" : <i>[ <a href="ipconfiguration-publicipaddress-iptag.md">IpTag</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>: <i>String</i>
<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#publicipprefixid" title="PublicIpPrefixId">PublicIpPrefixId</a>: <i>String</i>
<a href="#iptag" title="IpTag">IpTag</a>: <i>
      - <a href="ipconfiguration-publicipaddress-iptag.md">IpTag</a></i>
</pre>

## Properties

#### DomainNameLabel

The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeoutInMinutes

The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range `4` to `32`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the Public IP Address Configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpPrefixId

The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpTag

_Required_: No

_Type_: List of <a href="ipconfiguration-publicipaddress-iptag.md">IpTag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

