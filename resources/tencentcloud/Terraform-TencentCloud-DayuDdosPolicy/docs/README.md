# Terraform::TencentCloud::DayuDdosPolicy

CloudFormation equivalent of tencentcloud_dayu_ddos_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuDdosPolicy",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#blackips" title="BlackIps">BlackIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#sceneid" title="SceneId">SceneId</a>" : <i>String</i>,
        "<a href="#watermarkkey" title="WatermarkKey">WatermarkKey</a>" : <i>[ &lt;a href=&#34;watermarkkey.md&#34;&gt;WatermarkKey&lt;/a&gt;, ... ]</i>,
        "<a href="#whiteips" title="WhiteIps">WhiteIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#dropoptions" title="DropOptions">DropOptions</a>" : <i>[ &lt;a href=&#34;dropoptions.md&#34;&gt;DropOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#packetfilters" title="PacketFilters">PacketFilters</a>" : <i>[ &lt;a href=&#34;packetfilters.md&#34;&gt;PacketFilters&lt;/a&gt;, ... ]</i>,
        "<a href="#portfilters" title="PortFilters">PortFilters</a>" : <i>[ &lt;a href=&#34;portfilters.md&#34;&gt;PortFilters&lt;/a&gt;, ... ]</i>,
        "<a href="#watermarkfilters" title="WatermarkFilters">WatermarkFilters</a>" : <i>[ &lt;a href=&#34;watermarkfilters.md&#34;&gt;WatermarkFilters&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuDdosPolicy
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#blackips" title="BlackIps">BlackIps</a>: <i>
      - String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#sceneid" title="SceneId">SceneId</a>: <i>String</i>
    <a href="#watermarkkey" title="WatermarkKey">WatermarkKey</a>: <i>
      - &lt;a href=&#34;watermarkkey.md&#34;&gt;WatermarkKey&lt;/a&gt;</i>
    <a href="#whiteips" title="WhiteIps">WhiteIps</a>: <i>
      - String</i>
    <a href="#dropoptions" title="DropOptions">DropOptions</a>: <i>
      - &lt;a href=&#34;dropoptions.md&#34;&gt;DropOptions&lt;/a&gt;</i>
    <a href="#packetfilters" title="PacketFilters">PacketFilters</a>: <i>
      - &lt;a href=&#34;packetfilters.md&#34;&gt;PacketFilters&lt;/a&gt;</i>
    <a href="#portfilters" title="PortFilters">PortFilters</a>: <i>
      - &lt;a href=&#34;portfilters.md&#34;&gt;PortFilters&lt;/a&gt;</i>
    <a href="#watermarkfilters" title="WatermarkFilters">WatermarkFilters</a>: <i>
      - &lt;a href=&#34;watermarkfilters.md&#34;&gt;WatermarkFilters&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlackIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SceneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkKey

_Required_: No

_Type_: List of &lt;a href=&#34;watermarkkey.md&#34;&gt;WatermarkKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhiteIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropOptions

_Required_: No

_Type_: List of &lt;a href=&#34;dropoptions.md&#34;&gt;DropOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketFilters

_Required_: No

_Type_: List of &lt;a href=&#34;packetfilters.md&#34;&gt;PacketFilters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortFilters

_Required_: No

_Type_: List of &lt;a href=&#34;portfilters.md&#34;&gt;PortFilters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkFilters

_Required_: No

_Type_: List of &lt;a href=&#34;watermarkfilters.md&#34;&gt;WatermarkFilters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the &lt;code&gt;CreateTime&lt;/code&gt; value.

#### PolicyId

Returns the &lt;code&gt;PolicyId&lt;/code&gt; value.

#### SceneId

Returns the &lt;code&gt;SceneId&lt;/code&gt; value.

#### WatermarkKey

Returns the &lt;code&gt;WatermarkKey&lt;/code&gt; value.

