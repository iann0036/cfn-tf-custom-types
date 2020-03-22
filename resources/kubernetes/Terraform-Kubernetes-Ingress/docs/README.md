# Terraform::Kubernetes::Ingress

Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::Ingress",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="spec.md">Spec</a>, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backend.md">Backend</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#tls" title="Tls">Tls</a>" : <i>[ <a href="tls.md">Tls</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="http.md">Http</a>, ... ]</i>,
        "<a href="#path" title="Path">Path</a>" : <i>[ <a href="path.md">Path</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::Ingress
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="spec.md">Spec</a></i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backend.md">Backend</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#tls" title="Tls">Tls</a>: <i>
      - <a href="tls.md">Tls</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="http.md">Http</a></i>
    <a href="#path" title="Path">Path</a>: <i>
      - <a href="path.md">Path</a></i>
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

#### Backend

_Required_: No

_Type_: List of <a href="backend.md">Backend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: List of <a href="tls.md">Tls</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="http.md">Http</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="path.md">Path</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### LoadBalancerIngress

Returns the <code>LoadBalancerIngress</code> value.

