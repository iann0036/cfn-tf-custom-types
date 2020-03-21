# Terraform::Kubernetes::NetworkPolicy

CloudFormation equivalent of kubernetes_network_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::NetworkPolicy",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ &lt;a href=&#34;egress.md&#34;&gt;Egress&lt;/a&gt;, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ &lt;a href=&#34;ingress.md&#34;&gt;Ingress&lt;/a&gt;, ... ]</i>,
        "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ &lt;a href=&#34;podselector.md&#34;&gt;PodSelector&lt;/a&gt;, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>,
        "<a href="#to" title="To">To</a>" : <i>[ &lt;a href=&#34;to.md&#34;&gt;To&lt;/a&gt;, ... ]</i>,
        "<a href="#from" title="From">From</a>" : <i>[ &lt;a href=&#34;from.md&#34;&gt;From&lt;/a&gt;, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;, ... ]</i>,
        "<a href="#ipblock" title="IpBlock">IpBlock</a>" : <i>[ &lt;a href=&#34;ipblock.md&#34;&gt;IpBlock&lt;/a&gt;, ... ]</i>,
        "<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>" : <i>[ &lt;a href=&#34;namespaceselector.md&#34;&gt;NamespaceSelector&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::NetworkPolicy
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#egress" title="Egress">Egress</a>: <i>
      - &lt;a href=&#34;egress.md&#34;&gt;Egress&lt;/a&gt;</i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - &lt;a href=&#34;ingress.md&#34;&gt;Ingress&lt;/a&gt;</i>
    <a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - &lt;a href=&#34;podselector.md&#34;&gt;PodSelector&lt;/a&gt;</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;</i>
    <a href="#to" title="To">To</a>: <i>
      - &lt;a href=&#34;to.md&#34;&gt;To&lt;/a&gt;</i>
    <a href="#from" title="From">From</a>: <i>
      - &lt;a href=&#34;from.md&#34;&gt;From&lt;/a&gt;</i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;</i>
    <a href="#ipblock" title="IpBlock">IpBlock</a>: <i>
      - &lt;a href=&#34;ipblock.md&#34;&gt;IpBlock&lt;/a&gt;</i>
    <a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>: <i>
      - &lt;a href=&#34;namespaceselector.md&#34;&gt;NamespaceSelector&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of &lt;a href=&#34;egress.md&#34;&gt;Egress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of &lt;a href=&#34;ingress.md&#34;&gt;Ingress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No

_Type_: List of &lt;a href=&#34;podselector.md&#34;&gt;PodSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

_Required_: No

_Type_: List of &lt;a href=&#34;to.md&#34;&gt;To&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### From

_Required_: No

_Type_: List of &lt;a href=&#34;from.md&#34;&gt;From&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpBlock

_Required_: No

_Type_: List of &lt;a href=&#34;ipblock.md&#34;&gt;IpBlock&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSelector

_Required_: No

_Type_: List of &lt;a href=&#34;namespaceselector.md&#34;&gt;NamespaceSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

