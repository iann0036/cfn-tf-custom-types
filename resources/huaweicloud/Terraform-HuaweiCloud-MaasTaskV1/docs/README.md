# Terraform::HuaweiCloud::MaasTaskV1

CloudFormation equivalent of huaweicloud_maas_task_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::MaasTaskV1",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablekms" title="EnableKms">EnableKms</a>" : <i>Boolean</i>,
        "<a href="#threadnum" title="ThreadNum">ThreadNum</a>" : <i>Double</i>,
        "<a href="#dstnode" title="DstNode">DstNode</a>" : <i>[ <a href="dstnode.md">DstNode</a>, ... ]</i>,
        "<a href="#smninfo" title="SmnInfo">SmnInfo</a>" : <i>[ <a href="smninfo.md">SmnInfo</a>, ... ]</i>,
        "<a href="#srcnode" title="SrcNode">SrcNode</a>" : <i>[ <a href="srcnode.md">SrcNode</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::MaasTaskV1
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablekms" title="EnableKms">EnableKms</a>: <i>Boolean</i>
    <a href="#threadnum" title="ThreadNum">ThreadNum</a>: <i>Double</i>
    <a href="#dstnode" title="DstNode">DstNode</a>: <i>
      - <a href="dstnode.md">DstNode</a></i>
    <a href="#smninfo" title="SmnInfo">SmnInfo</a>: <i>
      - <a href="smninfo.md">SmnInfo</a></i>
    <a href="#srcnode" title="SrcNode">SrcNode</a>: <i>
      - <a href="srcnode.md">SrcNode</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKms

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadNum

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstNode

_Required_: No

_Type_: List of <a href="dstnode.md">DstNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmnInfo

_Required_: No

_Type_: List of <a href="smninfo.md">SmnInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcNode

_Required_: No

_Type_: List of <a href="srcnode.md">SrcNode</a>

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

#### Name

Returns the <code>Name</code> value.

#### Status

Returns the <code>Status</code> value.

