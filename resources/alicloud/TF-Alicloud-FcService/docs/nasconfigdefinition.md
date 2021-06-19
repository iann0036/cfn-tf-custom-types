# TF::Alicloud::FcService NasConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#groupid" title="GroupId">GroupId</a>" : <i>Double</i>,
    "<a href="#userid" title="UserId">UserId</a>" : <i>Double</i>,
    "<a href="#mountpoints" title="MountPoints">MountPoints</a>" : <i>[ <a href="mountpointsdefinition.md">MountPointsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#groupid" title="GroupId">GroupId</a>: <i>Double</i>
<a href="#userid" title="UserId">UserId</a>: <i>Double</i>
<a href="#mountpoints" title="MountPoints">MountPoints</a>: <i>
      - <a href="mountpointsdefinition.md">MountPointsDefinition</a></i>
</pre>

## Properties

#### GroupId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountPoints

_Required_: No

_Type_: List of <a href="mountpointsdefinition.md">MountPointsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

