# TF::RKE::Cluster DnsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodeselector" title="NodeSelector">NodeSelector</a>" : <i>[ <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>, ... ]</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
    "<a href="#reversecidrs" title="ReverseCidrs">ReverseCidrs</a>" : <i>[ String, ... ]</i>,
    "<a href="#upstreamnameservers" title="UpstreamNameservers">UpstreamNameservers</a>" : <i>[ String, ... ]</i>,
    "<a href="#nodelocal" title="Nodelocal">Nodelocal</a>" : <i>[ <a href="nodelocaldefinition.md">NodelocalDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodeselector" title="NodeSelector">NodeSelector</a>: <i>
      - <a href="nodeselectordefinition.md">NodeSelectorDefinition</a></i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
<a href="#reversecidrs" title="ReverseCidrs">ReverseCidrs</a>: <i>
      - String</i>
<a href="#upstreamnameservers" title="UpstreamNameservers">UpstreamNameservers</a>: <i>
      - String</i>
<a href="#nodelocal" title="Nodelocal">Nodelocal</a>: <i>
      - <a href="nodelocaldefinition.md">NodelocalDefinition</a></i>
</pre>

## Properties

#### NodeSelector

_Required_: No

_Type_: List of <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamNameservers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodelocal

_Required_: No

_Type_: List of <a href="nodelocaldefinition.md">NodelocalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

