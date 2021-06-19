# TF::VCD::NsxtEdgegateway SubnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
    "<a href="#primaryip" title="PrimaryIp">PrimaryIp</a>" : <i>String</i>,
    "<a href="#allocatedips" title="AllocatedIps">AllocatedIps</a>" : <i>[ <a href="allocatedipsdefinition.md">AllocatedIpsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
<a href="#primaryip" title="PrimaryIp">PrimaryIp</a>: <i>String</i>
<a href="#allocatedips" title="AllocatedIps">AllocatedIps</a>: <i>
      - <a href="allocatedipsdefinition.md">AllocatedIpsDefinition</a></i>
</pre>

## Properties

#### Gateway

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllocatedIps

_Required_: No

_Type_: List of <a href="allocatedipsdefinition.md">AllocatedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

