# Terraform::FlexibleEngine::AsConfigurationV1

CloudFormation equivalent of flexibleengine_as_configuration_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::AsConfigurationV1",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#scalingconfigurationname" title="ScalingConfigurationName">ScalingConfigurationName</a>" : <i>String</i>,
        "<a href="#instanceconfig" title="InstanceConfig">InstanceConfig</a>" : <i>[ &lt;a href=&#34;instanceconfig.md&#34;&gt;InstanceConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;, ... ]</i>,
        "<a href="#personality" title="Personality">Personality</a>" : <i>[ &lt;a href=&#34;personality.md&#34;&gt;Personality&lt;/a&gt;, ... ]</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>[ &lt;a href=&#34;publicip.md&#34;&gt;PublicIp&lt;/a&gt;, ... ]</i>,
        "<a href="#eip" title="Eip">Eip</a>" : <i>[ &lt;a href=&#34;eip.md&#34;&gt;Eip&lt;/a&gt;, ... ]</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>[ &lt;a href=&#34;bandwidth.md&#34;&gt;Bandwidth&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::AsConfigurationV1
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#scalingconfigurationname" title="ScalingConfigurationName">ScalingConfigurationName</a>: <i>String</i>
    <a href="#instanceconfig" title="InstanceConfig">InstanceConfig</a>: <i>
      - &lt;a href=&#34;instanceconfig.md&#34;&gt;InstanceConfig&lt;/a&gt;</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;</i>
    <a href="#personality" title="Personality">Personality</a>: <i>
      - &lt;a href=&#34;personality.md&#34;&gt;Personality&lt;/a&gt;</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>
      - &lt;a href=&#34;publicip.md&#34;&gt;PublicIp&lt;/a&gt;</i>
    <a href="#eip" title="Eip">Eip</a>: <i>
      - &lt;a href=&#34;eip.md&#34;&gt;Eip&lt;/a&gt;</i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>
      - &lt;a href=&#34;bandwidth.md&#34;&gt;Bandwidth&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;instanceconfig.md&#34;&gt;InstanceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Personality

_Required_: No

_Type_: List of &lt;a href=&#34;personality.md&#34;&gt;Personality&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No

_Type_: List of &lt;a href=&#34;publicip.md&#34;&gt;PublicIp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eip

_Required_: No

_Type_: List of &lt;a href=&#34;eip.md&#34;&gt;Eip&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

_Required_: No

_Type_: List of &lt;a href=&#34;bandwidth.md&#34;&gt;Bandwidth&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

