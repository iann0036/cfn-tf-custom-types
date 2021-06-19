# TF::Kubernetes::NetworkPolicy ToDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipblock" title="IpBlock">IpBlock</a>" : <i>[ <a href="ipblockdefinition.md">IpBlockDefinition</a>, ... ]</i>,
    "<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>" : <i>[ <a href="namespaceselectordefinition.md">NamespaceSelectorDefinition</a>, ... ]</i>,
    "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ <a href="podselectordefinition.md">PodSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipblock" title="IpBlock">IpBlock</a>: <i>
      - <a href="ipblockdefinition.md">IpBlockDefinition</a></i>
<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>: <i>
      - <a href="namespaceselectordefinition.md">NamespaceSelectorDefinition</a></i>
<a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - <a href="podselectordefinition.md">PodSelectorDefinition</a></i>
</pre>

## Properties

#### IpBlock

_Required_: No

_Type_: List of <a href="ipblockdefinition.md">IpBlockDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSelector

_Required_: No

_Type_: List of <a href="namespaceselectordefinition.md">NamespaceSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No

_Type_: List of <a href="podselectordefinition.md">PodSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

