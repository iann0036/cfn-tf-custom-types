# Terraform::Docker::Service TaskSpec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Double</i>,
    "<a href="#networks" title="Networks">Networks</a>" : <i>[ String, ... ]</i>,
    "<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>" : <i>[ <a href="taskspec-restartpolicy.md">RestartPolicy</a>, ... ]</i>,
    "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
    "<a href="#containerspec" title="ContainerSpec">ContainerSpec</a>" : <i>[ <a href="taskspec-containerspec.md">ContainerSpec</a>, ... ]</i>,
    "<a href="#logdriver" title="LogDriver">LogDriver</a>" : <i>[ <a href="taskspec-logdriver.md">LogDriver</a>, ... ]</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="taskspec-placement.md">Placement</a>, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="taskspec-resources.md">Resources</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Double</i>
<a href="#networks" title="Networks">Networks</a>: <i>
      - String</i>
<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>: <i>
      - <a href="taskspec-restartpolicy.md">RestartPolicy</a></i>
<a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
<a href="#containerspec" title="ContainerSpec">ContainerSpec</a>: <i>
      - <a href="taskspec-containerspec.md">ContainerSpec</a></i>
<a href="#logdriver" title="LogDriver">LogDriver</a>: <i>
      - <a href="taskspec-logdriver.md">LogDriver</a></i>
<a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="taskspec-placement.md">Placement</a></i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="taskspec-resources.md">Resources</a></i>
</pre>

## Properties

#### ForceUpdate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPolicy

_Required_: No

_Type_: List of <a href="taskspec-restartpolicy.md">RestartPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSpec

_Required_: No

_Type_: List of <a href="taskspec-containerspec.md">ContainerSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDriver

_Required_: No

_Type_: List of <a href="taskspec-logdriver.md">LogDriver</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="taskspec-placement.md">Placement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="taskspec-resources.md">Resources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

