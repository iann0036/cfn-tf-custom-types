# Terraform::HuaweiCloud::AsConfigurationV1

CloudFormation equivalent of huaweicloud_as_configuration_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::AsConfigurationV1",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#scalingconfigurationname" title="ScalingConfigurationName">ScalingConfigurationName</a>" : <i>String</i>,
        "<a href="#instanceconfig" title="InstanceConfig">InstanceConfig</a>" : <i>[ <a href="instanceconfig.md">InstanceConfig</a>, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="disk.md">Disk</a>, ... ]</i>,
        "<a href="#personality" title="Personality">Personality</a>" : <i>[ <a href="personality.md">Personality</a>, ... ]</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>[ <a href="publicip.md">PublicIp</a>, ... ]</i>,
        "<a href="#eip" title="Eip">Eip</a>" : <i>[ <a href="eip.md">Eip</a>, ... ]</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>[ <a href="bandwidth.md">Bandwidth</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::AsConfigurationV1
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#scalingconfigurationname" title="ScalingConfigurationName">ScalingConfigurationName</a>: <i>String</i>
    <a href="#instanceconfig" title="InstanceConfig">InstanceConfig</a>: <i>
      - <a href="instanceconfig.md">InstanceConfig</a></i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="disk.md">Disk</a></i>
    <a href="#personality" title="Personality">Personality</a>: <i>
      - <a href="personality.md">Personality</a></i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>
      - <a href="publicip.md">PublicIp</a></i>
    <a href="#eip" title="Eip">Eip</a>: <i>
      - <a href="eip.md">Eip</a></i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>
      - <a href="bandwidth.md">Bandwidth</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingConfigurationName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceConfig

_Required_: No

_Type_: List of <a href="instanceconfig.md">InstanceConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="disk.md">Disk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Personality

_Required_: No

_Type_: List of <a href="personality.md">Personality</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No

_Type_: List of <a href="publicip.md">PublicIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eip

_Required_: No

_Type_: List of <a href="eip.md">Eip</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

_Required_: No

_Type_: List of <a href="bandwidth.md">Bandwidth</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

