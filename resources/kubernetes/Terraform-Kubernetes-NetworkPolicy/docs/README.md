# Terraform::Kubernetes::NetworkPolicy

CloudFormation equivalent of kubernetes_network_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::NetworkPolicy",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="spec.md">Spec</a>, ... ]</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="egress.md">Egress</a>, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingress.md">Ingress</a>, ... ]</i>,
        "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ <a href="podselector.md">PodSelector</a>, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="ports.md">Ports</a>, ... ]</i>,
        "<a href="#to" title="To">To</a>" : <i>[ <a href="to.md">To</a>, ... ]</i>,
        "<a href="#from" title="From">From</a>" : <i>[ <a href="from.md">From</a>, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressions.md">MatchExpressions</a>, ... ]</i>,
        "<a href="#ipblock" title="IpBlock">IpBlock</a>" : <i>[ <a href="ipblock.md">IpBlock</a>, ... ]</i>,
        "<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>" : <i>[ <a href="namespaceselector.md">NamespaceSelector</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::NetworkPolicy
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="spec.md">Spec</a></i>
    <a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="egress.md">Egress</a></i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingress.md">Ingress</a></i>
    <a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - <a href="podselector.md">PodSelector</a></i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="ports.md">Ports</a></i>
    <a href="#to" title="To">To</a>: <i>
      - <a href="to.md">To</a></i>
    <a href="#from" title="From">From</a>: <i>
      - <a href="from.md">From</a></i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressions.md">MatchExpressions</a></i>
    <a href="#ipblock" title="IpBlock">IpBlock</a>: <i>
      - <a href="ipblock.md">IpBlock</a></i>
    <a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>: <i>
      - <a href="namespaceselector.md">NamespaceSelector</a></i>
</pre>

## Properties

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="spec.md">Spec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of <a href="egress.md">Egress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingress.md">Ingress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No

_Type_: List of <a href="podselector.md">PodSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="ports.md">Ports</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

_Required_: No

_Type_: List of <a href="to.md">To</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### From

_Required_: No

_Type_: List of <a href="from.md">From</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressions.md">MatchExpressions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpBlock

_Required_: No

_Type_: List of <a href="ipblock.md">IpBlock</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSelector

_Required_: No

_Type_: List of <a href="namespaceselector.md">NamespaceSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

