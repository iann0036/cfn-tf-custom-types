# Terraform::Kubernetes::Endpoints

An Endpoints resource is an abstraction, linked to a Service, which defines the list of endpoints that actually implement the service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::Endpoints",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#subset" title="Subset">Subset</a>" : <i>[ <a href="subset.md">Subset</a>, ... ]</i>,
        "<a href="#address" title="Address">Address</a>" : <i>[ <a href="address.md">Address</a>, ... ]</i>,
        "<a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>" : <i>[ <a href="notreadyaddress.md">NotReadyAddress</a>, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>[ <a href="port.md">Port</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::Endpoints
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#subset" title="Subset">Subset</a>: <i>
      - <a href="subset.md">Subset</a></i>
    <a href="#address" title="Address">Address</a>: <i>
      - <a href="address.md">Address</a></i>
    <a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>: <i>
      - <a href="notreadyaddress.md">NotReadyAddress</a></i>
    <a href="#port" title="Port">Port</a>: <i>
      - <a href="port.md">Port</a></i>
</pre>

## Properties

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subset

_Required_: No

_Type_: List of <a href="subset.md">Subset</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Address

_Required_: No

_Type_: List of <a href="address.md">Address</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotReadyAddress

_Required_: No

_Type_: List of <a href="notreadyaddress.md">NotReadyAddress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="port.md">Port</a>

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

