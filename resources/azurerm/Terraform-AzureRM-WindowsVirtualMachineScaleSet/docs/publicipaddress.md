# Terraform::AzureRM::WindowsVirtualMachineScaleSet PublicIpAddress

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>" : <i>String</i>,
    "<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#publicipprefixid" title="PublicIpPrefixId">PublicIpPrefixId</a>" : <i>String</i>,
    "<a href="#iptag" title="IpTag">IpTag</a>" : <i>[ <a href="publicipaddress-iptag.md">IpTag</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>: <i>String</i>
<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#publicipprefixid" title="PublicIpPrefixId">PublicIpPrefixId</a>: <i>String</i>
<a href="#iptag" title="IpTag">IpTag</a>: <i>
      - <a href="publicipaddress-iptag.md">IpTag</a></i>
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
_Type_: List of <a href="publicipaddress-iptag.md">IpTag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

