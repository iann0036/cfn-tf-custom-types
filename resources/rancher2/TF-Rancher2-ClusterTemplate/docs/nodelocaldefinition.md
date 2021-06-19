# TF::Rancher2::ClusterTemplate NodelocalDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#nodeselector" title="NodeSelector">NodeSelector</a>" : <i>[ <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#nodeselector" title="NodeSelector">NodeSelector</a>: <i>
      - <a href="nodeselectordefinition.md">NodeSelectorDefinition</a></i>
</pre>

## Properties

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSelector

_Required_: No

_Type_: List of <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

