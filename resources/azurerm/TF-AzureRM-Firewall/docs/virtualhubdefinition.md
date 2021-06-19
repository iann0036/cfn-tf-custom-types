# TF::AzureRM::Firewall VirtualHubDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#publicipcount" title="PublicIpCount">PublicIpCount</a>" : <i>Double</i>,
    "<a href="#virtualhubid" title="VirtualHubId">VirtualHubId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#publicipcount" title="PublicIpCount">PublicIpCount</a>: <i>Double</i>
<a href="#virtualhubid" title="VirtualHubId">VirtualHubId</a>: <i>String</i>
</pre>

## Properties

#### PublicIpCount

Specifies the number of public IPs to assign to the Firewall. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualHubId

Specifies the ID of the Virtual Hub where the Firewall resides in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

