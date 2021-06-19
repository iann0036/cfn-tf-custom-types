# TF::Kubernetes::Secret

The resource provides mechanisms to inject containers with sensitive information, such as passwords, while keeping containers agnostic of Kubernetes.
Secrets can be used to store sensitive information either as individual properties or coarse-grained entries like entire files or JSON blobs.
The resource will by default create a secret which is available to any pod in the specified (or default) namespace.

~> Read more about security properties and risks involved with using Kubernetes secrets: [Kubernetes reference](https://kubernetes.io/docs/user-guide/secrets/#security-properties)

~> **Note:** All arguments including the secret data will be stored in the raw state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Kubernetes::Secret",
    "Properties" : {
        "<a href="#binarydata" title="BinaryData">BinaryData</a>" : <i>[ <a href="binarydatadefinition.md">BinaryDataDefinition</a>, ... ]</i>,
        "<a href="#data" title="Data">Data</a>" : <i>[ <a href="datadefinition.md">DataDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Kubernetes::Secret
Properties:
    <a href="#binarydata" title="BinaryData">BinaryData</a>: <i>
      - <a href="binarydatadefinition.md">BinaryDataDefinition</a></i>
    <a href="#data" title="Data">Data</a>: <i>
      - <a href="datadefinition.md">DataDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
</pre>

## Properties

#### BinaryData

A map base64 encoded map of the secret data.

_Required_: No

_Type_: List of <a href="binarydatadefinition.md">BinaryDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

A map of the secret data.

_Required_: No

_Type_: List of <a href="datadefinition.md">DataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The secret type. Defaults to `Opaque`. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/c7151dd8dd7e487e96e5ce34c6a416bb3b037609/contributors/design-proposals/auth/secrets.md#proposed-design).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

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

