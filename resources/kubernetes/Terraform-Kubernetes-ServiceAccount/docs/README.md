# Terraform::Kubernetes::ServiceAccount

A service account provides an identity for processes that run in a Pod.

Read more at [Kubernetes reference](https://kubernetes.io/docs/admin/service-accounts-admin)/

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::ServiceAccount",
    "Properties" : {
        "<a href="#automountserviceaccounttoken" title="AutomountServiceAccountToken">AutomountServiceAccountToken</a>" : <i>Boolean</i>,
        "<a href="#imagepullsecret" title="ImagePullSecret">ImagePullSecret</a>" : <i>[ <a href="imagepullsecret.md">ImagePullSecret</a>, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secret.md">Secret</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::ServiceAccount
Properties:
    <a href="#automountserviceaccounttoken" title="AutomountServiceAccountToken">AutomountServiceAccountToken</a>: <i>Boolean</i>
    <a href="#imagepullsecret" title="ImagePullSecret">ImagePullSecret</a>: <i>
      - <a href="imagepullsecret.md">ImagePullSecret</a></i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secret.md">Secret</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutomountServiceAccountToken

Boolean, `true` to enable automatic mounting of the service account token.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullSecret

_Required_: No

_Type_: List of <a href="imagepullsecret.md">ImagePullSecret</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="secret.md">Secret</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultSecretName

Returns the <code>DefaultSecretName</code> value.

#### Id

Returns the <code>Id</code> value.

