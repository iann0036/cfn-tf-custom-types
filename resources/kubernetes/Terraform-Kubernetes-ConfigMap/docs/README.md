# Terraform::Kubernetes::ConfigMap

CloudFormation equivalent of kubernetes_config_map

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

_Required_: No

_Type_: List of <a href="binarydata.md">BinaryData</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

_Required_: No

_Type_: List of <a href="data.md">Data</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

