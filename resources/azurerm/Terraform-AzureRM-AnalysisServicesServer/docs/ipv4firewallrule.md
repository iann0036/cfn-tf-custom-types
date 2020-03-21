# Terraform::AzureRM::AnalysisServicesServer Ipv4FirewallRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rangeend" title="RangeEnd">RangeEnd</a>" : <i>String</i>,
    "<a href="#rangestart" title="RangeStart">RangeStart</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rangeend" title="RangeEnd">RangeEnd</a>: <i>String</i>
<a href="#rangestart" title="RangeStart">RangeStart</a>: <i>String</i>
</pre>

## Properties

#### Name

Specifies the name of the firewall rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeEnd

End of the firewall rule range as IPv4 address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeStart

Start of the firewall rule range as IPv4 address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

