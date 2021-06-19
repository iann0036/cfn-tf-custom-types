# TF::AWS::Kinesisanalyticsv2Application ParallelismConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalingenabled" title="AutoScalingEnabled">AutoScalingEnabled</a>" : <i>Boolean</i>,
    "<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>" : <i>String</i>,
    "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>Double</i>,
    "<a href="#parallelismperkpu" title="ParallelismPerKpu">ParallelismPerKpu</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalingenabled" title="AutoScalingEnabled">AutoScalingEnabled</a>: <i>Boolean</i>
<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>: <i>String</i>
<a href="#parallelism" title="Parallelism">Parallelism</a>: <i>Double</i>
<a href="#parallelismperkpu" title="ParallelismPerKpu">ParallelismPerKpu</a>: <i>Double</i>
</pre>

## Properties

#### AutoScalingEnabled

Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationType

Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. Valid values: `CUSTOM`, `DEFAULT`. Set this attribute to `CUSTOM` in order for any specified `auto_scaling_enabled`, `parallelism`, or `parallelism_per_kpu` attribute values to be effective.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

Describes the initial number of parallel tasks that a Flink-based Kinesis Data Analytics application can perform.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParallelismPerKpu

Describes the number of parallel tasks that a Flink-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

