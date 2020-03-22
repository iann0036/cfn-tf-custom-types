# Terraform::Kubernetes::ConfigMap

The resource provides mechanisms to inject containers with configuration data while keeping containers agnostic of Kubernetes.
Config Map can be used to store fine-grained information like individual properties or coarse-grained information like entire config files or JSON blobs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::ConfigMap",
    "Properties" : {
        "<a href="#binarydata" title="BinaryData">BinaryData</a>" : <i>[ <a href="binarydata.md">BinaryData</a>, ... ]</i>,
        "<a href="#data" title="Data">Data</a>" : <i>[ <a href="data.md">Data</a>, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::ConfigMap
Properties:
    <a href="#binarydata" title="BinaryData">BinaryData</a>: <i>
      - <a href="binarydata.md">BinaryData</a></i>
    <a href="#data" title="Data">Data</a>: <i>
      - <a href="data.md">Data</a></i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
</pre>

## Properties

#### BinaryData

BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. This field only accepts base64-encoded payloads that will be decoded/received before being sent/received to the apiserver.

_Required_: No

_Type_: List of <a href="binarydata.md">BinaryData</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process.

_Required_: No

_Type_: List of <a href="data.md">Data</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

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

