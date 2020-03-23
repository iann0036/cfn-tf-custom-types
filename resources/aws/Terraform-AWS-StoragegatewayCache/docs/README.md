# Terraform::AWS::StoragegatewayCache

Manages an AWS Storage Gateway cache.

~> **NOTE:** The Storage Gateway API provides no method to remove a cache disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::StoragegatewayCache",
    "Properties" : {
        "<a href="#diskid" title="DiskId">DiskId</a>" : <i>String</i>,
        "<a href="#gatewayarn" title="GatewayArn">GatewayArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::StoragegatewayCache
Properties:
    <a href="#diskid" title="DiskId">DiskId</a>: <i>String</i>
    <a href="#gatewayarn" title="GatewayArn">GatewayArn</a>: <i>String</i>
</pre>

## Properties

#### DiskId

Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayArn

The Amazon Resource Name (ARN) of the gateway.

_Required_: Yes

_Type_: String

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

