# TF::Kubernetes::Ingress

Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Kubernetes::Ingress",
    "Properties" : {
        "<a href="#waitforloadbalancer" title="WaitForLoadBalancer">WaitForLoadBalancer</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="specdefinition.md">SpecDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Kubernetes::Ingress
Properties:
    <a href="#waitforloadbalancer" title="WaitForLoadBalancer">WaitForLoadBalancer</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="specdefinition.md">SpecDefinition</a></i>
</pre>

## Properties

#### WaitForLoadBalancer

Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="specdefinition.md">SpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

