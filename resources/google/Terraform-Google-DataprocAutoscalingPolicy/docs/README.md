# Terraform::Google::DataprocAutoscalingPolicy

CloudFormation equivalent of google_dataproc_autoscaling_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DataprocAutoscalingPolicy",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#basicalgorithm" title="BasicAlgorithm">BasicAlgorithm</a>" : <i>[ &lt;a href=&#34;basicalgorithm.md&#34;&gt;BasicAlgorithm&lt;/a&gt;, ... ]</i>,
        "<a href="#secondaryworkerconfig" title="SecondaryWorkerConfig">SecondaryWorkerConfig</a>" : <i>[ &lt;a href=&#34;secondaryworkerconfig.md&#34;&gt;SecondaryWorkerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#yarnconfig" title="YarnConfig">YarnConfig</a>" : <i>[ &lt;a href=&#34;yarnconfig.md&#34;&gt;YarnConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DataprocAutoscalingPolicy
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#basicalgorithm" title="BasicAlgorithm">BasicAlgorithm</a>: <i>
      - &lt;a href=&#34;basicalgorithm.md&#34;&gt;BasicAlgorithm&lt;/a&gt;</i>
    <a href="#secondaryworkerconfig" title="SecondaryWorkerConfig">SecondaryWorkerConfig</a>: <i>
      - &lt;a href=&#34;secondaryworkerconfig.md&#34;&gt;SecondaryWorkerConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;</i>
    <a href="#yarnconfig" title="YarnConfig">YarnConfig</a>: <i>
      - &lt;a href=&#34;yarnconfig.md&#34;&gt;YarnConfig&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAlgorithm

_Required_: No

_Type_: List of &lt;a href=&#34;basicalgorithm.md&#34;&gt;BasicAlgorithm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryWorkerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;secondaryworkerconfig.md&#34;&gt;SecondaryWorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YarnConfig

_Required_: No

_Type_: List of &lt;a href=&#34;yarnconfig.md&#34;&gt;YarnConfig&lt;/a&gt;

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

