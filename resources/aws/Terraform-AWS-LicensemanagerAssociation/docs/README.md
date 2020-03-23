# Terraform::AWS::LicensemanagerAssociation

Provides a License Manager association.

~> **Note:** License configurations can also be associated with launch templates by specifying the `license_specifications` block for an `aws_launch_template`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LicensemanagerAssociation",
    "Properties" : {
        "<a href="#licenseconfigurationarn" title="LicenseConfigurationArn">LicenseConfigurationArn</a>" : <i>String</i>,
        "<a href="#resourcearn" title="ResourceArn">ResourceArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LicensemanagerAssociation
Properties:
    <a href="#licenseconfigurationarn" title="LicenseConfigurationArn">LicenseConfigurationArn</a>: <i>String</i>
    <a href="#resourcearn" title="ResourceArn">ResourceArn</a>: <i>String</i>
</pre>

## Properties

#### LicenseConfigurationArn

ARN of the license configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceArn

ARN of the resource associated with the license configuration.

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

