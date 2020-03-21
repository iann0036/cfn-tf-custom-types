# Terraform::VCD::NetworkIsolated DhcpPool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultleasetime" title="DefaultLeaseTime">DefaultLeaseTime</a>" : <i>Double</i>,
    "<a href="#endaddress" title="EndAddress">EndAddress</a>" : <i>String</i>,
    "<a href="#maxleasetime" title="MaxLeaseTime">MaxLeaseTime</a>" : <i>Double</i>,
    "<a href="#startaddress" title="StartAddress">StartAddress</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#defaultleasetime" title="DefaultLeaseTime">DefaultLeaseTime</a>: <i>Double</i>
<a href="#endaddress" title="EndAddress">EndAddress</a>: <i>String</i>
<a href="#maxleasetime" title="MaxLeaseTime">MaxLeaseTime</a>: <i>Double</i>
<a href="#startaddress" title="StartAddress">StartAddress</a>: <i>String</i>
</pre>

## Properties

#### DefaultLeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

