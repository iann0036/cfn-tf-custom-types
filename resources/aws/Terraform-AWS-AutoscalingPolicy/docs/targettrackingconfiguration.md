# Terraform::AWS::AutoscalingPolicy TargetTrackingConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>" : <i>Boolean</i>,
    "<a href="#targetvalue" title="TargetValue">TargetValue</a>" : <i>Double</i>,
    "<a href="#customizedmetricspecification" title="CustomizedMetricSpecification">CustomizedMetricSpecification</a>" : <i>[ &lt;a href=&#34;targettrackingconfiguration-customizedmetricspecification.md&#34;&gt;CustomizedMetricSpecification&lt;/a&gt;, ... ]</i>,
    "<a href="#predefinedmetricspecification" title="PredefinedMetricSpecification">PredefinedMetricSpecification</a>" : <i>[ &lt;a href=&#34;targettrackingconfiguration-predefinedmetricspecification.md&#34;&gt;PredefinedMetricSpecification&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>: <i>Boolean</i>
<a href="#targetvalue" title="TargetValue">TargetValue</a>: <i>Double</i>
<a href="#customizedmetricspecification" title="CustomizedMetricSpecification">CustomizedMetricSpecification</a>: <i>
      - &lt;a href=&#34;targettrackingconfiguration-customizedmetricspecification.md&#34;&gt;CustomizedMetricSpecification&lt;/a&gt;</i>
<a href="#predefinedmetricspecification" title="PredefinedMetricSpecification">PredefinedMetricSpecification</a>: <i>
      - &lt;a href=&#34;targettrackingconfiguration-predefinedmetricspecification.md&#34;&gt;PredefinedMetricSpecification&lt;/a&gt;</i>
</pre>

## Properties

#### DisableScaleIn

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetValue

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedMetricSpecification

_Required_: No
_Type_: List of &lt;a href=&#34;targettrackingconfiguration-customizedmetricspecification.md&#34;&gt;CustomizedMetricSpecification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedMetricSpecification

_Required_: No
_Type_: List of &lt;a href=&#34;targettrackingconfiguration-predefinedmetricspecification.md&#34;&gt;PredefinedMetricSpecification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

