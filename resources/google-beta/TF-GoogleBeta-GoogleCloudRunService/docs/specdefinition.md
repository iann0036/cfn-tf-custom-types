# TF::GoogleBeta::GoogleCloudRunService SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerconcurrency" title="ContainerConcurrency">ContainerConcurrency</a>" : <i>Double</i>,
    "<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>" : <i>String</i>,
    "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#containers" title="Containers">Containers</a>" : <i>[ <a href="containersdefinition.md">ContainersDefinition</a>, ... ]</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="volumesdefinition.md">VolumesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#containerconcurrency" title="ContainerConcurrency">ContainerConcurrency</a>: <i>Double</i>
<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>: <i>String</i>
<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
<a href="#containers" title="Containers">Containers</a>: <i>
      - <a href="containersdefinition.md">ContainersDefinition</a></i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="volumesdefinition.md">VolumesDefinition</a></i>
</pre>

## Properties

#### ContainerConcurrency

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Containers

_Required_: No

_Type_: List of <a href="containersdefinition.md">ContainersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="volumesdefinition.md">VolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

