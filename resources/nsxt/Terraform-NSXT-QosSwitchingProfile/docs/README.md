# Terraform::NSXT::QosSwitchingProfile

CloudFormation equivalent of nsxt_qos_switching_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::QosSwitchingProfile",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#classofservice" title="ClassOfService">ClassOfService</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dscppriority" title="DscpPriority">DscpPriority</a>" : <i>Double</i>,
        "<a href="#dscptrusted" title="DscpTrusted">DscpTrusted</a>" : <i>Boolean</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>Double</i>,
        "<a href="#egressrateshaper" title="EgressRateShaper">EgressRateShaper</a>" : <i>[ &lt;a href=&#34;egressrateshaper.md&#34;&gt;EgressRateShaper&lt;/a&gt;, ... ]</i>,
        "<a href="#ingressbroadcastrateshaper" title="IngressBroadcastRateShaper">IngressBroadcastRateShaper</a>" : <i>[ &lt;a href=&#34;ingressbroadcastrateshaper.md&#34;&gt;IngressBroadcastRateShaper&lt;/a&gt;, ... ]</i>,
        "<a href="#ingressrateshaper" title="IngressRateShaper">IngressRateShaper</a>" : <i>[ &lt;a href=&#34;ingressrateshaper.md&#34;&gt;IngressRateShaper&lt;/a&gt;, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::QosSwitchingProfile
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#classofservice" title="ClassOfService">ClassOfService</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dscppriority" title="DscpPriority">DscpPriority</a>: <i>Double</i>
    <a href="#dscptrusted" title="DscpTrusted">DscpTrusted</a>: <i>Boolean</i>
    <a href="#revision" title="Revision">Revision</a>: <i>Double</i>
    <a href="#egressrateshaper" title="EgressRateShaper">EgressRateShaper</a>: <i>
      - &lt;a href=&#34;egressrateshaper.md&#34;&gt;EgressRateShaper&lt;/a&gt;</i>
    <a href="#ingressbroadcastrateshaper" title="IngressBroadcastRateShaper">IngressBroadcastRateShaper</a>: <i>
      - &lt;a href=&#34;ingressbroadcastrateshaper.md&#34;&gt;IngressBroadcastRateShaper&lt;/a&gt;</i>
    <a href="#ingressrateshaper" title="IngressRateShaper">IngressRateShaper</a>: <i>
      - &lt;a href=&#34;ingressrateshaper.md&#34;&gt;IngressRateShaper&lt;/a&gt;</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassOfService

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpPriority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpTrusted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressRateShaper

_Required_: No

_Type_: List of &lt;a href=&#34;egressrateshaper.md&#34;&gt;EgressRateShaper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressBroadcastRateShaper

_Required_: No

_Type_: List of &lt;a href=&#34;ingressbroadcastrateshaper.md&#34;&gt;IngressBroadcastRateShaper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressRateShaper

_Required_: No

_Type_: List of &lt;a href=&#34;ingressrateshaper.md&#34;&gt;IngressRateShaper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.

