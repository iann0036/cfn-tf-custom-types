# TF::AzureRM::VirtualMachineScaleSet PublicIpAddressConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>" : <i>String</i>,
    "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#domainnamelabel" title="DomainNameLabel">DomainNameLabel</a>: <i>String</i>
<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### DomainNameLabel

The domain name label for the dns settings.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

The idle timeout in minutes. This value must be between 4 and 30.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the public ip address configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

