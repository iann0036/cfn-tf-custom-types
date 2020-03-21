# Terraform::Kubernetes::NetworkPolicy Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#policytypes" title="PolicyTypes">PolicyTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="spec-egress.md">Egress</a>, ... ]</i>,
    "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="spec-ingress.md">Ingress</a>, ... ]</i>,
    "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ <a href="spec-podselector.md">PodSelector</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#policytypes" title="PolicyTypes">PolicyTypes</a>: <i>
      - String</i>
<a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="spec-egress.md">Egress</a></i>
<a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="spec-ingress.md">Ingress</a></i>
<a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - <a href="spec-podselector.md">PodSelector</a></i>
</pre>

## Properties

#### PolicyTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of <a href="spec-egress.md">Egress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="spec-ingress.md">Ingress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No

_Type_: List of <a href="spec-podselector.md">PodSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

