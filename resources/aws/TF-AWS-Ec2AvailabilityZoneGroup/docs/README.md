# TF::AWS::Ec2AvailabilityZoneGroup

Manages an EC2 Availability Zone Group, such as updating its opt-in status.

~> **NOTE:** This is an advanced Terraform resource. Terraform will automatically assume management of the EC2 Availability Zone Group without import and perform no actions on removal from configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Ec2AvailabilityZoneGroup",
    "Properties" : {
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#optinstatus" title="OptInStatus">OptInStatus</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Ec2AvailabilityZoneGroup
Properties:
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#optinstatus" title="OptInStatus">OptInStatus</a>: <i>String</i>
</pre>

## Properties

#### GroupName

Name of the Availability Zone Group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptInStatus

Indicates whether to enable or disable Availability Zone Group. Valid values: `opted-in` or `not-opted-in`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

