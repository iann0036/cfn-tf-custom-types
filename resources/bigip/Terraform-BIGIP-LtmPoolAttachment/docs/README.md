# Terraform::BIGIP::LtmPoolAttachment

`bigip_ltm_pool_attachment` Manages nodes membership in pools

Resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

Note: node must be the full path to the node followed by the port. For example /Common/my-node:80

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmPoolAttachment",
    "Properties" : {
        "<a href="#node" title="Node">Node</a>" : <i>String</i>,
        "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmPoolAttachment
Properties:
    <a href="#node" title="Node">Node</a>: <i>String</i>
    <a href="#pool" title="Pool">Pool</a>: <i>String</i>
</pre>

## Properties

#### Node

Node to add to the pool in /Partition/NodeName:Port format (e.g. /Common/Node01:80).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

Name of the pool in /Partition/Name format.

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

