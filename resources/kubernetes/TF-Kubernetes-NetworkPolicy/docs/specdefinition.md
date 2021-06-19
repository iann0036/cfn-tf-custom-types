# TF::Kubernetes::NetworkPolicy SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#policytypes" title="PolicyTypes">PolicyTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="egressdefinition.md">EgressDefinition</a>, ... ]</i>,
    "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingressdefinition.md">IngressDefinition</a>, ... ]</i>,
    "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ <a href="podselectordefinition.md">PodSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#policytypes" title="PolicyTypes">PolicyTypes</a>: <i>
      - String</i>
<a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="egressdefinition.md">EgressDefinition</a></i>
<a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingressdefinition.md">IngressDefinition</a></i>
<a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - <a href="podselectordefinition.md">PodSelectorDefinition</a></i>
</pre>

## Properties

#### PolicyTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of <a href="egressdefinition.md">EgressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingressdefinition.md">IngressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No

_Type_: List of <a href="podselectordefinition.md">PodSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

