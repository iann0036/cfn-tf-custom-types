# TF::Rancher2::Cluster NodeGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#desiredsize" title="DesiredSize">DesiredSize</a>" : <i>Double</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#ec2sshkey" title="Ec2SshKey">Ec2SshKey</a>" : <i>String</i>,
    "<a href="#gpu" title="Gpu">Gpu</a>" : <i>Boolean</i>,
    "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>, ... ]</i>,
    "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
    "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#requestspotinstances" title="RequestSpotInstances">RequestSpotInstances</a>" : <i>Boolean</i>,
    "<a href="#resourcetags" title="ResourceTags">ResourceTags</a>" : <i>[ <a href="resourcetagsdefinition.md">ResourceTagsDefinition</a>, ... ]</i>,
    "<a href="#spotinstancetypes" title="SpotInstanceTypes">SpotInstanceTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#desiredsize" title="DesiredSize">DesiredSize</a>: <i>Double</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#ec2sshkey" title="Ec2SshKey">Ec2SshKey</a>: <i>String</i>
<a href="#gpu" title="Gpu">Gpu</a>: <i>Boolean</i>
<a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a></i>
<a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
<a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#requestspotinstances" title="RequestSpotInstances">RequestSpotInstances</a>: <i>Boolean</i>
<a href="#resourcetags" title="ResourceTags">ResourceTags</a>: <i>
      - <a href="resourcetagsdefinition.md">ResourceTagsDefinition</a></i>
<a href="#spotinstancetypes" title="SpotInstanceTypes">SpotInstanceTypes</a>: <i>
      - String</i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#userdata" title="UserData">UserData</a>: <i>String</i>
<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a></i>
</pre>

## Properties

#### DesiredSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2SshKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSpotInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTags

_Required_: No

_Type_: List of <a href="resourcetagsdefinition.md">ResourceTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstanceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No

_Type_: List of <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

