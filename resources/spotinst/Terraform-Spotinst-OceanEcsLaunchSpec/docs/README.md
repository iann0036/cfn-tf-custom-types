# Terraform::Spotinst::OceanEcsLaunchSpec

Provides a custom Spotinst Ocean ECS Launch Spec resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::OceanEcsLaunchSpec",
    "Properties" : {
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oceanid" title="OceanId">OceanId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#attributes" title="Attributes">Attributes</a>" : <i>[ <a href="attributes.md">Attributes</a>, ... ]</i>,
        "<a href="#autoscaleheadrooms" title="AutoscaleHeadrooms">AutoscaleHeadrooms</a>" : <i>[ <a href="autoscaleheadrooms.md">AutoscaleHeadrooms</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::OceanEcsLaunchSpec
Properties:
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oceanid" title="OceanId">OceanId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#attributes" title="Attributes">Attributes</a>: <i>
      - <a href="attributes.md">Attributes</a></i>
    <a href="#autoscaleheadrooms" title="AutoscaleHeadrooms">AutoscaleHeadrooms</a>: <i>
      - <a href="autoscaleheadrooms.md">AutoscaleHeadrooms</a></i>
</pre>

## Properties

#### IamInstanceProfile

The ARN or name of an IAM instance profile to associate with launched instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

ID of the image used to launch the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Ocean Launch Specification name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OceanId

The Ocean cluster ID .

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

One or more security group ids.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Base64-encoded MIME user data to make available to the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attributes

_Required_: No

_Type_: List of <a href="attributes.md">Attributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadrooms

_Required_: No

_Type_: List of <a href="autoscaleheadrooms.md">AutoscaleHeadrooms</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

