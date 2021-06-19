# TF::AzureRM::HdinsightHadoopCluster CapacityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxinstancecount" title="MaxInstanceCount">MaxInstanceCount</a>" : <i>Double</i>,
    "<a href="#mininstancecount" title="MinInstanceCount">MinInstanceCount</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxinstancecount" title="MaxInstanceCount">MaxInstanceCount</a>: <i>Double</i>
<a href="#mininstancecount" title="MinInstanceCount">MinInstanceCount</a>: <i>Double</i>
</pre>

## Properties

#### MaxInstanceCount

The maximum number of worker nodes to autoscale to based on the cluster's activity.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInstanceCount

The minimum number of worker nodes to autoscale to based on the cluster's activity.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

