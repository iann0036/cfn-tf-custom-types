# TF::Spotinst::OceanEcs OptimizeImagesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#performat" title="PerformAt">PerformAt</a>" : <i>String</i>,
    "<a href="#shouldoptimizeecsami" title="ShouldOptimizeEcsAmi">ShouldOptimizeEcsAmi</a>" : <i>Boolean</i>,
    "<a href="#timewindows" title="TimeWindows">TimeWindows</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#performat" title="PerformAt">PerformAt</a>: <i>String</i>
<a href="#shouldoptimizeecsami" title="ShouldOptimizeEcsAmi">ShouldOptimizeEcsAmi</a>: <i>Boolean</i>
<a href="#timewindows" title="TimeWindows">TimeWindows</a>: <i>
      - String</i>
</pre>

## Properties

#### PerformAt

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldOptimizeEcsAmi

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeWindows

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

