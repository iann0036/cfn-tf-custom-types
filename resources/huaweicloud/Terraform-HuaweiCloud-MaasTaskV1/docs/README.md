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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#threadnum" title="ThreadNum">ThreadNum</a>" : <i>Double</i>,
        "<a href="#dstnode" title="DstNode">DstNode</a>" : <i>[ &lt;a href=&#34;dstnode.md&#34;&gt;DstNode&lt;/a&gt;, ... ]</i>,
        "<a href="#smninfo" title="SmnInfo">SmnInfo</a>" : <i>[ &lt;a href=&#34;smninfo.md&#34;&gt;SmnInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#srcnode" title="SrcNode">SrcNode</a>" : <i>[ &lt;a href=&#34;srcnode.md&#34;&gt;SrcNode&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::MaasTaskV1
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablekms" title="EnableKms">EnableKms</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#threadnum" title="ThreadNum">ThreadNum</a>: <i>Double</i>
    <a href="#dstnode" title="DstNode">DstNode</a>: <i>
      - &lt;a href=&#34;dstnode.md&#34;&gt;DstNode&lt;/a&gt;</i>
    <a href="#smninfo" title="SmnInfo">SmnInfo</a>: <i>
      - &lt;a href=&#34;smninfo.md&#34;&gt;SmnInfo&lt;/a&gt;</i>
    <a href="#srcnode" title="SrcNode">SrcNode</a>: <i>
      - &lt;a href=&#34;srcnode.md&#34;&gt;SrcNode&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
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

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadNum

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstNode

_Required_: No

_Type_: List of &lt;a href=&#34;dstnode.md&#34;&gt;DstNode&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmnInfo

_Required_: No

_Type_: List of &lt;a href=&#34;smninfo.md&#34;&gt;SmnInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcNode

_Required_: No

_Type_: List of &lt;a href=&#34;srcnode.md&#34;&gt;SrcNode&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;Name&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

