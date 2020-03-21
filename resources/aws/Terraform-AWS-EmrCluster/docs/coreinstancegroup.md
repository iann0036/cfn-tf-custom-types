# Terraform::AWS::EmrCluster CoreInstanceGroup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalingpolicy" title="AutoscalingPolicy">AutoscalingPolicy</a>" : <i>String</i>,
    "<a href="#bidprice" title="BidPrice">BidPrice</a>" : <i>String</i>,
    "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#ebsconfig" title="EbsConfig">EbsConfig</a>" : <i>[ &lt;a href=&#34;coreinstancegroup-ebsconfig.md&#34;&gt;EbsConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalingpolicy" title="AutoscalingPolicy">AutoscalingPolicy</a>: <i>String</i>
<a href="#bidprice" title="BidPrice">BidPrice</a>: <i>String</i>
<a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#ebsconfig" title="EbsConfig">EbsConfig</a>: <i>
      - &lt;a href=&#34;coreinstancegroup-ebsconfig.md&#34;&gt;EbsConfig&lt;/a&gt;</i>
</pre>

## Properties

#### AutoscalingPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BidPrice

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsConfig

_Required_: No
_Type_: List of &lt;a href=&#34;coreinstancegroup-ebsconfig.md&#34;&gt;EbsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

