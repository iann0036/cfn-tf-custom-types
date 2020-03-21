# Terraform::OCI::CoreNetworkSecurityGroupSecurityRule UdpOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>" : <i>[ <a href="udpoptions-destinationportrange.md">DestinationPortRange</a>, ... ]</i>,
    "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>[ <a href="udpoptions-sourceportrange.md">SourcePortRange</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>: <i>
      - <a href="udpoptions-destinationportrange.md">DestinationPortRange</a></i>
<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>
      - <a href="udpoptions-sourceportrange.md">SourcePortRange</a></i>
</pre>

## Properties

#### DestinationPortRange

_Required_: No

_Type_: List of <a href="udpoptions-destinationportrange.md">DestinationPortRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

_Required_: No

_Type_: List of <a href="udpoptions-sourceportrange.md">SourcePortRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

