# Terraform::OpenTelekomCloud::AsConfigurationV1 InstanceConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flavor" title="Flavor">Flavor</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
    "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="instanceconfig-metadata.md">Metadata</a>, ... ]</i>,
    "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="instanceconfig-disk.md">Disk</a>, ... ]</i>,
    "<a href="#personality" title="Personality">Personality</a>" : <i>[ <a href="instanceconfig-personality.md">Personality</a>, ... ]</i>,
    "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>[ <a href="instanceconfig-publicip.md">PublicIp</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#flavor" title="Flavor">Flavor</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
<a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="instanceconfig-metadata.md">Metadata</a></i>
<a href="#userdata" title="UserData">UserData</a>: <i>String</i>
<a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="instanceconfig-disk.md">Disk</a></i>
<a href="#personality" title="Personality">Personality</a>: <i>
      - <a href="instanceconfig-personality.md">Personality</a></i>
<a href="#publicip" title="PublicIp">PublicIp</a>: <i>
      - <a href="instanceconfig-publicip.md">PublicIp</a></i>
</pre>

## Properties

#### Flavor

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No
_Type_: List of <a href="instanceconfig-metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No
_Type_: List of <a href="instanceconfig-disk.md">Disk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Personality

_Required_: No
_Type_: List of <a href="instanceconfig-personality.md">Personality</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No
_Type_: List of <a href="instanceconfig-publicip.md">PublicIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

