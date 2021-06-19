# TF::TencentCloud::KubernetesCluster ExistInstanceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#desiredpodnumbers" title="DesiredPodNumbers">DesiredPodNumbers</a>" : <i>[ Double, ... ]</i>,
    "<a href="#noderole" title="NodeRole">NodeRole</a>" : <i>String</i>,
    "<a href="#instancespara" title="InstancesPara">InstancesPara</a>" : <i>[ <a href="instancesparadefinition.md">InstancesParaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#desiredpodnumbers" title="DesiredPodNumbers">DesiredPodNumbers</a>: <i>
      - Double</i>
<a href="#noderole" title="NodeRole">NodeRole</a>: <i>String</i>
<a href="#instancespara" title="InstancesPara">InstancesPara</a>: <i>
      - <a href="instancesparadefinition.md">InstancesParaDefinition</a></i>
</pre>

## Properties

#### DesiredPodNumbers

Custom mode cluster, you can specify the number of pods for each node. corresponding to the existed_instances_para.instance_ids parameter.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeRole

Role of existed node. value:MASTER_ETCD or WORKER.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancesPara

_Required_: No

_Type_: List of <a href="instancesparadefinition.md">InstancesParaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

