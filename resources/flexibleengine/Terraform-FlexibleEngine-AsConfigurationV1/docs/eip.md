# Terraform::FlexibleEngine::AsConfigurationV1 Eip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#iptype" title="IpType">IpType</a>" : <i>String</i>,
    "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>[ <a href="eip-bandwidth.md">Bandwidth</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#iptype" title="IpType">IpType</a>: <i>String</i>
<a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>
      - <a href="eip-bandwidth.md">Bandwidth</a></i>
</pre>

## Properties

#### IpType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

_Required_: No
_Type_: List of <a href="eip-bandwidth.md">Bandwidth</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

